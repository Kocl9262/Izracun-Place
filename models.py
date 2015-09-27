# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


class Salary(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    date = ndb.StringProperty(indexed=True)
    start = ndb.StringProperty(indexed=False)
    end = ndb.StringProperty(indexed=False)
    job_name = ndb.StringProperty(indexed=True)
    eur_hour = ndb.StringProperty(indexed=False)
    note = ndb.StringProperty(indexed=False)
    user = ndb.StringProperty(indexed=True)
    total_hrs = ndb.StringProperty(indexed=False)
    daily = ndb.StringProperty(indexed=False)
    dailywtax = ndb.StringProperty(indexed=False)
    d = ndb.StringProperty(indexed=True)
    m = ndb.StringProperty(indexed=True)
    y = ndb.StringProperty(indexed=True)


class Kontakt(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    message = ndb.StringProperty(indexed=False)
