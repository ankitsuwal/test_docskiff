from datetime import datetime, date, timedelta
from calendar import monthcalendar, SATURDAY


class IntervalDates:
    """
    A class used for provide or print interval dates between range
    :param(str) s_date(starting date), e_date(end date)
    methods:
    is_valid: checking date format is valid or not.
    daterange: generator, providing dates between range.
    interval_dates: showing dates on behalf of test cases.
    """
    def __init__(self, s_date, e_date):
        self.s_date = s_date
        self.e_date = e_date
        self.format = "'%Y%m%d"

    def is_valid(self):
        ll = [self.s_date, self.e_date]
        if int(self.s_date) > int(self.e_date):
            raise ValueError("Start date should be less than end date.")
        for date in ll:
            try:
                datetime.strptime(date, '%Y%m%d')
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYYMMDD")

    def daterange(self, date1, date2):
        for n in range(int((date2 - date1).days) + 1):
            yield date1 + timedelta(n)

    def interval_dates(self):
        syyyy, smm, sdd = int(self.s_date[:4]), int(self.s_date[4:6]), int(self.s_date[6:8])
        eyyyy, emm, edd = int(self.e_date[:4]), int(self.e_date[4:6]), int(self.e_date[6:8])
        s_date = date(syyyy, smm, sdd)
        e_date = date(eyyyy, emm, edd)
        for dt in self.daterange(s_date, e_date):
            day = datetime.strptime(dt.strftime("%Y%m%d"), '%Y%m%d').weekday()
            if day == 5:
                month_calender = monthcalendar(dt.year, dt.month)
                fourth_sat = month_calender[3][SATURDAY] if month_calender[0][SATURDAY] else month_calender[4][SATURDAY]
                if fourth_sat == int(dt.day) and fourth_sat % 5 != 0:
                    print(dt.strftime("%Y%m%d"))
                elif int(dt.day) % 5 == 0 and fourth_sat != int(dt.day):
                    print(dt.strftime("%Y%m%d"))


if __name__ == "__main__":
    s_date = str(input("Enter the start date<%Y%m%d>: "))
    e_date = str(input("Enter the  end  date<%Y%m%d>: "))
    # s_date, e_date = "20180728", "20180927"
    obj = IntervalDates(s_date, e_date)
    obj.is_valid()
    obj.interval_dates()
