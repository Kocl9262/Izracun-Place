<<<<<<< HEAD
from google.appengine.ext import ndb


class Placa(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    to = ndb.StringProperty()
    subject = ndb.StringProperty()
    msg = ndb.TextProperty()
    from_user = ndb.StringProperty()
    read = ndb.BooleanProperty(default=False)
=======
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
>>>>>>> ef79633fe237f45d31a35ec88d8e49eabcfd0b41
