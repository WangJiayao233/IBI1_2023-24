import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
# Pseudocode:
# this code is used to show the average time spent on different activities in a day, besed on the data given by the professor if IBI1.
# introduce the data given
# define variables used for input,then use these variables to create a dictionary
# set up 6 categories and show the time of these activities in a day.
Sleeping=8
Classes=6
Studying=3.5
Tv=2
Music=1
others=24-Sleeping-Classes-Studying-Tv-Music
#generate a dict, 'type1': data1, 'type2': data2,......
dict_activities = {'Sleeping': Sleeping,'Classes':Classes,'Studying': Studying,'TV': Tv,'Music': Music,'others': others}
print(dict_activities)
list(dict_activities.values())

lables = ["Sleeping", "Classes", "Studying", "TV", "Music","others"]

time_an_average_day = [Sleeping, Classes, Studying, Tv, Music,others]
#generate a pie chart, lead the lables and the data to the plt.pie, use autopct to show the percentage
#So, lables = lables(the list I created), and autopct='%1.1f%%', autopct is used to show the percentage, and to control the decimal parts.
plt.figure()
plt.pie(time_an_average_day, labels=lables,autopct='%1.1f%%' )

plt.show()

plt.clf()
#print the mean of the data
print(stat.mean(list(dict_activities.values())))
