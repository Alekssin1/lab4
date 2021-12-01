import calendar
from datetime import datetime
import json


class Calendar:
    """class for performing adding and substracting with dates, as well as their comparison"""
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

    @staticmethod
    def round_date_after_add(day, month, year):
        with open("months.json") as f:
            months_dict = json.load(f)
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
        return day, month, year

    @staticmethod
    def round_date_after_sub(day, month, year):
        with open("months.json") as f:
            months_dict = json.load(f)
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
        return day, month, year

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


    def __iadd__(self, other):
        """overloading the add operator to add dates"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        self.year += other.year
        self.month +=  other.month
        self.day += other.day
        self.day, self.month, self.year = self.round_date_after_add(self.day, self.month, self.year)
        return self

    def __isub__(self, other):
        """overloading the add operator to substract dates"""
        if not isinstance(other, Calendar):
            raise TypeError("It should be Calendar object!")
        self.year -= other.year
        self.month -=  other.month
        self.day -= other.day
        self.day, self.month, self.year = self.round_date_after_sub(self.day, self.month, self.year)
        return self

    def __str__(self):
        return f'\nCurrent date:\nYear: {self.year}\nMonth: {self.month}\nDay: {self.day}\n'


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
# print(f'{date1 + date3}')
date2 -= date1
print(f'{date2}')
date1 += date3
print(f'{date1}')
