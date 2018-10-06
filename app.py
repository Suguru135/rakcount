#!/usr/bin/python3

from urllib.request import urlopen
import linecache
import re
from datetime import datetime
import csv

html = urlopen('http://rakuen.jeison.biz/bbs/?mode=list')
source = html.read()

with open('/home/pi/pg/python/rakcount/log/cache', 'w') as f:
    f.write(source.decode('utf-8'))

line = linecache.getline('/home/pi/pg/python/rakcount/log/cache', 75)
linecache.clearcache()

now = datetime.now()
pattern = '今日：([0-9]{4})' if now.hour != 0 else '昨日：([0-9]{4})'

r = re.compile(pattern)
m = r.search(line)

# data準備
data = [int(m.group(1)), now]


# log書き込み
with open('/home/pi/pg/python/rakcount/log/log', 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(data)


