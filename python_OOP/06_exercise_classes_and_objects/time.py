class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours, new_minutes, new_seconds):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    # def next_second(self):
    #     total_time_in_seconds = (self.hours * 3600) + (self.minutes * 60) + self.seconds + 1
    #     self.hours = total_time_in_seconds // 3600
    #     if self.hours > Time.max_hours:
    #         self.hours = 0
    #     total_time_in_seconds %= 3600
    #     self.minutes = total_time_in_seconds // 60
    #     total_time_in_seconds %= 60
    #     self.seconds = total_time_in_seconds
    #     return self.get_time()
    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 0
        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())





