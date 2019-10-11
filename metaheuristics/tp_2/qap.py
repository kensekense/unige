#Ning
#30 September 2019
#metaheuristics TP2

import random
import numpy as np
import math
import sys

sys.setrecursionlimit(20000) #WARNING: python recursion issue

class QuadraticAssignment:

    def __init__ (self, data, stop_condo):
        '''
        Initial assignment randomly generates a solution matrix D and W, where D is the distance matrix
        and W is the weight matrix, and N is the number of locations (and facilities).
        '''
        self.document = []
        with open(data) as pfile: #open file, read lines, store
            for line in pfile:
                if(len(line.split())>0): #if it's not an empty line
                    self.document.append(line.split()) #store the values

        for i in range(0,len(self.document)): #integer the strings
            self.document[i] = [int(x) for x in self.document[i]]

        self.N = self.document[0][0] #the first line should be the size N
        self.D = np.array(self.document[1:self.N+1]) #the first N lines after 'N' should be D
        self.W = np.array(self.document[self.N+1:]) #the rest should be W

        #generate initial solution
        self.placement = [None]*self.N
        for i in range(0, self.N):
            self.placement[i] = i
        random.shuffle(self.placement) #random initial state
        for i in range(0, self.N):
            self.placement[i] = (i, self.placement[i]) #put it in (location, facility) forme.

        #create empty tabu list (tabu list should be a matrix of NxN, initialized with 0s)
        self.iteration = 0
        self.tabu_list = np.zeros((self.N, self.N))
        #note that tabu list has a short and long term memory mechanism that we should separate

        #need a stop condition on iterations
        self.tmax = stop_condo

    def calculate_fitness(self, N, D, W, configuration):
        sum = 0
        #triangle is 2x for loop i,j with j = i+1
        for i in range(0, N):
            for j in range(i+1, N):
                sum += W[configuration[i][1]][configuration[j][1]]*D[configuration[i][0]][configuration[j][0]]
        return sum*2

    def partial_sum(self, N, D, W, swap):
        partial = 0
        for k in range(0,N):
            if(k!=swap[0][0] and k!=swap[1][0]):
                partial += (W[swap[1][1]][k]-W[swap[0][1]][k])*(D[swap[0][0]][k]-D[swap[1][0]][k])

        return partial  * 2

    def add_to_tabu(self, N, iter, tenure, taboo, swap):
        t = tenure*N #taboo tenure l, defined by the notes
        if (tenure==1):
            t = 1
        #edit the taboo value
        tab = t + random.randint(0,N)
        taboo[swap[0][0]][swap[0][1]] = tab  #loc 0 -> fac 0
        taboo[swap[1][0]][swap[1][1]] = tab #loc 1 -> fac 1
        taboo[swap[0][0]][swap[1][1]] = tab #loc 0 -> fac 1
        taboo[swap[1][0]][swap[0][1]] = tab #loc 1 -> fac 0

        return taboo

    def suitable_selection(self, N, D, W, configuration):
        for i in range(random.randint(0,len(configuration)-1),len(configuration)):
            for j in range(0, len(configuration)):
                pot_swap = [(configuration[i][0],configuration[i][1]),(configuration[j][0],configuration[j][1])]
                advantage = self.partial_sum(N,D,W,pot_swap)
                if advantage < 0:
                    return pot_swap

    def tabu_search(self, N, D, W, iter, tenure, taboo, configuration):
        '''
        tabu search algorithm placeholder.
        '''
        advantage = 0

        '''while(advantage >= best): #need to find a good roll
            roll1 = 0
            roll2 = 0
            while(roll1 == roll2):
                roll1 = random.randint(0,len(configuration)-1) #each time makes two rolls
                roll2 = random.randint(0,len(configuration)-1)

            #randomly choose a potential swap
            pot_swap = [(configuration[roll1][0],configuration[roll1][1]),(configuration[roll2][0],configuration[roll2][1])]
            #calculate the advantage we get from this swap
            advantage = self.partial_sum(N,D,W,pot_swap)'''
        pot_swap = self.suitable_selection(N,D,W, configuration)

        #choose the best non-tabu neighbor, first run is okay
        if(iter == 0 or (taboo[pot_swap[0][0]][pot_swap[1][1]] != taboo[pot_swap[1][0]][pot_swap[0][1]])): #if a valid placement
            if(iter == 0 or (iter > taboo[pot_swap[0][0]][pot_swap[1][1]] and iter > taboo[pot_swap[1][0]][pot_swap[0][1]])): #from loc 0-> fac 1, and loc 1-> fac 0
                #swap is accepted
                taboo = self.add_to_tabu(N, iter, tenure, taboo, pot_swap) #adjust tabu list

                #swaps fac from roll1 with fac from roll2 while maintaining respective loc in config
                (tloc_a, tfac_a) = configuration[pot_swap[0][0]]
                (tloc_b, tfac_b) = configuration[pot_swap[1][0]]
                configuration[pot_swap[0][0]] = (tloc_a, tfac_b)
                configuration[pot_swap[1][0]] = (tloc_b, tfac_a)


        #check whether end condition is met
        if(iter > self.tmax):
            return configuration

        return self.tabu_search(N, D, W, iter+1, tenure, taboo, configuration)

if __name__ == "__main__":

    #read the .dat file here and fill the arrays
    default = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11)]
    #test1 = [(0,1),(1,0),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11)]
    a = QuadraticAssignment("1.dat", 15000) #core dumps after 15000 bc python
    #print("{0} \n {1} \n {2}".format(a.N,a.D,a.W))
    #print(a.placement)
    #print(a.tabu_list)
    #print(a.calculate_fitness(a.N, a.D, a.W, a.placement))
    #print(a.calculate_fitness(a.N, a.D, a.W, default))
    #print(a.calculate_fitness(a.N, a.D, a.W, test1))
    #print(a.partial_sum(a.N, a.D, a.W, [(0,0), (1,1)]))
    print(a.placement, a.calculate_fitness(a.N, a.D, a.W, a.placement))
    #print(default, a.calculate_fitness(a.N, a.D, a.W, default))
    result = a.tabu_search(a.N, a.D, a.W, a.iteration, 1, a.tabu_list, a.placement)
    #result = a.tabu_search(a.N, a.D, a.W, a.iteration, 0.5, a.tabu_list, default)
    print(result, a.calculate_fitness(a.N, a.D, a.W, result))
