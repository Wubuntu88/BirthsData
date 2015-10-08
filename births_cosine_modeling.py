#!/usr/bin/env python
__author__ = 'will'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq



#0 is the day number
#2 is the number of births
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days = []

births_list_by_day_of_the_week = []
for day in daysOfWeek:
    births_list_by_day_of_the_week.append([])


f = open("births.txt")
f.readline()  # removes header

"""This is for cosine modeling"""
days_of_sunday = range(1, 365, 7)
y_values_for_cos_model_for_sunday = []
'''end of cos modeling'''

for line in f:
    components = line.split()
    dayNumber = int(components[0])
    days.append(daysOfWeek[(dayNumber - 1) % 7])
    numberOfBirths = int(components[2])
    if dayNumber in days_of_sunday:  # <--- for cosine modeling
        y_values_for_cos_model_for_sunday.append(np.float(numberOfBirths))
    for dayOfWeekIndex in range(len(daysOfWeek)):
        if days[-1] is daysOfWeek[dayOfWeekIndex]:
            births_list_by_day_of_the_week[dayOfWeekIndex].append(numberOfBirths)
        else:
            births_list_by_day_of_the_week[dayOfWeekIndex].append(np.nan)

daysOfWeekListOfDictionaries = []
for counter in range(len(births_list_by_day_of_the_week)):
    daysOfWeekListOfDictionaries.append({'Births': births_list_by_day_of_the_week[counter]})


print days_of_sunday
print y_values_for_cos_model_for_sunday
'''cos modeling'''
y_values_for_cos_model_for_sunday = np.array(y_values_for_cos_model_for_sunday)
#print type(days_of_sunday[0])
#print type(y_values_for_cos_model_for_sunday[0])
sin_fit = lambda p: p[0]*np.sin(days_of_sunday+p[1]) + p[2] - y_values_for_cos_model_for_sunday

est_std, est_phase, est_mean = leastsq(sin_fit, [1, 1, 1])[0]
y_fit = est_std * np.sin(days_of_sunday + est_phase) + est_mean

plt.plot(days_of_sunday, y_fit, c="burlywood")
'''end of cos modeling'''

daysOfWeekDataFrames = []
for counter in range(len(daysOfWeekListOfDictionaries)):
    df = pd.DataFrame(daysOfWeekListOfDictionaries[counter], index=range(365))
    daysOfWeekDataFrames.append(df)

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
i = 0
for dayOfWeekDataFrame in daysOfWeekDataFrames:
    plt.scatter(dayOfWeekDataFrame.index, dayOfWeekDataFrame["Births"], c=colors[i], s=100, label=[daysOfWeek[i]])
    i += 1




legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.xlabel("Day of the year in 1978", fontsize=50)
plt.ylabel("Number of Births", fontsize=50)

plt.show()

f.close()