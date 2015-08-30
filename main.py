<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
>>>>>>> ef79633fe237f45d31a35ec88d8e49eabcfd0b41
#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import users
from google.appengine.api import urlfetch
<<<<<<< HEAD
from models import Placa
=======
from models import Salary
>>>>>>> ef79633fe237f45d31a35ec88d8e49eabcfd0b41


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

<<<<<<< HEAD
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
=======

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

        salary = Salary(date=date, start=start, end=end, job_name=job_name, eur_hour=eur_hour, note=note, user=user)
        salary.put()

        self.render_template("dodano.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/dodaj', DodajHandler),
    webapp2.Route('/dodano', DodanoHandler),
>>>>>>> ef79633fe237f45d31a35ec88d8e49eabcfd0b41
], debug=True)
