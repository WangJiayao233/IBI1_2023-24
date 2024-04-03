import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change the working directory and read the data from the file
os.chdir("/Users/wangjiayao/Desktop/Python/Notes/IBI1_2023-24/IBI1_2023-24/Practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#print the fourth column (the DALYs) from every 10th row, starting from the first row, for the first 100 rows (inclusive).(cited from the practical7 instruction)
print(dalys_data.iloc[0:101:10,3])
#use bool value to select the columns--'DALYs'
my_columns = [False, False, False, True]
#select the rows with the entity 'Afghanistan' and print out
print(dalys_data.loc[dalys_data['Entity']=='Afghanistan',my_columns])

china_data = dalys_data.loc[dalys_data['Entity']=='China',[True, False, True, True]]
meanvalue=np.mean(china_data['DALYs'])
#the mean value of DALYs in China is about 30677.6943
#the value of DALYs in China in 2019 is 22270.51, so the DALYs in China in 2019 was less than the mean.
print(meanvalue)

plt.figure(figsize=(10,6))
plt.plot(china_data.Year, china_data.DALYs, 'bo')
plt.xticks(china_data.Year,rotation=-90)
plt.xlabel("Year")
plt.ylabel("The value of DALYs in China")
plt.show()

#answer the question in question.txt
Countries_data = dalys_data.loc[dalys_data['Year']==2019,[True, False, False, True]]

plt.figure(figsize=(10,6))
countries_dalys=[Countries_data['DALYs']]
plt.boxplot(countries_dalys,labels=['Countries in 2019'],vert=True)
plt.ylabel("The value of DALYs in 2019")

plt.show()
plt.clf()