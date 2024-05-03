import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') #Use TKAgg renderer to show the interactive image(dynamic image) cited from https://blog.csdn.net/leo0308/article/details/132499565?ops_request_misc=&request_id=&biz_id=102&utm_term=imshow如何做动态图&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-132499565.142^v100^pc_search_result_base2&spm=1018.2226.3001.4187

population = np.zeros((100 , 100))
outbreak = np.random.choice(range(100),2) #return an array
population[outbreak[0], outbreak[1]] = 1
plt.ion() #Turn on the interactive mode, cited from https://blog.csdn.net/leo0308/article/details/132499565?ops_request_misc=&request_id=&biz_id=102&utm_term=imshow如何做动态图&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-132499565.142^v100^pc_search_result_base2&spm=1018.2226.3001.4187
fig = plt.figure(figsize =(6 ,4), dpi=150)


beta = 0.3
gamma = 0.05
#Pseudocode:
#for i in each time point(100):
    #search for all the infected individuals(np.where())
    #for each infected individual:
        #set the x and y of 8 neighbors
        #for xNear...:
            #for yNear...:
                #if the point is not the infected point:
                    #if the neighbor is not out of the boundary:
                        #if the neighbor is susceptible:
                            #posibility: beta to turn into infected
                        #if the neighbor is infected:
                            #posibility: gamma to turn into recovered
                        #if the neighbor is recovered:
                            #continue
                #if the neighbor is the infected individual:
                    #recover the infected individual with probability gamma
    #draw the imshow graph at each time point
    #do something to make a dynamic graph
N = 10000
TIME = 100
#0-Susceptible, 1-Infected, 2-Recovered

for j in range(TIME):
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNear in range(x-1,x+2):
            for yNear in range(y-1,y+2):
                if (xNear,yNear) != (x,y):
                    if xNear != -1 and yNear != -1 and xNear!=100 and yNear!=100:
                        if population[xNear,yNear]==0:
                            population[xNear,yNear]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                        if population[xNear,yNear]==1:
                            population[xNear,yNear]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
                        if population[xNear,yNear]==2:
                            population[xNear,yNear]=2
                if (xNear,yNear)==(x,y):
                    population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]              
    plt.imshow(population, cmap='viridis', interpolation='nearest')

    fig.canvas.flush_events() 
    plt.draw() #Line 57-58 was cited from https://blog.csdn.net/leo0308/article/details/132499565?ops_request_misc=&request_id=&biz_id=102&utm_term=imshow如何做动态图&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-132499565.142^v100^pc_search_result_base2&spm=1018.2226.3001.4187
plt.pause(0) #Avoid closing the graph automatically, cited from https://blog.csdn.net/oMoDao1/article/details/81222465?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171378636816800222895472%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=171378636816800222895472&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-81222465-null-null.142^v100^pc_search_result_base2&utm_term=TKAgg显示图片如何不自动关闭&spm=1018.2226.3001.4187
plt.clf()