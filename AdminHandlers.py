# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import users
from BasicHandlers import BaseHandler
from models import Kontakt


class AdminHandler(BaseHandler):
    def get(self):

        self.render_template("/admin/admin.html")


class SporociloOddano(BaseHandler):
    def post(self):
        name = self.request.get("name")
        email = self.request.get("email")
        message = self.request.get("message")
        user = str(users.get_current_user())

        kontakt = Kontakt(name=name, email=email, message=message, user=user)
        kontakt.put()

        self.render_template("/admin/sporocilo_oddano.html")


class KontaktHandler(BaseHandler):
    def get(self):
        message = Kontakt.query().order(-Kontakt.created).fetch()

        params = {"message": message}

        self.render_template("admin/kontakt.html", params)


class MessageHandler(BaseHandler):
    def get(self, msg_id):
        msg = Kontakt.get_by_id(int(msg_id))

        params = {"msg": msg}

        self.render_template("admin/msg.html", params)
