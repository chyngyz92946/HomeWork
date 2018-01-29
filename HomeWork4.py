import datetime
import time
a = datetime.date(1990, 12, 4).strftime('%Y/%m/%d')
print(a)

while True:
    print(datetime.datetime.now())
    time.sleep(1)