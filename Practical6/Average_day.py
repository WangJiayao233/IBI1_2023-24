import numpy as np
import matplotlib.pyplot as plt
# Pseudocode:
# introduce the data given
# define variables used for input,then use these variables to create a dictionary
Sleeping=8
Classes=6
Studying=3.5
TV=2
Music=1
others=24-Sleeping-Classes-Studying-TV-Music
#generate a dict, 'type1': data1, 'type2': data2,......
dict = {'Sleeping': Sleeping,'Classes':Classes,'Studying': Studying,'TV': TV,'Music': Music,'others': others}
print(dict)

lables = ["Sleeping", "Classes", "Studying", "TV", "Music","others"]

time_an_average_day = [Sleeping, Classes, Studying, TV, Music,others]
#generate a pie chart, lead the lables and the data to the plt.pie, use autopct to show the percentage
#So, lables = lables(the list I created), and autopct='%1.1f%%'
plt.figure()
plt.pie(time_an_average_day, labels=lables,autopct='%1.1f%%' )

plt.show()

plt.clf()