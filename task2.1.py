import calendar
from datetime import datetime
import json


def round_date_after_sub(function):
    """creating a decorator to reduce the date after adding"""

    def rounding(*args):
        with open("months.json") as f:
            months_dict = json.load(f)
        day, month, year = function(*args)
        while (month < 1):
            year -= 1
            month += 12
        while (0 > day):
            try:
                month -= 1
                day += months_dict[str(month)]
            except:
                month += 12
                year -= 1
        return Calendar(day, month, year)

    return rounding


def round_date_after_add(function):
    """creating a decorator to reduce the date after adding"""

    def rounding(*args):
        with open("months.json") as f:
            months_dict = json.load(f)
        day, month, year = function(*args)
        while (month > 12):
            year += 1
            month -= 12
        while (months_dict[str(month)] < day):
            try:
                month += 1
                day -= months_dict[str(month)]
            except:
                month %= 12
                year += 1
        return Calendar(day, month, year)

    return rounding


class Calendar:

    def __init__(self, day, month, year):
        with open("months.json") as f:
            months = json.load(f)
        if not all(isinstance(date, int) for date in (day, month, year)):
            raise TypeError("Day, month and year must be integer")
        if 0 > month or month > 12:
            raise ValueError("Month must be from 0 to 12")
        self.month = month
        if calendar.isleap(year) and month == 2:
            months[str(month)] = 29
        elif not calendar.isleap(year) and month == 2:
            months[str(month)] = 28
        if months[str(month)] < day or day < 0:
            raise ValueError("Incorrect data. Wrong input, there is no such day this month")
        self.day = day
        self.year = year
        self.date = (self.year, self.month, self.day)

    def __eq__(self, other):
        """overloading the equal operator"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        return self.date == other.date

    def __lt__(self, other):
        """overloading comparison date1 < date2"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        return self.date < other.date

    def __le__(self, other):
        """overloading comparison date1 <= date2"""
        return self.date <= other.date

    def __gt__(self, other):
        """overloading comparison date1 > date2"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        return self.date > other.date

    def __ge__(self, other):
        """overloading comparison date1 >= date2"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        return self.date >= other.date

    def __ge__(self, other):
        """overloading comparison date1 >= date2"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        return self.date != other.date

    @round_date_after_add
    def __add__(self, other):
        """overloading the add operator to add dates"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        year = self.year + other.year
        month = self.month + other.month
        day = self.day + other.day
        return day, month, year

    @round_date_after_sub
    def __sub__(self, other):
        """overloading the add operator to substract dates"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        year = self.year - other.year
        month = self.month - other.month
        day = self.day - other.day
        return day, month, year

    def __str__(self):
        return f'Current date:\nYear: {self.year}\nMonth: {self.month}\nDay: {self.day}'


date1 = Calendar(22, 12, 2015)
date2 = Calendar(29, 2, 2016)
date3 = Calendar(29, 12, 2016)
print(f'date 1 = date 3: {date1 == date3}')
print(f'date 1 < date 3: {date1 < date2}')
print(f'date 1 <= date 2: {date1 <= date2}')
print(f'date 1 <= date 3: {date1 <= date3}')
print(f'date 1 > date 2: {date1 > date2}')
print(f'date 1 >= date 2: {date1 >= date2}')
print(f'date 1 >= date 2: {date2 >= date3}')
print(f'date 1 != date 2: {date2 != date1}')
print(f'{date1 + date3}')
print(f'{date2 - date1}')