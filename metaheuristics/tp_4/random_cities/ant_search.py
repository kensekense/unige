#Ning
#09 Nov 2019

import numpy as np
import math
import random
import time

def create_city (cityfile):
    '''
    create a dictionary of cities locations
    taken directly from previous TP3 implementation
    '''
    cityscape = {}
    with open(cityfile, "r") as city_file:
        for line in city_file:
            line = line.split()
            cityscape[line[0]] = (float(line[1]), float(line[2]))
    return cityscape

def distance (i, j):
    '''
    returns the euclidean distance
    '''
    x = i[0] - j[0]
    y = i[1] - j[1]
    distance = math.sqrt(x**2 + y**2) #euclidean distance
    return distance

def length_of_tour (path, city):
    '''
    the equivalent of finding the fitness of a tour
    '''
    length = 0.0
    for i in range(0, len(path)-1):
        length += distance(city[path[i]], city[path[i+1]])
    length += distance(city[path[len(path)-1]], city[path[0]])

    return length

def inverse_distance (i, j):
    '''
    specifically written for finding the inverse_distance, used in the AS algorithm
    '''
    x = i[0] - j[0]
    y = i[1] - j[1]
    distance = math.sqrt(x**2 + y**2) #euclidean distance
    return 1.0/distance #inverse distance

def init_ph_graph (city, T_0):
    '''
    defines the edges in the graph as a dictionary, with the keys being the edges, and the values being pheromone values.
    originally all pheromone values set to 0.01, as defined by the assignment
    '''

    #obtain a list of nodes
    all_nodes = list(city.keys())

    #establish a dictionary of the graph
    ph_graph = {}

    for i in range(0, len(all_nodes)):
        for j in range(i, len(all_nodes)): #only do one side, save space
            if i != j: #no self edges
                ph_graph["{0} {1}".format(all_nodes[i], all_nodes[j])] = T_0 #a small amount > 0

    return ph_graph

def update_graph (path, ph_graph, city, Q):

    '''
    updates the graph initialized as per our assignment
    Q is taken from the NN algorithm length averaged over 10 runs
    '''

    #define a list of edges travelled
    all_edges = []

    #search all the ant's path
    for i in range(0, len(path)-1):
        all_edges.append((path[i], path[i+1])) #as a tuple

    #define ant-k's ph levels
    Lk = length_of_tour(path, city)
    #Q = 66.0323178894233 #length of NN algorithm
    delt_ph = Q/Lk #equation 3
    p = 0.1 #defined by our problem

    #check all edges against ph_graph and set ph, accounting for alphabetical order
    for edge in all_edges:

        try:
            ph = (1-p)*ph_graph["{0} {1}".format(edge[0], edge[1])] + delt_ph
            ph_graph["{0} {1}".format(edge[0], edge[1])] = ph #normal order
        except:
            ph = (1-p)*ph_graph["{0} {1}".format(edge[1], edge[0])] + delt_ph
            ph_graph["{0} {1}".format(edge[1], edge[0])] = ph #otherwise try switched

    #return updated graph post ant-k's tour
    return ph_graph

def do_tour (path, ph_graph, city):

    '''
    this function used by all ants to create their solution
    '''

    #path is originally just a starting node
    #return should be the input path + one more node travelled (accepted node)

    #establish constants
    A = 1
    B = 5

    while(True):

        #generate all cities not in current path
        rest = []
        for node in city:
            if not node in path:
                rest.append(node)

        #exit condition
        if len(rest) == 0:
            return path

        current = path[-1] #the last node in the path is the current node i
        potential = rest[random.randint(0,len(rest)-1)] #a random node in the unvisited list is node j

        #establish Tij
        try:
            Tij = ph_graph["{0} {1}".format(current, potential)]
        except:
            Tij = ph_graph["{0} {1}".format(potential, current)]

        denom = 0.0
        for j in range(0, len(rest)):
            il = rest[j]
            try:
                Til = ph_graph["{0} {1}".format(current, il)]
            except:
                Til = ph_graph["{0} {1}".format(il, current)]
            denom += (Til**A)*(inverse_distance(city[current], city[il])**B)

        probability = (Tij**A)*(inverse_distance(city[current], city[potential])**B)/denom

        #accept-reject
        if random.random() < probability: #accepted
            path.append(potential) #add to path

def nearest_neighbor(cityfile):
    '''
    greedy algorithm implementation
    '''
    city = create_city(cityfile)

    nodes = list(city.keys())
    path = [nodes[random.randint(0, len(nodes)-1)]]
    #path = ['i'] #for testing consistency

    visited = []
    current = path[-1]

    while(1):

        #create the rest of the options
        rest = []
        for node in nodes:
            if not node in path:
                rest.append(node)

        #exit condition
        if len(rest) == 0:
            return path, length_of_tour(path, city)

        #find the distance from current to rest
        shortest = float('inf')
        for i in range(0, len(rest)):
            if distance(city[current], city[rest[i]]) < shortest:
                best = rest[i]

        current = best[:] #copy the best as current
        path.append(current) #add it to the path


def ant_search (cityfile, rank, timesteps):
    '''
    the AS algorithm proper
    note that we find Q by running NN on the problem set 10 times and obtain the average over those 10 runs
    '''

    #create the city
    city = create_city(cityfile)

    #find Q
    sum = 0.0
    for i in range(10):
        sum+= nearest_neighbor(cityfile)[1]
    Q = sum/10.0
    #find T_0
    T_0 = 1/Q

    #initialize the graph
    ph_graph = init_ph_graph(city, T_0)

    for t in range (0, timesteps):
        for k in range (0, rank):

            #random city start and clear this timestep's paths
            nodes = list(city.keys())
            ant_paths = []

            ant_k_path = [nodes[random.randint(0, len(nodes)-1)]]
            #ant-k makes a move
            ant_paths.append(do_tour(ant_k_path, ph_graph, city)) #determine ant-k's move

        #update the graph after all ants have moved
        for paths in ant_paths:
            ph_graph = update_graph(paths, ph_graph, city, Q) #update the graph

        #keep the best solution at the end of the timesteps
        length_best = float('inf')
        best = []
        for i in range(0, len(ant_paths)):
            k_path = length_of_tour(ant_paths[i], city)
            if k_path < length_best:
                best = ant_paths[i][:]

    return best, length_of_tour(best, city)



if __name__ == "__main__":

    
    wp = open("results.dat", "w")

    #run on cities.dat, print image
    wp.write("cities.dat results: {0}\n".format(ant_search("cities.dat", 18, 20)))

    #run on cities2.dat, print image
    wp.write("cities2.dat results: {0}\n".format(ant_search("cities2.dat", 50, 20)))

    #report the results for above

    #analyze the influence of m and tmax on quality of solutions

    #run NN 10 times and compare results with the NN average
    nn_sum = 0.0
    for i in range(10):
        nn_sum += nearest_neighbor("cities.dat")[1]
    wp.write("cities.dat NN results: {0}\n".format(nn_sum/10.0))

    nn_sum = 0.0
    for i in range(10):
        nn_sum += nearest_neighbor("cities2.dat")[1]
    wp.write("cities2.dat NN results: {0}\n".format(nn_sum/10.0))

    wp.close()

    #generate 5 TSP problems of size 50, 60, 80, 100, compare with NN average
    wp = open("results_50.dat", "w")
    wp.write("cities_50_1.dat results: {0}\n".format(ant_search("cities_50_1.dat", 50, 10)))
    wp.write("cities_50_2.dat results: {0}\n".format(ant_search("cities_50_2.dat", 50, 10)))
    wp.write("cities_50_3.dat results: {0}\n".format(ant_search("cities_50_3.dat", 50, 10)))
    wp.write("cities_50_4.dat results: {0}\n".format(ant_search("cities_50_4.dat", 50, 10)))
    wp.write("cities_50_5.dat results: {0}\n".format(ant_search("cities_50_5.dat", 50, 10)))

    nn_sum = 0.0
    for i in range(10):
        nn_sum += nearest_neighbor("cities_50_1.dat")[1]
    wp.write("cities_50.dat NN results: {0}\n".format(nn_sum/10.0))
    wp.close()

    wp = open("results_60.dat", "w")
    wp.write("cities_60_1.dat results: {0}\n".format(ant_search("cities_60_1.dat", 60, 10)))
    wp.write("cities_60_2.dat results: {0}\n".format(ant_search("cities_60_2.dat", 60, 10)))
    wp.write("cities_60_3.dat results: {0}\n".format(ant_search("cities_60_3.dat", 60, 10)))
    wp.write("cities_60_4.dat results: {0}\n".format(ant_search("cities_60_4.dat", 60, 10)))
    wp.write("cities_60_5.dat results: {0}\n".format(ant_search("cities_60_5.dat", 60, 10)))

    nn_sum = 0.0
    for i in range(10):
        nn_sum += nearest_neighbor("cities_60_1.dat")[1]
    wp.write("cities_60.dat NN results: {0}\n".format(nn_sum/10.0))
    wp.close()

    wp = open("results_80.dat", "w")
    wp.write("cities_80_1.dat results: {0}\n".format(ant_search("cities_80_1.dat", 80, 10)))
    wp.write("cities_80_2.dat results: {0}\n".format(ant_search("cities_80_2.dat", 80, 10)))
    wp.write("cities_80_3.dat results: {0}\n".format(ant_search("cities_80_3.dat", 80, 10)))
    wp.write("cities_80_4.dat results: {0}\n".format(ant_search("cities_80_4.dat", 80, 10)))
    wp.write("cities_80_5.dat results: {0}\n".format(ant_search("cities_80_5.dat", 80, 10)))

    nn_sum = 0.0
    for i in range(10):
        nn_sum += nearest_neighbor("cities_80_1.dat")[1]
    wp.write("cities_80.dat NN results: {0}\n".format(nn_sum/10.0))
    wp.close()


    wp = open("results_100.dat", "w")
    wp.write("cities_100_1.dat results: {0}\n".format(ant_search("cities_100_1.dat", 100, 10)))
    wp.write("cities_100_2.dat results: {0}\n".format(ant_search("cities_100_2.dat", 100, 10)))
    wp.write("cities_100_3.dat results: {0}\n".format(ant_search("cities_100_3.dat", 100, 10)))
    wp.write("cities_100_4.dat results: {0}\n".format(ant_search("cities_100_4.dat", 100, 10)))
    wp.write("cities_100_5.dat results: {0}\n".format(ant_search("cities_100_5.dat", 100, 10)))

    nn_sum = 0.0
    for i in range(10):
        nn_sum += nearest_neighbor("cities_100_1.dat")[1]
    wp.write("cities_100.dat NN results: {0}\n".format(nn_sum/10.0))
    wp.close()

    #compare results from AS to Simulated Annealing (quality and execution time)
