from MyModuls.moduls import *
import os
import datetime

print(kill('.', 'txttxt.txt'))
while True:
    now = datetime.datetime.now()   # показывает время
    time.sleep(1)   # задержка в 1 секунду
    print(now)