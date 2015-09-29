# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import users
from models import Salary
from models import Kontakt


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}

        user = users.get_current_user()
        if user:
            if users.is_current_user_admin():
                admin = True
                params["admin"] = admin
            logged_in = True
            logout_url = users.create_logout_url("/")
            params["logged_in"] = logged_in
            params["user"] = user
            params["logout_url"] = logout_url
        else:
            logged_in = False
            login_url = users.create_login_url("/")
            params["logged_in"] = logged_in
            params["user"] = user
            params["login_url"] = login_url

        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")


class DodajHandler(BaseHandler):
    def get(self):
        self.render_template("dodaj.html")


class DodanoHandler(BaseHandler):
    def post(self):
        date = self.request.get("date")
        start = self.request.get("start")
        end = self.request.get("end")
        job_name = self.request.get("job_name")
        eur_hour = self.request.get("eur_hour")
        note = self.request.get("note")
        user = str(users.get_current_user())

        if note == "":
            note = "brez"

        if eur_hour.find(",") != -1:
            eur_hour = eur_hour.replace(",", ".")

        eur_hour = float(eur_hour)

        ts = start
        te = end

        (h, m) = ts.split(":")

        result1 = int(h) * 3600 + int(m) * 60

        (h, m) = te.split(":")

        result2 = int(h) * 3600 + int(m) * 60

        result = result2 - result1

        result = float(result) / 3600.0
        result = str(result)
        (h, m) = result.split(".")
        h = str(h)
        m = str(m)

        m = ("0.%s") % m
        m = float(m)
        m = m * 60.0
        m = round(m)
        m = int(m)
        m = str(m)

        if len(m) < 2:
            m = ("0%s") % (m)

        total_hrs = ("%s:%s") % (h, m)

        dm = float(m) / 60.0
        dm = str(dm)

        (dh, dm2) = dm.split(".")
        daily = ("%s.%s") % (h, dm2)

        daily = float(daily) * eur_hour
        daily = round(daily, 2)

        dailywtax = daily * (1.0 - 0.155)
        dailywtax = round(dailywtax, 2)

        daily = str(daily)
        dailywtax = str(dailywtax)

        if daily.find(".") != -1:
            daily = daily.replace(".", ",")

        if dailywtax.find(".") != -1:
            dailywtax = dailywtax.replace(".", ",")

        eur_hour = str(eur_hour)

        if eur_hour.find(".") != -1:
            eur_hour = eur_hour.replace(".", ",")

        (m, d, y) = date.split("/")

        date = ("%s.%s.%s") % (d, m, y)

        salary = Salary(date=date, start=start, end=end, job_name=job_name, eur_hour=eur_hour, note=note, user=user,
                        total_hrs=total_hrs, daily=daily, dailywtax=dailywtax, d=d, m=m, y=y)
        salary.put()

        self.render_template("dodano.html")


class TableHandler(BaseHandler):
    def get(self, table_id):
        table = Salary.get_by_id(int(table_id))

        params = {"table": table}

        self.render_template("table.html", params)


class TableDelete(BaseHandler):
    def get(self, table_id):
        table = Salary.get_by_id(int(table_id))

        params = {"table": table}

        self.render_template("table_delete.html", params)

    def post(self, table_id):
        table = Salary.get_by_id(int(table_id))
        table.key.delete()
        return self.redirect_to("pregled")


class AdminHandler(BaseHandler):
    def get(self):

        self.render_template("admin.html")


class SporociloOddano(BaseHandler):
    def post(self):
        name = self.request.get("name")
        email = self.request.get("email")
        message = self.request.get("message")
        user = str(users.get_current_user())

        kontakt = Kontakt(name=name, email=email, message=message, user=user)
        kontakt.put()

        self.render_template("sporocilo_oddano.html")


class KontaktHandler(BaseHandler):
    def get(self):
        message = Kontakt.query().order(-Kontakt.created).fetch()

        params = {"message": message}

        self.render_template("kontakt.html", params)
