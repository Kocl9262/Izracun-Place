# -*- coding: utf-8 -*-
#!/usr/bin/env python
from BasicHandlers import BaseHandler
from formule import year, month


class L2015Handler(BaseHandler):
    def get(self):
        year(self, "2015")


class Januar15Handler(BaseHandler):
    def get(self):
        month(self, "01", "2015", "/leto2015/januar15.html")


class Februar15Handler(BaseHandler):
    def get(self):
        month(self, "02", "2015", "/leto2015/februar15.html")


class Marec15Handler(BaseHandler):
    def get(self):
        month(self, "03", "2015", "/leto2015/marec15.html")


class April15Handler(BaseHandler):
    def get(self):
        month(self, "04", "2015", "/leto2015/april15.html")


class Maj15Handler(BaseHandler):
    def get(self):
        month(self, "05", "2015", "/leto2015/maj15.html")


class Junij15Handler(BaseHandler):
    def get(self):
        month(self, "06", "2015", "/leto2015/junij15.html")


class Julij15Handler(BaseHandler):
    def get(self):
        month(self, "07", "2015", "/leto2015/julij15.html")


class Avgust15Handler(BaseHandler):
    def get(self):
        month(self, "08", "2015", "/leto2015/avgust15.html")


class September15Handler(BaseHandler):
    def get(self):
        month(self, "09", "2015", "/leto2015/september15.html")


class Oktober15Handler(BaseHandler):
    def get(self):
        month(self, "10", "2015", "/leto2015/oktober15.html")


class November15Handler(BaseHandler):
    def get(self):
        month(self, "11", "2015", "/leto2015/november15.html")


class December15Handler(BaseHandler):
    def get(self):
        month(self, "12", "2015", "/leto2015/december15.html")
