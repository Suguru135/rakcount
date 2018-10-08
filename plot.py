#!/usr/bin/python3
from datetime import datetime
from datetime import timedelta

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import csv

def plot():
    now = datetime.now() - timedelta(days=1)

    log = get_log(now)
    generate_bar(log, now)



def generate_bar(array, now):
    # arrayについて整理
    length = len(array)
    nums = list(range(length))
    
    # pltの諸設定
    left = np.array(nums)
    height = np.array(array)

    plt.bar(left, height, width=1.0, color="#EEFFFF", edgecolor="#00AAEE")
    plt.savefig('/home/pi/pg/python/rakcount/images/{0:%Y%m%d}.png'.format(now))
    

def get_log(now):
    array = []

    before = 0
    with open('/home/pi/pg/python/rakcount/log/{0:%Y%m%d}.log'.format(now), newline='') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            num = int(row[0])
            if i == 0:
                array.append(num)
                before = num
            else:
                array.append(num - before)
                before = num

    return array


if __name__ == "__main__":
    
    plot()
