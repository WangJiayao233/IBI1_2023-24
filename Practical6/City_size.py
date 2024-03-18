import numpy as np
import matplotlib.pyplot as plt
#Create two lists, storing the data
#then sort them and print them
#Create lists to store the names of cities in the UK and China to match the new order of data
#Then use plt to create bar charts(plt.bar)
#Finally, use plt.show to show the charts.
#Don't forget to use plt.clf to clear the charts.
uk_cities = [0.56,0.62,0.04,9.7]
china_cities = [0.58,8.4,29.9,22.2]

uk_cities.sort()
print(uk_cities)
china_cities.sort()
print(china_cities)

UK_list = ["Stirling","Edinburgh","Glasgow","London"]
CN_list = ["Haining","Hangzhou","Beijing","Shanghai"]

plt.bar(UK_list,uk_cities,color=['r','b','y','g'],width=0.5,hatch='/') #Adjust the properties of the chart.
plt.title("Distribution of city sizes in the UK")
plt.ylabel("Population(millions)")
plt.xlabel("Cities in UK")
plt.show()
plt.clf()

plt.bar(CN_list,china_cities,color=['r','b','y','g'],width=0.5,hatch='\\') #Adjust the properties of the chart.
plt.title("Distribution of city sizes in the China")
plt.ylabel("Population(millions)")
plt.xlabel("Cities in China")
plt.show()
plt.clf()