from google.appengine.api import users
from models import Salary


def year(self, leto):
    current_user = users.get_current_user()

    if current_user:
        salary = Salary.query(Salary.user == current_user.nickname(), Salary.y == leto).order(Salary.m).fetch()

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

        month_total_daily = str(month_total_daily)
        month_total_dailywtax = str(month_total_dailywtax)

        if month_total_daily.find(".") != -1:
            month_total_daily = month_total_daily.replace(".", ",")

        if month_total_dailywtax.find(".") != -1:
            month_total_dailywtax = month_total_dailywtax.replace(".", ",")

        params = {"salary": salary, "month_total_daily": month_total_daily,
                  "month_total_dailywtax": month_total_dailywtax, "month_total_hrs": month_total_hrs}

        self.render_template("/leto2015/l2015.html", params)

    else:
        return self.render_template("/leto2015/l2015.html")


def month(self, mesec, leto, mesec_html):
    current_user = users.get_current_user()

    if current_user:
        salary = Salary.query(Salary.user == current_user.nickname(), Salary.m == mesec,
                              Salary.y == leto).order(Salary.date).fetch()

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

        month_total_daily = str(month_total_daily)
        month_total_dailywtax = str(month_total_dailywtax)

        if month_total_daily.find(".") != -1:
            month_total_daily = month_total_daily.replace(".", ",")

        if month_total_dailywtax.find(".") != -1:
            month_total_dailywtax = month_total_dailywtax.replace(".", ",")

        params = {"salary": salary, "month_total_daily": month_total_daily,
                  "month_total_dailywtax": month_total_dailywtax, "month_total_hrs": month_total_hrs}

        self.render_template(mesec_html, params)

    else:
        return self.render_template(mesec_html)
