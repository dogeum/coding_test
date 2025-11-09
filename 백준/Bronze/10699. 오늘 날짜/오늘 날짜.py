import datetime

utc = datetime.datetime.now(datetime.timezone.utc)

seoul = utc + datetime.timedelta(hours=9)
print(seoul.strftime("%Y-%m-%d"))