# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import users
from google.appengine.api import urlfetch
from models import Salary


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
        h = int(h)
        m = int(m)

        m = ("0.%s") % m
        m = float(m)
        m = m * 60.0
        m = float(m)
        m = round(m)
        m = int(m)

        whours = ("%s:%s") % (h, m)

        salary = Salary(date=date, start=start, end=end, job_name=job_name, eur_hour=eur_hour, note=note, user=user,
                        whours=whours)
        salary.put()

        self.render_template("dodano.html")


class PregledHandler(BaseHandler):
    def get(self):
        current_user = users.get_current_user()

        if current_user:
            salary = Salary.query(Salary.user == current_user.nickname()).order(-Salary.date).fetch()

            params = {"salary": salary}

            self.render_template("pregled.html", params)

        else:
            return self.render_template("pregled.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/dodaj', DodajHandler),
    webapp2.Route('/dodano', DodanoHandler),
    webapp2.Route('/pregled', PregledHandler),
], debug=True)
