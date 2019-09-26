#Ning
#23 Sep
#Metaheuristics tp1

import random
import math

def start_location (num=21):
    '''
    create a random sequence of num (N) bits, where the default N is 21.
    '''
    bits = [None]*num
    for i in range(0,num):
        r_bit = math.floor(random.random()+0.5) #generates 0 or 1
        bits[i] = r_bit
    return bits

def s_bits(bit_seq):
    '''
    takes a list of bits and converts it to a string of bits.
    '''
    s_bit = ""
    for bit in bit_seq:
        s_bit = s_bit + str(bit)
    return s_bit

def l_bits(bit_s):
    '''
    takes a string of bits and turns it into a list of bits
    '''
    l_bit = []
    for char in bit_s:
        l_bit.append(int(char))
    return l_bit

def evaluate_fitness (seq, kVal, lookup):
    '''
    evaluates a sequence of bits according to the K value.
    lookup should be a dictionary that corresponds to the local fitness function fk.
    '''
    try:
        fitness = 0
        for i in range(0,len(seq)): #use the lookup table to generate the fitness for the sequence
            fitness += lookup[s_bits(seq[i:i+kVal+1])] #defined 'window' of bit evaluation according to kVal
        return fitness

    except:
        print("Error. Check your K value and lookup table.") #if K value is not defined, program exits
        exit()

def calculate_neighbors (point):
    '''
    given a point outputs a list of neighbors within 1 hamming distance.
    neighbors are strings of bits.
    '''
    neighbors = []
    for i in range(0,len(point)):
        bits = point[:] #copies point to bits by value
        bits[i] = int(not bits[i]) #inverts the bit at position i
        neighbors.append(s_bits(bits))
    return neighbors

def deterministic_hill (point, neighbors):
    '''
    given a point and a list of neighbors, return the next choice according to deterministic hill-climbing
    '''
    pass

def probabilistic_hill (point, neighbors):
    '''
    given a point and list of neighbors, return the the next choice according to probabilistic hill-climbing
    '''
    pass

if __name__ == "__main__":
    pass
