# -*- coding: utf-8 -*-
#!/usr/bin/env python
from BasicHandlers import BaseHandler
from formule import year, month


class L2016Handler(BaseHandler):
    def get(self):
        year(self, "2016")


class Januar16Handler(BaseHandler):
    def get(self):
        month(self, "01", "2016", "/leto2016/januar16.html")


class Februar16Handler(BaseHandler):
    def get(self):
        month(self, "02", "2016", "/leto2016/februar16.html")


class Marec16Handler(BaseHandler):
    def get(self):
        month(self, "03", "2016", "/leto2016/marec16.html")


class April16Handler(BaseHandler):
    def get(self):
        month(self, "04", "2016", "/leto2016/april16.html")


class Maj16Handler(BaseHandler):
    def get(self):
        month(self, "05", "2016", "/leto2016/maj16.html")


class Junij16Handler(BaseHandler):
    def get(self):
        month(self, "06", "2016", "/leto2016/junij16.html")


class Julij16Handler(BaseHandler):
    def get(self):
        month(self, "07", "2016", "/leto2016/julij16.html")


class Avgust16Handler(BaseHandler):
    def get(self):
        month(self, "08", "2016", "/leto2016/avgust16.html")


class September16Handler(BaseHandler):
    def get(self):
        month(self, "09", "2016", "/leto2016/september16.html")


class Oktober16Handler(BaseHandler):
    def get(self):
        month(self, "10", "2016", "/leto2016/oktober16.html")


class November16Handler(BaseHandler):
    def get(self):
        month(self, "11", "2016", "/leto2016/november16.html")


class December16Handler(BaseHandler):
    def get(self):
        month(self, "12", "2016", "/leto2016/december16.html")
