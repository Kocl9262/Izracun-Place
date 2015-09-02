# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


class Salary(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    date = ndb.StringProperty()
    start = ndb.StringProperty()
    end = ndb.StringProperty()
    job_name = ndb.StringProperty()
    eur_hour = ndb.StringProperty()
    note = ndb.StringProperty()
    user = ndb.StringProperty()
    whours = ndb.StringProperty()
