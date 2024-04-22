import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000

beta = 0.3     #beta is the infection probability for each susceptible individual(not considered the probability of the contact between susceptible and infected individual)
gamma = 0.05  #gamma is the recovery probability for each infected individual
plt.figure (figsize =(6,4), dpi=150)
plt.title("SIR model with different vaccination rates")
plt.xlabel("time")
plt.ylabel("number of people")

for k in [x * 0.1 for x in range(0, 11)]:  #k is the vaccination probability for each susceptible individual
    #0-Susceptible, 1-Infected, 2-Recovered, 3-Vaccinated
    sus = 0
    sus_array = []
    inf = 1
    inf_array = []
    rec = 2
    rec_array = []
    vac = 3
    vac_array = []
    if k != 1.0:
        wholelist = np.random.choice(range(4),N,p=[0.9999-k,0.0001,0,k])
    else:
        wholelist = np.random.choice(range(4),N,p=[0,0,0,1.0])
    
    for i in range(N):
        if wholelist[i] == sus:
            sus_array.append(wholelist[i])
        elif wholelist[i] == inf:
            inf_array.append(wholelist[i])
        elif wholelist[i] == rec:
            rec_array.append(wholelist[i])
        elif wholelist[i] == vac:
            vac_array.append(wholelist[i])
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
    
    x = [i for i in range(TIME)]
    m = [i for i in num_inf]
    k1 = round(k,1)
    if k1 == 0.0:
        plt.plot(x,m,label='0')
    else:
        plt.plot(x,m,label=str(int(round(k1*100,2)))+'%')
    plt.legend()

plt.show()
plt.clf()

#check: two runs of the model gave the different results of the number of individuals, which proves the randomness of the model

#The herd immunity threshold may be around 60-70% in this model.