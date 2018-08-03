#!/usr/bin/env python
#lake_height_vs_time.py
#plot symbols versus time
#time range seems to be set automatically

#manual data only

#input file camera observations
#header line
#2013-12-12T22:40:02Z,147,38.6,31.6,0.0,-22.23,0.25
#2013-12-20T00:00:02Z,147,38.6,31.6,0.0,-22.23,0.25

#input file rangefinder observations
#header line
#05/02/2014,30.4,-21,0.25
#04/04/2014,28.9,-19.5,0.25

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import sys
from matplotlib.dates import DAILY #fix for AutoDateLocator bug

#input arguments
if (len(sys.argv) != 4):
  sys.exit("syntax lake_height_vs_time_basic.py camera_manual_csv_file rangefinder_manual_csv_file plotfile")
else:
  cameracsvfile = sys.argv[1]
  rangecsvfile = sys.argv[2]
  plotfile = sys.argv[3]

#camera
names = ['date', 'measurepx', 'slope', 'vertical', 'delta', 'camera', 'error']

#read data
file = open(cameracsvfile)
df = pd.read_csv(file, skiprows=1, names=names, parse_dates={"Datetime" : ['date']})

fig = plt.figure(figsize=(15, 5))
plt.ylabel('Height below rim (m)')
now = dt.datetime.now()	#for plot label
#lasttim = df.last_valid_index()
lasttim = df.tail(1)['Datetime']
strlasttim = lasttim.apply(str)
lastval = float(df.tail(1)['camera'])
strlast = "%.1f" % lastval
#title = 'White Island Lake Below Overflow (in UT), last value of ' + strlast + ' at ' + lasttim.strftime("%Y-%m-%d") + ', plotted at: ' + now.strftime("%Y-%m-%d %H:%M")
#title = 'White Island Lake Below Overflow (in UT), last value of ' + strlast + ' at ' + strlasttim + ', plotted at: ' + now.strftime("%Y-%m-%d %H:%M")
#plt.title(title)

#plot symbols
plt.plot(df['Datetime'], df['camera'], marker='^', color='blue', linestyle='None', label='Image')

#rangefinder
names = ['date', 'obs', 'range', 'error']
file = open(rangecsvfile)
df2 = pd.read_csv(file, skiprows=1, names=names, parse_dates={"Datetime" : ['date']})
plt.plot(df2['Datetime'], df2['range'], marker='o', color='red', linestyle='None', label='Manual')

#legend
plt.legend(loc='upper left')

plt.savefig(plotfile, dpi=200)

