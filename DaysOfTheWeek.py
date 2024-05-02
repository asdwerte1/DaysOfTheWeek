class WeekDayError(Exception):
    pass
	

class Weeker:

    def __init__(self, day):
        self.__days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        if day not in self.__days: raise WeekDayError
        else: self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        day_diff = n % 7 # Number of days to add
        current_day = self.__days.index(self.__day)
        new_day = day_diff + current_day
        if new_day >= 7: new_day -= 7 # Remove overflow - sets index of day of week
        self.__day = self.__days[new_day]

    def subtract_days(self, n):
        day_diff = n % 7 # Number of days to remove
        current_day = self.__days.index(self.__day)
        new_day = current_day - day_diff
        if new_day < 0: new_day = 7 - abs(new_day) # Remove overflow - sets index of day of week
        self.__day = self.__days[new_day]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
