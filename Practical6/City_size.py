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

#Set the size of the window.
plt.figure(figsize=(10,6))
#use plt.subplot to create two charts in the same time
plt.subplot(1,2,1)
plt.bar(UK_list,uk_cities,color=['b'],width=0.5,hatch='\\') #Adjust the properties of the chart.
#This code of line 26 & 27 was obtained from https://www.csdn.net
for a,b,i in zip(UK_list,uk_cities,range(len(UK_list))): # zip function
    plt.text(a,b+0.03,"%.2f"%uk_cities[i],ha='center',fontsize=10) # plt.text function
#set a title for the chart
plt.title("Distribution of city sizes in the UK")
#set the x and y labels
plt.ylabel("Population(millions)")
plt.xlabel("Cities in UK")

plt.subplot(1,2,2)
plt.bar(CN_list,china_cities,color=['r'],width=0.5,hatch='/') #Adjust the properties of the chart.
#This code of line 38 & 40 was obtained from https://www.csdn.net
# zip function
for a,b,i in zip(CN_list,china_cities,range(len(UK_list))): 
    # plt.text function
    plt.text(a,b+0.03,"%.2f"%china_cities[i],ha='center',fontsize=10) 
#set a title for the chart
plt.title("Distribution of city sizes in the China")
plt.ylabel("Population(millions)")
plt.xlabel("Cities in China")
#show the charts
plt.show()
#Clear the charts
plt.clf()