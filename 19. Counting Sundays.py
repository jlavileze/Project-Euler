import datetime as dt

total = 0

d = dt.date(1901,1,1)
delta = dt.timedelta(days=1)
while d <= dt.date(2000,12,31):
    if d.weekday() == 6 and d.day == 1:
        total += 1
    d += delta
    
print total