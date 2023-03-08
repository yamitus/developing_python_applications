class Clock:
    def __init__(self):
        self.hours = int(input("Please set the hours: "))
        self.minutes = int(input("Please set the minutes: "))

    def set_hours(self, hours):
        self.hours = hours
    
    def set_minutes(self, minutes):
        self.minutes = minutes

    def ticking(self):
        print("Tik, tok")

    def get_hours(self):
        return self.hours
    
    def get_minutes(self):
        return self.minutes
    
class AlarmClock(Clock):
    def __init__(self):
        super().__init__()
    
    def set_alarm(self, alarm_time):
        self.alarm_time = alarm_time

    def ring_alarm(self):
        print("Ring, ring!")

def main():
    p = AlarmClock()
    p.ticking()
    p.set_alarm("1:14")
    p.ring_alarm()

main()