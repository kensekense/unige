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
        #TODO: scrambling the array brings up the issue with the connections, since every point is connected to every other point
        #how can we know the distances without drawing the entire graph?
        #because swapping two placements affects some connections, and not others
        #maybe we can think about it as "placing" the distances between points
        #if we're "placing" distances, then how do we get a preliminary distance chart? (this is the triangle)
        #so we can store all the values in the triangle
        #triangle is 2x for loop i,j with j = i+1
        self.triangle = [] #for reference there should be (n+1)*n/2 values in triangle
        for i in range(0, self.N):
            for j in range(i+1, self.N):
                self.triangle.append(self.D[i][j])
        #this is fine because when we change connections, we can just change values according to rows and columns
        #the ones that don't change will not be affected, as long as we originally scramble by placing distances
        #we should be fine


        #create empty tabu list (tabu list should be a matrix of NxN, initialized with 0s)
        #note that tabu list has a short and long term memory mechanism that we should separate

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

    a = QuadraticAssignment("1.dat")
    #print("{0} \n {1} \n {2}".format(a.N,a.D,a.W))
    print("{0} \n {1}".format(a.triangle,len(a.triangle)))
