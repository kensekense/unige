#Ning

import numpy as np
import math
import random
import time

def create_city (cityfile):
    cityscape = {}
    with open(cityfile, "r") as city_file:
        for line in city_file:
            line = line.split()
            cityscape[line[0]] = (float(line[1]), float(line[2]))
    return cityscape

def find_distance (a, b):
    '''
    a,b are tuples (x-loc,y-loc)
    '''
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance

def calc_fitness (path, cityscape):
    '''
    path is a list of cities
    cityscape is the city dictionary
    '''
    fitness = 0.0
    for i in range(0, len(path)-1):
        fitness += find_distance(cityscape[path[i]], cityscape[path[i+1]])
    fitness += find_distance(cityscape[path[len(path)-1]], cityscape[path[0]])

    return fitness

def roll_two (l):
    i = 0
    j = 0
    while(i==j):
        i = random.randint(0,l-1)
        j = random.randint(0,l-1)
    return i,j

def random_config (city):
    '''
    takes the city dictionary to create initial configuration
    '''
    rand_config = list(city.keys())

    x = random.randint(10,30)

    for k in range(0, x):

        i,j = roll_two(len(rand_config))

        temp = rand_config[i]
        rand_config[i] = rand_config[j]
        rand_config[j] = temp

    return rand_config

def accept_reject(current_config, update_config, temperature, city):
    e1 = float(calc_fitness(current_config, city))
    e2 = float(calc_fitness(update_config, city))
    delta_e = e2-e1

    try:
        prob_accept = math.exp((-1*delta_e)/temperature)
    except:
        prob_accept = float("-inf")

    if delta_e < 0:
        return True
    elif random.random() < prob_accept:
        return True
    else:
        return False

def find_initial_temperature(city):

    init_config = random_config(city)
    config = init_config[:]

    delta_energies = []

    e1 = calc_fitness(config, city)

    for i in range(0,100):

        s1, s2 = roll_two(len(config))
        move_config = random_config(city)[:]
        e2 = calc_fitness(move_config, city)
        delta_energies.append(e2-e1)

    avg = sum(delta_energies)/float(100)
    return (-1*avg)/math.log(0.5)

def simulated_annealing (data):

    #define the cityscape
    cities = create_city(data)

    #Initial Configuration
    config = random_config(cities)[:]
    #print(config, calc_fitness(config, cities))
    starting_e = calc_fitness(config,cities)
    N = len(config)

    #Initial Temperature
    temp = find_initial_temperature(cities)
    #temp = 0.1

    #!!!
    accepted = 0
    tries = 0
    iteration = 0
    fitnesses = []
    freeze_condition = False

    while(not freeze_condition):

        #Elementary Configuration
        #i, j = roll_two(N)
        #transform = movement(config, i, j)[:]
        transform = random_config(cities)[:]

        #Accept/Reject
        if accept_reject(config, transform, temp, cities):
            config = transform[:]
            accepted += 1
            tries += 1
        else:
            #reject
            tries += 1

        if(accepted == 12*N or tries == 100*N):
            #equilibrium reached, track fitness and reduce temperature
            fitnesses.append(calc_fitness(config, cities))
            temp = temp*0.9
            iteration += 1
            accepted = 0
            tries = 0

            if iteration > 3:
                if fitnesses[iteration-4] == fitnesses[iteration-1]: #no improvement
                    if fitnesses[iteration-3] == fitnesses[iteration-1]: #within the last
                        if fitnesses[iteration-2] == fitnesses[iteration-1]: #three temperature steps
                            freeze_condition = True

    return config, calc_fitness(config, cities)

def greedy_algorithm (data):

    #define the cityscape
    cities = create_city(data)

    #Initial Configuration
    config = random_config(cities)[:]
    #print(config, calc_fitness(config, cities))
    starting_e = calc_fitness(config, cities)
    N = len(config)

    visited = []
    current = config[0]
    path = []
    best = 100
    now = 100

    path.append(current)
    for i in range(0, N):
        for j in range(0, N):
            if i!=j and not(config[j] in visited):
                now = find_distance(cities[config[i]],cities[config[j]])
                if now <= best:
                    best_index = j
        visited.append(config[best_index])
        current = config[best_index]
        path.append(config[best_index])

    return path, calc_fitness(path, cities)

if __name__ == "__main__":

    #run the comparison 10 times
    start_10times = time.time()
    comparisons = []
    for times in range(0,10):
        sa_result = simulated_annealing("cities.dat")[1]
        greedy_result = greedy_algorithm("cities.dat")[1]
        comparisons.append("{0}\t{1}\n".format(str(sa_result),str(greedy_result)))
    comparisons.append("Total Run Time: {0}".format(time.time()-start_10times))

    with open("results.dat", "w") as wfile:
        wfile.writelines(comparisons)


    #run the comparison for 5 files (50)
    for i in range(1,6):
        start_size50 = time.time() #start time
        comparisons = []
        sa_result = simulated_annealing("cities_50_{0}.dat".format(str(i)))
        greedy_result = greedy_algorithm("cities_50_{0}.dat".format(str(i)))
        comparisons.append("{0}\t{1}\n".format(str(sa_result),str(greedy_result)))
        comparisons.append("Total Run Time: {0}".format(time.time()-start_size50)) #end time

        with open("results_50_{0}.dat".format(str(i)), "w") as wfile:
            wfile.writelines(comparisons)

    #run the comparison for 5 files (60)
    for i in range(1,6):
        start_size60 = time.time() #start time
        comparisons = []
        sa_result = simulated_annealing("cities_60_{0}.dat".format(str(i)))
        greedy_result = greedy_algorithm("cities_60_{0}.dat".format(str(i)))
        comparisons.append("{0}\t{1}\n".format(str(sa_result),str(greedy_result)))
        comparisons.append("Total Run Time: {0}".format(time.time()-start_size60)) #end time

        with open("results_60_{0}.dat".format(str(i)), "w") as wfile:
            wfile.writelines(comparisons)

    #run the comparison for 5 files (80)
    for i in range(1,6):
        start_size80 = time.time() #start time
        comparisons = []
        sa_result = simulated_annealing("cities_80_{0}.dat".format(str(i)))
        greedy_result = greedy_algorithm("cities_80_{0}.dat".format(str(i)))
        comparisons.append("{0}\t{1}\n".format(str(sa_result),str(greedy_result)))
        comparisons.append("Total Run Time: {0}".format(time.time()-start_size80)) #end time

        with open("results_80_{0}.dat".format(str(i)), "w") as wfile:
            wfile.writelines(comparisons)

    #run the comparison for 5 files (100)
    for i in range(1,6):
        start_size100 = time.time() #start time
        comparisons = []
        sa_result = simulated_annealing("cities_100_{0}.dat".format(str(i)))
        greedy_result = greedy_algorithm("cities_100_{0}.dat".format(str(i)))
        comparisons.append("{0}\t{1}\n".format(str(sa_result),str(greedy_result)))
        comparisons.append("Total Run Time: {0}".format(time.time()-start_size100)) #end time

        with open("results_100_{0}.dat".format(str(i)), "w") as wfile:
            wfile.writelines(comparisons)
