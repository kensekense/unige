#Ning
#30 September 2019
#metaheuristics TP2

'''
TODO: sidenote! the matrix for holding the solution (ie: like the file 1.dat) starts at location 1, so for
our array organization, we should probably hold 0-indexes to be empty (None-type), and just keep consistency
with 1-indexes in order to not get confused in calculations.
'''

import random

class QuadraticAssignment:

    def __init__ (self, N):
        '''
        Initial assignment randomly generates a solution matrix D and W, where D is the distance matrix
        and W is the weight matrix, and N is the number of locations (and facilities).
        '''
        #generate initial solution
        #create empty tabu list (tabu list should be a matrix of NxN, initialized with 0s)

    def generate_neighbor(self):
        '''
        defining neighborhood placeholder.
        '''
        #neighborhood is given by the classical 2-exchange which amounts to swapping two locations
        #

    def tabu_search(self):
        '''
        tabu search algorithm placeholder.
        '''
        #choose the best non-tabu neighbor
        #update the best solution seen so far
        #check whether end condition is met
        #update tabu list with movement x0 -> x1 or generate_neighbor



if __name__ == "__main__":
    return 0
