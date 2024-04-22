import numpy as np
import matplotlib.pyplot as plt
#Pseudocode: 
#for at each time point:
    #calculate the probability of each individual to be infected at each time point
    #for each individual:
        #if the individual is susceptible:
            #generate a random number to simulate the posibility of the individual to be infected
            #if the individual will be infected at the time point:
                #remove it from susceptible
                #add it into infected 
        #if the individual is infected:
            #if the individual will be recovered at the time point:
                #remove it from infected
                #add it into recovered
    #store the number of individuals in each group at each time point(be ready to draw graph)
#Begin coding:     
N = 10000
#0-Susceptible, 1-Infected, 2-Recovered
sus = 0
sus_array = []
inf = 1
inf_array = []
rec = 2
rec_array = []

beta = 0.3     #beta is the infection probability for each susceptible individual(not considered the probability of the contact between susceptible and infected individual)
gamma = 0.05  #gamma is the recovery probability for each infected individual

wholelist = np.random.choice(range(3),N,p=[0.9999,0.0001,0])

for i in range(N):
    if wholelist[i] == sus:
        sus_array.append(wholelist[i])
    elif wholelist[i] == inf:
        inf_array.append(wholelist[i])
    else:
        rec_array.append(wholelist[i])

#set 1000 time points to check the condition of the system
TIME = 1000
num_sus = []
num_inf = []
num_rec = []
for i in range(TIME):
    #calculate the probability of each individual to be infected at each time point(considered the probability of the contact between susceptible and infected individual)
    p_infection = beta * len(inf_array)/N
    for j in range(len(wholelist)):
        if wholelist[j] == sus:
            if np.random.rand() < p_infection:
                sus_array.pop()
                inf_array.append(inf)
                wholelist[j] = inf
        elif wholelist[j] == inf:
            if np.random.rand() < gamma:
                inf_array.pop()
                rec_array.append(rec)
                wholelist[j] = rec
    #store the number of individuals in each group at each time point
    num_sus.append(len(sus_array))
    num_inf.append(len(inf_array))
    num_rec.append(len(rec_array))
    #print(len(sus_array),len(inf_array),len(rec_array))----check the random process
#begin to draw the plot
plt.figure (figsize =(6,4), dpi=150)
plt.title("SIR Model")
plt.xlabel("Time Points")
plt.ylabel("Number of Individuals")

x = [i for i in range(TIME)]
y = [i for i in num_sus]
m = [i for i in num_inf]
n = [i for i in num_rec]

plt.plot(x,y,label="Susceptible")
plt.plot(x,m,label="Infected")
plt.plot(x,n,label="Recovered")
plt.legend()

plt.show()
plt.clf()

#check: two runs of the model gave the different results of the number of individuals, which proves the randomness of the model
#But sometimes, the possible one infected people may fail to infect the susceptible people, which may make the graph two special lines