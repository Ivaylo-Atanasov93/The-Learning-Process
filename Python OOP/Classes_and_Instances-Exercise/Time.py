from _datetime import datetime,timedelta


class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.current_time = datetime(100, 1, 1, hours, minutes, seconds)

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.current_time = datetime(100, 1, 1, hour=hours, minute=minutes, second=seconds)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        self.current_time += timedelta(seconds=1)
        self.hours = self.current_time.hour
        self.minutes = self.current_time.minute
        self.seconds = self.current_time.second
        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

