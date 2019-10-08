#Ning
#30 September 2019
#metaheuristics TP2

import random
import numpy as np
import math

class QuadraticAssignment:

    def __init__ (self, data):
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

    def generate_neighbor(self):
        '''
        defining neighborhood placeholder.
        '''
        #neighborhood is given by the classical 2-exchange which amounts to swapping two locations
        #the formula given is better understood as, partial = 2*np.sum((w[i][j] - w[p][q])*(d1[i][j]-d2[i][j]))
        pass

    def tabu_search(self):
        '''
        tabu search algorithm placeholder.
        '''
        #choose the best non-tabu neighbor
        #update the best solution seen so far
        #check whether end condition is met
        #update tabu list with movement x0 -> x1 or generate_neighbor
        pass


if __name__ == "__main__":

    #read the .dat file here and fill the arrays
    #default = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11)]
    #test1 = [(0,1),(1,0),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11)]
    a = QuadraticAssignment("1.dat")
    #print("{0} \n {1} \n {2}".format(a.N,a.D,a.W))
    #print(a.placement)
    #print(a.tabu_list)
    #print(a.calculate_fitness(a.N, a.D, a.W, a.placement))
    #print(a.calculate_fitness(a.N, a.D, a.W, default))
    #print(a.calculate_fitness(a.N, a.D, a.W, test1))
    #print(a.partial_sum(a.N, a.D, a.W, [(0,0), (1,1)]))
