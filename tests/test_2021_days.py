# -*- coding: utf-8 -*-
import datetime
import unittest

import chinese_calendar as calendar


class In2021Tests(unittest.TestCase):

    def test_in_lieu_should_equal_workdays_amount(self):
        days_2021 = calendar.get_dates(datetime.date(2021, 1, 1), datetime.date(2021, 12, 31))
        id = 0
        print(days_2021)
        for day in days_2021:
            # print(day, calendar.get_holiday_detail(day), calendar.is_in_lieu(day))

            sql_temp = 'INSERT INTO "BASE_ADM"."CUSTOM_CALENDAR"("ID", "OPTIMISTIC", "CREATE_TIME", "CALENDAR_TYPE", "CALENDAR_DATE", "STATUS") VALUES ({0}, {1}, {2}, {3}, {4}, {5});'
            id += 1
            sql = sql_temp.format(id, 0, "SYSDATE", "'HOLIDAY'" if calendar.is_holiday(day) else "'WORKDAY'",
                                  "DATE'" + day.strftime('%Y-%m-%d') + "'",
                                  "'ENABLE'")
            print(sql)
