#Ning
#16 October 2019
#Data Science TP3

from mnist import MNIST
import random
import numpy as np
from sklearn.neighbors import NearestNeigbhors
from sklearn.decomposition import PCA

def load_MNIST_data():
    '''
    loads the MNIST dataset downloaded from the official website in python using MNIST library.
    '''

    data = MNIST('mnistdata')

    #images_train is a 60,000 sample list of 28x28 imgs
    #labels_train is a 60,000 digit list of labels
    images_train, labels_train = data.load_training()

    #TODO: do some action here


if __name__ == "__main__":

    load_MNIST_data()