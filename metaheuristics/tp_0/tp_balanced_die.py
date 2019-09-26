#Ning
#Metaheuristics for optimization
#16 sept 2019
import random

def balanced_die(num_rolls, results):
    #generate a random number
    while(num_rolls>0):
        num_rolls = num_rolls - 1 #for the number of rolls
        roll = random.randint(1,6)
        results[roll] = results[roll] + 1 #increase the value

    return results

def count_die(num_rolls, results):
    probabilities = []
    for i in range(1,7): #accounting for die value 1
        prob = results[i] / num_rolls
        probabilities.append(prob) #add value to list
    return probabilities

if __name__ == "__main__":
    res = [0]*7 #factoring in buffer of one at pos 0
    print("Testing die 10 times.")
    res = balanced_die(10, res)
    prob = count_die(10, res)
    print("Results: ", prob[0:7])
    print("Testing die 10 000 times.")
    res = balanced_die(10000, res)
    prob = count_die(10000, res)
    print("Results: ", prob[0:7])   
