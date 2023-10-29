from datetime import date, datetime, timedelta

#1
d = datetime.today() - timedelta(days=5)
print(d)

#2
yesterday= datetime.today()- timedelta(days=1)
print(yesterday)
today=datetime.today()
print(today)
tomorrow=datetime.today()+ timedelta(days=1)
print(tomorrow)

#3
now = datetime.today()
print (now.replace(microsecond=0))

#4
date1=date(2023,12,12)
date2=date(2023,12,20)
diff=date2-date1
print(diff.days*24*3600+ diff.seconds)





