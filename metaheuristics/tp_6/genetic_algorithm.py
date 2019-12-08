#Ning Tientso
#27 Nov 2019
#Metaheuristics TP6

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import random
import math
from mpl_toolkits import mplot3d
%matplotlib inline

class Individual:

    def __init__ (self):

        self.solution = np.array([int(x) for x in format(random.getrandbits(20), "020b")])
        self.x = int("".join([str(x) for x in self.solution[0:10]]),2)
        self.y = int("".join([str(x) for x in self.solution[10:]]),2)

    def calc_fitness(self):

        #account for the mapping between solution_y, solution_y elementof [0,1024], and x,y elementof [10, 10000]
        if self.x < 10:
            self.x = self.x + 1024 #map it past 1024
        if self.y < 10:
            self.y = self.y + 1024 #map it pas 1024

        return np.subtract(np.multiply(-1, np.absolute(np.multiply(0.5, np.multiply(self.x,np.sin(np.sqrt(np.absolute(self.x))))))),np.absolute(np.multiply(self.y,np.sin(np.multiply(30,np.sqrt(np.absolute(np.divide(self.x,self.y))))))))

    def mutation(self, pm):
        '''
        With probability pm at each index, alter the value
        '''
        mutated = Individual()

        for i,bit in enumerate(self.solution):
            if random.random() < pm: #means that mutation probability is met
                if bit == 0:
                    mutated.solution[i] = 1 #flip the bits
                else:
                    mutated.solution[i] = 0

        #update x,y
        self.x = int("".join([str(x) for x in self.solution[0:10]]),2)
        self.y = int("".join([str(x) for x in self.solution[10:]]),2)

        return mutated

    def crossover(self, other, pc=0.6):
        '''
        With probability pc, swap x1 with x0, y1 with y0
        default value is 0.6 as defined by the assignment
        '''
        child1 = Individual()
        child2 = Individual()

        if random.random() < pc: #cross over probability is met
            child1.solution = np.concatenate((self.solution[0:10], other.solution[10:]),axis=None)
            child2.solution = np.concatenate((other.solution[0:10], self.solution[10:]),axis=None)
            return child1, child2 #give back the children
        else:
            return None, None #return nothing

def tournament_selection(population, size=5):
    '''
    tournament selection method, default number of tournament players is defined as
    five by the assignment, "use the 5-tournament selection."
    '''
    N = len(population) #population size N
    arena = [] #tournament size
    future = [] #intermediate population

    while(len(future)<N):

        #randomly select for tournament
        for i in range(size):
            x = random.randint(0,N-1)
            candidate = population[x]
            candidate_fit = candidate.calc_fitness()
            arena.append((candidate, candidate_fit)) #append as many as the tournament needs to run

        #select and put into the intermediate population
        best = min(arena, key=lambda x:x[1])
        future.append(best[0])

    return future

def generate_population(N=100):
    '''
    create a population of size N.
    default population size is 100 as defined by the assignment.
    '''
    population = []

    for i in range(N):
        population.append(Individual()) #create a new Individual and add it to the population

    return population


def genetic_algorithm(prob_mutate, with_crossover, max_gen=10, pop=100):
    '''
    genetic algorithm proper
    '''

    #variables
    generation = 0
    Pm = prob_mutate

    #create a population
    population = generate_population(pop)

    #for each generation
    while(1):

        #check stop conditions
        if(generation >= max_gen):
            #find best
            best_fit = [None, 0.0]
            for individual in population:
                if individual.calc_fitness() < best_fit[1]:
                    best_fit = [individual, individual.calc_fitness()]
            return (best_fit[0].solution, best_fit[0].calc_fitness())

        #selection
        population = tournament_selection(population)

        #crossover
        if(with_crossover):
            zoomers = []
            for i in range(0,len(population),2):
                zoomer1, zoomer2 = population[i].crossover(population[i+1]) #crossover
                if zoomer1 == None or zoomer2 == None:
                    #no new children
                    pass
                else:
                    population[i] = zoomer1 #replace parents
                    population[i+1] = zoomer2

        #mutation
        population = [x.mutation(Pm) for x in population]

        #increase generation count
        generation += 1
