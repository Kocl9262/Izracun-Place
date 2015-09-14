# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import users
from models import Salary
from BasicHandlers import BaseHandler


class L2015Handler(BaseHandler):
    def get(self):
        current_user = users.get_current_user()

        if current_user:
            salary = Salary.query(Salary.user == current_user.nickname(), Salary.y == "2015").order(Salary.date).fetch()

            daily = []

            for item in salary:
                daily.append(item.daily)

            daily = [w.replace(',', '.') for w in daily]
            daily = map(float, daily)
            month_total_daily = sum(daily)

            dailywtax = []

            for item in salary:
                dailywtax.append(item.dailywtax)

            dailywtax = [w.replace(',', '.') for w in dailywtax]
            dailywtax = map(float, dailywtax)
            month_total_dailywtax = sum(dailywtax)

            total_hrs = []

            for item in salary:
                (h, m) = item.total_hrs.split(":")
                result = int(h) * 3600 + int(m) * 60
                total_hrs.append(result)

            result = sum(total_hrs)

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

            month_total_hrs = ("%s:%s") % (h, m)

            params = {"salary": salary, "month_total_daily": month_total_daily,
                      "month_total_dailywtax": month_total_dailywtax, "month_total_hrs": month_total_hrs}

            self.render_template("l2015.html", params)

        else:
            return self.render_template("l2015.html")


class Januar15Handler(BaseHandler):
    def get(self):
        current_user = users.get_current_user()

        if current_user:
            salary = Salary.query(Salary.user == current_user.nickname(), Salary.m == "01",
                                  Salary.y == "2015").order(Salary.date).fetch()

            daily = []

            for item in salary:
                daily.append(item.daily)

            daily = [w.replace(',', '.') for w in daily]
            daily = map(float, daily)
            month_total_daily = sum(daily)

            dailywtax = []

            for item in salary:
                dailywtax.append(item.dailywtax)

            dailywtax = [w.replace(',', '.') for w in dailywtax]
            dailywtax = map(float, dailywtax)
            month_total_dailywtax = sum(dailywtax)

            total_hrs = []

            for item in salary:
                (h, m) = item.total_hrs.split(":")
                result = int(h) * 3600 + int(m) * 60
                total_hrs.append(result)

            result = sum(total_hrs)

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

            month_total_hrs = ("%s:%s") % (h, m)

            params = {"salary": salary, "month_total_daily": month_total_daily,
                      "month_total_dailywtax": month_total_dailywtax, "month_total_hrs": month_total_hrs}

            self.render_template("januar15.html", params)

        else:
            return self.render_template("januar15.html")


class Februar15Handler(BaseHandler):
    def get(self):
        current_user = users.get_current_user()

        if current_user:
            salary = Salary.query(Salary.user == current_user.nickname(), Salary.m == "02",
                                  Salary.y == "2015").order(Salary.date).fetch()

            daily = []

            for item in salary:
                daily.append(item.daily)

            daily = [w.replace(',', '.') for w in daily]
            daily = map(float, daily)
            month_total_daily = sum(daily)

            dailywtax = []

            for item in salary:
                dailywtax.append(item.dailywtax)

            dailywtax = [w.replace(',', '.') for w in dailywtax]
            dailywtax = map(float, dailywtax)
            month_total_dailywtax = sum(dailywtax)

            total_hrs = []

            for item in salary:
                (h, m) = item.total_hrs.split(":")
                result = int(h) * 3600 + int(m) * 60
                total_hrs.append(result)

            result = sum(total_hrs)

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

            month_total_hrs = ("%s:%s") % (h, m)

            params = {"salary": salary, "month_total_daily": month_total_daily,
                      "month_total_dailywtax": month_total_dailywtax, "month_total_hrs": month_total_hrs}

            self.render_template("februar15.html", params)

        else:
            return self.render_template("februar15.html")
