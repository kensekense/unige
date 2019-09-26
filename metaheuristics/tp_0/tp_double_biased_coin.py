#Ning
#Metaheuristics for optimization
#17 Sep 2019
import random
import math

def flip_coin(p):
    flip = math.floor(random.random() + p)
    return flip

def compare_coin(a, b):
    if(a == b):
        return 2 #coins are the same, acts as an escape sequence
    else:
        return a #different, return the first flip

if __name__ == "__main__":
    print("Define a biased coin C, with p being the probability of flipping tails set as 0.3.")
    p = 0.3
    results = [0]*3
    NUM_FLIPS = 10000
    count = NUM_FLIPS
    while(count > 0):
        count = count - 1
        f1 = flip_coin(p)
        f2 = flip_coin(p)
        results[compare_coin(f1,f2)] += 1 #increment
    print("Occurences observed (heads, tails, throwaways): ", results)
    LEGIT_FLIPS = results[0] + results[1]
    print("Probabilities should be around 50% for both: ", results[0]/LEGIT_FLIPS, results[1]/LEGIT_FLIPS)
