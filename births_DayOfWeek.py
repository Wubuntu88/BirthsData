#!/usr/bin/env python
__author__ = 'will'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#0 is the day number
#2 is the number of births
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days = []

births_list_by_day_of_the_week = []
for day in daysOfWeek:
    births_list_by_day_of_the_week.append([])

#weekdays_births_list = []
#sat_births_list = []  # Saturday
#sun_births_list = []  # Sunday
f = open("births.txt")
f.readline()  # removes header

for line in f:
    components = line.split()
    dayNumber = int(components[0])
    days.append(daysOfWeek[(dayNumber - 1) % 7])
    numberOfBirths = components[2]
    for dayOfWeekIndex in range(len(daysOfWeek)):
        if days[-1] is daysOfWeek[dayOfWeekIndex]:
            births_list_by_day_of_the_week[dayOfWeekIndex].append(int(numberOfBirths))
        else:
            births_list_by_day_of_the_week[dayOfWeekIndex].append(np.nan)
'''
weekdays_birthsNDArray = np.array(weekdays_births_list)
sat_birthsNDArray = np.array(sat_births_list)
sun_birthsNDArray = np.array(sun_births_list)
'''

daysOfWeekListOfDictionaries = []
for counter in range(len(births_list_by_day_of_the_week)):
    daysOfWeekListOfDictionaries.append({'Births': births_list_by_day_of_the_week[counter]})

'''
weekdays_dict = {'Births': weekdays_birthsNDArray, 'Days': days}  # type: DateTimeIndex
sat_dict = {'Births': sat_birthsNDArray, 'Days': days}
sun_dict = {'Births': sun_birthsNDArray, 'Days': days}
'''


myIndex = pd.date_range('01/01/1978', periods=365)

daysOfWeekDataFrames = []
for counter in range(len(daysOfWeekListOfDictionaries)):
    df = pd.DataFrame(daysOfWeekListOfDictionaries[counter], index=myIndex)
    daysOfWeekDataFrames.append(df)

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
i = 0
for dayOfWeekDataFrame in daysOfWeekDataFrames:
    plt.scatter(dayOfWeekDataFrame.index, dayOfWeekDataFrame["Births"], c=colors[i], s=100,label=[daysOfWeek[i]])
    i += 1


legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.xlabel("Day of the year in 1978", fontsize=50)
plt.ylabel("Number of Births", fontsize=50)

plt.show()

f.close()