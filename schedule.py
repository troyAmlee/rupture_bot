# Method
# User inputs date for a pug !pugevent (year, month, day, time)
# Get difference of the current date and event date
# Set schedule delay time to difference
# When schedule reaches end time the notification function will execute


import sched
import time
import datetime
import calendar

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

localTime = time.localtime()

print(time.localtime())

currentDateYMD = datetime.date(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)
currentDateHMS = datetime.time(localTime.tm_hour, localTime.tm_min, localTime.tm_sec, 0, )
totalDate = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday,
                              localTime.tm_hour, localTime.tm_min, localTime.tm_sec)

# print(currentDateYMD)
print(currentDateHMS)
print(totalDate)

eventTime = datetime.datetime(2020, 3, 9, 9, 50)

difference = eventTime - totalDate

yearOfEvent = eventTime.year
monthOfEvent = eventTime.month
dayOfEvent = eventTime.day
hourOfEvent = eventTime.hour
minuteOfEvent = eventTime.minute

print(eventTime.ctime())

realEventTime = f"I am string"

print(difference.seconds)

# def convertTime(time):
#   #5:30pm
#   print(time)
#   hr_minPeriod = time.split(":")
#   print(hr_minPeriod)
#   minPeriod = hr_minPeriod[1]
#   for i in minPeriod:
#     if (i.isdigit() is true):


# print(convertTime("5:20pm"))

# def differenceInTime(year, month, day, time):
#   currentTime = []
#   eventTime = []
#   differenceInTime = 0
#   pass


scheduler = sched.scheduler(time.time, time.sleep)


# figure out the time delay: DELAY = current_time - time_of_event

def print_event(name):
    print('EVENT:', "SourceForts Pug", 'DATE:', eventTime.ctime(), name)


print('START:', time.time())
scheduler.enter(2, 1, print_event, ('first',))
scheduler.enter(3, 1, print_event, ('second',))

scheduler.run()
