# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:55:04 2020

@author: Ayush
"""

import datetime 
import calendar 
  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    return (calendar.day_name[born]) 

#   test 1
#d = {'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
#   test 2
d = {'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}
r = list(d.keys())
D = {'Mon':None,'Tue':None,'Wed':None,'Thu':None,'Fri':None,'Sat':None,'Sun':None}

for i in range(0,len(r)):
    c = r[i]
    date = findDay(c)
    val = d[c]
    if(D[date[:3]] == None):
        D[date[:3]] = val
    else:
        D[date[:3]] = int(D[date[:3]]) + val
 
prev1=D['Sat']
prev2=D['Mon']

for key in D:
    if(key == 'Mon'):
        continue
    
    if(D[key] == None):
        D[key] = (2*prev2) - prev1
    
    prev1 = prev2
    prev2 = D[key]

print(D)