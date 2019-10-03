#Ning
#30 September 2019
#metaheuristics TP2

'''
TODO: sidenote! the matrix for holding the solution (ie: like the file 1.dat) starts at location 1, so for
our array organization, we should probably hold 0-indexes to be empty (None-type), and just keep consistency
with 1-indexes in order to not get confused in calculations.
'''

import random
import numpy as np
import math

class QuadraticAssignment:

    def __init__ (self, N, D, W):
        '''
        Initial assignment randomly generates a solution matrix D and W, where D is the distance matrix
        and W is the weight matrix, and N is the number of locations (and facilities).
        '''
        self.N = N
        self.D = D
        self.W = W
        #generate initial solution #TODO: this is not trivial, since you have to scramble an array
        #we would have to scramble the array using temporary values and make sure we don't mess up the symmetry
        #maybe we can find a way to scramble it on one diagonal and match the symmetry after?
        #so we can technically read in only the diagonal, make the rest 0s, then scramble the values, and make
        #it symmetric using np.maximum(a, a.transpose()) because that takes the higher values (our values >0)
        #to do a triangle array, we do a[i][j] and 2x for loop i, j, with j = i + 1

        #create empty tabu list (tabu list should be a matrix of NxN, initialized with 0s)
        #note that tabu list has a short and long term memory mechanism that we should separate

    def generate_neighbor(self):
        '''
        defining neighborhood placeholder.
        '''
        #neighborhood is given by the classical 2-exchange which amounts to swapping two locations
        #the formula given is better understood as, partial = 2*np.sum((w[i][j] - w[p][q])*(d1[i][j]-d2[i][j]))

    def tabu_search(self):
        '''
        tabu search algorithm placeholder.
        '''
        #choose the best non-tabu neighbor
        #update the best solution seen so far
        #check whether end condition is met
        #update tabu list with movement x0 -> x1 or generate_neighbor



if __name__ == "__main__":

    #read the .dat file here and fill the arrays

    return 0
