#Ning
#17 Nov
#Metaheuristics TP5

#import statements
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import math
import random

#preliminary look at the X.dat file and Y.dat file
#Note that 0 corresponds to 'two' and 1 corresponds to 'three'

def transfer_file_to_arrays (filename):

    images = []

    with open(filename, "r") as fp:
        for line in fp:
            line = line.split(",") #split values on ,
            for i in range(0, len(line)):
                line[i] = float(line[i]) #turn into a float
            line = np.array(line)
            images.append(line) #append in np array format

    return images

def get_labels (filename):
    labels = []
    with open(filename, "r") as fp:
        for line in fp:
            labels.append(float(line))
    return labels


def turn_two_to_one (theta1, theta2):
    return np.concatenate((theta1.flatten(), theta2.flatten()), axis=None)

def turn_one_to_two (big_theta):

    theta1 = np.reshape(big_theta[0:10025], (25,401)) #need to be careful here because of shape
    theta2 = np.reshape(big_theta[10025:], (1,26))

    return theta1, theta2

def sigmoid (X):
    return 1/(1+np.exp(-X))

def first_layer (picture):
    '''
    first layer's role is to download the 400 pixels of the picture
    and have one neuron that is the bias
    '''
    #add bias neuron
    layer_n = picture.shape[0]
    first_layer = np.insert(picture, 0, 1.0) #add 1 as the bias

    return first_layer

def second_layer (layer, theta):
    '''
    second layer contains 25 neurons, plus 1 for the bias
    job is to matmul the first layer's output with theta, apply sigmoid function, add bias

    theta is the matrix of size (25, 401)
    '''

    res = np.matmul(theta, layer) #should be a matmul of sizes (25,401)(401,) -> (25,)

    #apply the sigmoid function
    res = sigmoid(res)

    res_n = res.shape[0] #should be 25

    second_layer = np.insert(res, 0, 1.0) #add 1 as the bias

    return second_layer

def third_layer (layer, theta):
    '''
    third layer contains 1 neuron
    job is to matmul the second layer's output with theta, apply sigmoid function, and return

    theta is the matrix of size (1, 26)
    '''

    res = np.matmul(theta, layer) #should be a matmul of sizes (1,26)(26,) -> (1,)

    #apply the sigmoid function
    res = sigmoid(res)

    return res #should be a singular value answer, our prediction

def nn_predict (image, big_theta):
    '''
    application of all three layers
    '''

    #temporary values
    theta1, theta2 = turn_one_to_two(big_theta)

    layer1 = first_layer(image)
    layer2 = second_layer(layer1, theta1) #this theta value will take on PSO's output once complete
    layer3 = third_layer(layer2, theta2)

    return layer3[0] #the prediction

def calc_fitness(big_theta, images, labels):
    fitness = 0.0
    for k in range(0, len(labels)):
        fitness+=(labels[k] - nn_predict(images[k], big_theta))**2
    return fitness/len(labels)

def init_positions ():
    return 2*np.random.rand(25,401)-1, 2*np.random.rand(1,26)-1

def init_velocities ():
    return np.zeros((25,401)), np.zeros((1,26))

def PSO (n, tmax, images, labels):

    #variables
    global_best = np.array([None,float('inf')]) #global_best is (position, fitness)
    inertia_constant = 0.9
    c1 = 1.99811 #defined by the assignment as close to 2
    c2 = 1.99899
    t = 0
    vmax = 0.1

    #initialize particles -> (s, v, b)
    particles = []
    for i in range(n):
        s0_a, s0_b = init_positions()
        v0_a, v0_b = init_velocities()

        big_s0 = turn_two_to_one(s0_a, s0_b)
        big_v0 = turn_two_to_one(v0_a, v0_b)
        particle = np.array([big_s0, big_v0, big_s0]) #personal_best init is s0
        particles.append(particle)


    while(t < tmax):

        #for each particle
        for i in range(n):
            fit = calc_fitness(particles[i][0], images, labels) #positions are taken to calc fitness
            pbest_fit = calc_fitness(particles[i][2], images, labels)
            if fit <= pbest_fit: #if better than personal_best
                particles[i][2] = particles[i][0][:] #copy as new best

        #set global_best
        for i in range(n):
            fit = calc_fitness(particles[i][2], images, labels)
            if fit <= global_best[1]: #if personal_best better than global_best
                global_best[1] = fit
                global_best[0] = particles[i][2][:] #set new values for global

        #particle updates
        for i in range(n):
            r1 = random.random()
            r2 = random.random()

            #update velocity
            particles[i][1] = inertia_constant*particles[i][1] + c1*r1*(particles[i][2]-particles[i][0]) + c2*r2*(global_best[0]-particles[i][0])

            #velocity cutoff?
            particles[i][1][particles[i][1] > vmax] = vmax
            particles[i][1][particles[i][1] < -1*vmax] = -1*vmax

            #update positions
            particles[i][0] = particles[i][0] + particles[i][1]

            #correct particles out of range
            for x in range(len(particles[i][0])):
                particles[i][0][x] -(2*(particles[i][0][x]-1))
                particles[i][0][x] + (2*-1-particles[i][0][x])

        t = t + 1

    #get the stats of the global_best
    theta1, theta2 = turn_one_to_two(global_best[0]) #separate global_best's particle into thetas
    return theta1, theta2 #return

def calc_error(a,b,images,labels):
    #error testing
    correct = 0
    predictions = []
    for i in range(len(images)):
        predict = nn_predict(images[i], turn_two_to_one(a,b))
        predictions.append(predict)
        truth = labels[i]

        if truth == int(predict+0.5):
            correct += 1

    return correct/len(labels)

if __name__ == "__main__":

    #obtain images and labels
    images = transfer_file_to_arrays("X.dat")
    labels = get_labels("Y.dat")

    #run PSO ten times and output theta1, theta2, prediction error, to file to report
    for i in range(10):
        a,b = PSO(20, 200, images, labels)
        error = calc_error(a,b,images, labels)
        with open("./results/run_{0}.dat".format(i), "w") as wp:
            wp.write(str(calc_fitness(turn_two_to_one(a,b),images,labels))+"\n")
            wp.write(str(error))
