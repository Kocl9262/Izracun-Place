# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import users
from google.appengine.api import urlfetch
from models import Salary
from BasicHandlers import MainHandler, DodajHandler, DodanoHandler, TableHandler, TableDelete
from Pregled2015 import L2015Handler, Januar15Handler, Februar15Handler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/dodaj', DodajHandler),
    webapp2.Route('/dodano', DodanoHandler),
    webapp2.Route('/table/<table_id:\d+>', TableHandler),
    webapp2.Route('/table/<table_id:\d+>/delete', TableDelete),
    webapp2.Route('/l2015', L2015Handler,  name="pregled"),
    webapp2.Route('/januar15', Januar15Handler),
    webapp2.Route('/februar15', Februar15Handler),
], debug=True)
