#Ning
#Metaheuristics for optimization
#16 Sep 2019
import random
import math

def biased_coin(p, num_flips, res):
    while(num_flips > 0):
        num_flips = num_flips - 1
        lambda_ = math.floor(random.random() + p) #generate a random flip with bias p
        res[lambda_] = res[lambda_] + 1 #increment the bucket
    return res

def count_prob(num_flips, res):
    prob = []
    for i in range(0,2):
        probabilities = res[i] / num_flips
        prob.append(probabilities)
    return prob

def verify_p(p, actual):
    err = (p - actual)/actual
    return err

if __name__ == "__main__":
    res = [0]*2
    print("Flipping coin 10 000 times, where 1 is tails and 0 is heads, where p (prob of tails) is 0.3: ")
    res = biased_coin(0.3, 10000, res)
    prob = count_prob(10000, res)
    print("The value should be close to the p that was set: ", prob[1], "with error: ", verify_p(0.3, prob[1]))
