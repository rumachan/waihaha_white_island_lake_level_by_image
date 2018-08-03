#!/usr/bin/env python
#lake_height_vs_time.py
#plot symbols versus time
#time range seems to be set automatically

#manual data only

#input file
#header line
#12/12/2013,147,38.6,31.6,0.0,,,-22.2310638298
#20/12/2013,147,38.6,31.6,0.0,,,-22.2310638298
#26/12/2013,145,38.0,31.2,0.4,,,-21.8007092199
#05/02/2014,,,,,30.4,-21,

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import sys
from matplotlib.dates import DAILY #fix for AutoDateLocator bug

def date_parser(x):
    return dt.datetime.strptime(x, '%d/%m/%Y')

#input arguments
if (len(sys.argv) != 3):
  sys.exit("syntax lake_height_vs_time_basic.py manual_csv_file plotfile")
else:
  csvfile = sys.argv[1]
  plotfile = sys.argv[2]

names = ['date', 'measurepx', 'slope', 'vertical', 'delta', 'manual', 'manual-overflow', 'image-overflow']

#read data
file = open(csvfile)
df = pd.read_csv(file, skiprows=1, names=names, parse_dates=[0], date_parser=date_parser, index_col=['date'])

fig = plt.figure(figsize=(15, 5))
plt.ylabel('Height below rim (m)')
now = dt.datetime.now()	#for plot label
lasttim = df.last_valid_index()
lastval = float(df.tail(1)['image-overflow'])
strlast = "%.1f" % lastval
title = 'White Island Lake Below Overflow (in UT), last value of ' + strlast + ' at ' + lasttim.strftime("%Y-%m-%d") + ', plotted at: ' + now.strftime("%Y-%m-%d %H:%M")
plt.title(title)

#plot symbols
plt.plot(df.index, df['image-overflow'], marker='^', color='blue', linestyle='None', label='Image')
plt.plot(df.index, df['manual-overflow'], marker='o', color='red', linestyle='None', label='Manual')

#legend
plt.legend(loc='upper left')

plt.savefig(plotfile, dpi=200)
