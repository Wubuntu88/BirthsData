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
weekdays_births_list = []
sat_births_list = []  # Saturday
sun_births_list = []  # Sunday
f = open("births.txt")
f.readline()  # removes header

for line in f:
    components = line.split()
    dayNumber = int(components[0])
    days.append(daysOfWeek[(dayNumber - 1) % 7])
    numberOfBirths = components[2]
    if days[-1] in daysOfWeek[1:6]:
        weekdays_births_list.append(int(numberOfBirths))
    else:
        weekdays_births_list.append(np.nan)
    if days[-1] is daysOfWeek[6]:
        sat_births_list.append(int(numberOfBirths))
    else:
        sat_births_list.append(np.nan)
    if days[-1] is daysOfWeek[0]:
        sun_births_list.append(int(numberOfBirths))
    else:
        sun_births_list.append(np.nan)

weekdays_birthsNDArray = np.array(weekdays_births_list)
sat_birthsNDArray = np.array(sat_births_list)
sun_birthsNDArray = np.array(sun_births_list)

weekdays_dict = {'Births': weekdays_birthsNDArray, 'Days': days}  # type: DateTimeIndex
sat_dict = {'Births': sat_birthsNDArray, 'Days': days}
sun_dict = {'Births': sun_birthsNDArray, 'Days': days}

myIndex = pd.date_range('01/01/1978', periods=365)

weekdays_df = pd.DataFrame(weekdays_dict, index=myIndex)
sat_df = pd.DataFrame(sat_dict, index=myIndex)
sun_df = pd.DataFrame(sun_dict, index=myIndex)

series_weekdays_without_NAN = weekdays_df["Births"].dropna()
df_weekdays_without_NAN = pd.DataFrame(series_weekdays_without_NAN, index=series_weekdays_without_NAN.index)

df_weekdays_without_NAN.to_csv("births.csv", sep="\t")

'''
#file_to_write = open("weekday_births")
for index, row in df_weedays_without_NAN.iterrows():
    print(str(index) + "\t" + str(row))
    #file_to_write.write("")
'''

plt.scatter(weekdays_df.index, weekdays_df["Births"], c="Red", s=100, label='weekdays')
plt.scatter(sat_df.index, sat_df["Births"], c="Blue", s=100l, label='Saturday')
plt.scatter(sun_df.index, sun_df["Births"], c="Green", s=100, label='Sunday')

legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.xlabel("Day of the year in 1978", fontsize=50)
plt.ylabel("Number of Births", fontsize=50)

plt.show()

f.close()