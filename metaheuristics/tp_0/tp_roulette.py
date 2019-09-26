#Ning
#Metaheuristics for optimization
#17 Sept 2019
import random
from bisect import *

def init_p (p_arr, num_events):
    for i in range(0, num_events):
        rand = random.random()
        p_arr[i] = rand
    return p_arr

def calc_cumulative (p_arr, num_events):
    #should calculate the cumulative prob
    c_prob = [0]*num_events
    for j in range(0, num_events):
        c_prob[j] = p_arr[j]
    for i in range(1, num_events):
        c_prob[i] = c_prob[i] + c_prob[i-1]

    return c_prob

def roll(c_prob, c_total):
    gen_rand = random.uniform(0, c_total) #generate a number between lowest and cumulative prob
    return bisect_right(c_prob, gen_rand)

if __name__ == "__main__":
    NUM_ROLLS = 100000
    NUM_EVENTS = 20
    p_arr = [0]*NUM_EVENTS

    print("Generating the Pi values...\n")
    p_arr = init_p(p_arr, NUM_EVENTS)
    print("Calculating cumulative probability, denoted Pic...\n")
    PIC = calc_cumulative(p_arr, NUM_EVENTS)
    c_total = PIC[NUM_EVENTS-1]
    runs = NUM_ROLLS
    occ = [0]*NUM_EVENTS
    while(runs > 0):
        runs = runs - 1
        spin = roll(PIC, c_total)
        occ[spin] = occ[spin]+1
    CHECK_VAL = random.randint(0,NUM_EVENTS-1)
    print("Final results omitted due to length, but these numbers should be comparable: \n", occ[CHECK_VAL]/NUM_ROLLS, " and ", p_arr[CHECK_VAL]/c_total)
