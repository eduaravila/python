import datetime

t = datetime.time(4, 29, 1)

print(t)
print(t)
print("hour", t.hour)
print("minute", t.minute)
print("second", t.second)
print("microsecond", t.microsecond)
print("tzinfo", t.tzinfo)

print("Earliest:", datetime.time.min)
print("Lastest:", datetime.time.max)
print("Resolution:", datetime.time.resolution)

today = datetime.date.today()
print(today)
print("ctime", today.ctime())
print("tuple", today.timetuple())
print("ordinal", today.toordinal())
print("year", today.year)
print("month", today.month)
print("day", today.day)

print("max date", datetime.date.max)
print("min date", datetime.date.min)
print("resolution date", datetime.date.resolution)

print("changing the year")
today2 = today.replace(year=1998)
print(today2)

d1 = datetime.date(2015, 4, 29)
d2 = datetime.date(2000, 4, 29)

print(d1-d2)

print(datetime.timedelta())