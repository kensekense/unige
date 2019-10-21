#Ning
#17 October 2019
#Linguistics TP3

import numpy as np
import pandas as pd
import math

def viterbi(wordlist, tMAT, ):
    '''
    at each stage we are calculating the max(prob tagging gene+transition, prob tagging nogene+transition) along
    with other probabilities like **, *, and STOP.
    '''

    PATH1 = np.empty((len(A), len(wordlist))) #best path so far
    PATH2 = np.empty((len(A), len(wordlist))) #pointer to previous

    #init
    PATH1[:, 0] = e_prob(wordlist[2]) #first word begins at index 2
    PATH2[:, 0] = 0

    #calculate the probability at each step
    for i in range(1, len(wordlist)):
        PATH1[:, i] = np.max(PATH1[:, i-1]+e_prob(wordlist[i])+transition(wordlist[i]), 0)
        PATH2[:, i] = np.argmax(PATH1[:, i-1]+transition(wordlist[i]), 0)

    #backtracking
    result = [None]*len(wordlist)
    result[-1] = np.argmax(PATH1[:, len(wordlist)-1])
    for i in reversed(range(1, len(wordlist))):
        result[i-1] = PATH2[result[i], i]

    return result

def e_prob(word, gene, nogene, gram):

    #defining the emission probability according to assignment in log probabilities
    e_gene = 0
    e_nogene = 0
    if word in gene and word in nogene:
        e_gene = math.log2(gene[word]) - math.log2(gram["GENE"])
        e_nogene = math.log2(nogene[word]) - math.log2(gram["NOGENE"])
    elif word in gene:
        e_gene = math.log2(gene[word]) - math.log2(gram["GENE"])
        e_nogene = 0
    elif word in nogene:
        e_gene = 0
        e_nogene = math.log2(nogene[word]) - math.log2(gram["NOGENE"])
    else: #_RARE_ tag
        e_gene = math.log2(gene["_RARE_"]) - math.log2(gram["GENE"])
        e_nogene = math.log2(nogene["_RARE_"]) - math.log2(gram["NOGENE"])

    choice = max(e_gene, e_nogene)

    if choice == e_gene:
        return ("GENE", choice)
    else:
        return ("NOGENE", choice)

def transition_setup(word, bigram, trigram):

    tR = len(bigram)
    tp_mat = np.zero((tR, tR))) #transition probability matrix is a tRxtR matrix where tR is the number of bigram states

    #defined transition probability as FSA
    tp_mat[0,1] = math.log2(trigram["* * GENE"]/bigram["* *"])
    tp_mat[0,2] = math.log2(trigram["* * NOGENE"]/bigram["* *"])
    tp_mat[1,3] = math.log2(trigram["* GENE NOGENE"]/bigram["* GENE"])
    tp_mat[1,4] = math.log2(trigram["* GENE GENE"]/bigram["* GENE"])
    tp_mat[2,5] = math.log2(trigram["* NOGENE GENE"]/bigram["* NOGENE"])
    tp_mat[2,6] = math.log2(trigram["* NOGENE NOGENE"]/bigram["* NOGENE"])
    tp_mat[3,5] = math.log2(trigram["GENE NOGENE GENE"]/bigram["GENE NOGENE"])
    tp_mat[3,6] = math.log2(trigram["GENE NOGENE NOGENE"]/bigram["GENE NOGENE"])
    tp_mat[3,8] = math.log2(trigram["GENE NOGENE STOP"]/bigram["GENE NOGENE"])
    tp_mat[4,3] = math.log2(trigram["GENE GENE NOGENE"]/bigram["GENE GENE"])
    tp_mat[4,4] = math.log2(trigram["GENE GENE GENE"]/bigram["GENE GENE"])
    tp_mat[4,7] = math.log2(trigram["GENE GENE STOP"]/bigram["GENE GENE"])
    tp_mat[5,3] = math.log2(trigram["NOGENE GENE NOGENE"]/bigram["NOGENE GENE"])
    tp_mat[5,4] = math.log2(trigram["NOGENE GENE GENE"]/bigram["NOGENE GENE"])
    tp_mat[5,7] = math.log2(trigram["NOGENE GENE STOP"]/bigram["NOGENE GENE"])
    tp_mat[6,5] = math.log2(trigram["NOGENE NOGENE GENE"]/bigram["NOGENE NOGENE"])
    tp_mat[6,6] = math.log2(trigram["NOGENE NOGENE NOGENE"]/bigram["NOGENE NOGENE"])
    tp_mat[6,8] = math.log2(trigram["NOGENE NOGENE STOP"]/bigram["NOGENE NOGENE"])

    return tp_mat

def trigram_tagger(countsfile, devfile):

    gene_emission = {}
    nogene_emission = {}
    counts_1gram = {}
    counts_2gram = {}
    counts_3gram = {}

    #open the counts file and transfer the counts into memory
    with open(countsfile, "r") as count_file:
        for line in count_file:
            line = line.split() #separate each line of the file to a list

            if(line[1] == "WORDTAG"): #WORDTAG or 1-GRAM or 2-GRAM or 3-GRAM
                if(line[2] == "GENE"): #emission for WORDTAG was GENE
                    gene_emission[line[3]] = float(line[0]) #line[3] is the word, and line[0] is the count
                else:
                    nogene_emission[line[3]] = float(line[0]) #otherwise tag is NOGENE

            elif(line[1] == "1-GRAM"):
                counts_1gram[line[2]] = float(line[0])

            elif(line[1] == "2-GRAM"): #line[3] and line[4] are emissions
                counts_2gram[line[2]+" "+line[3]] = float(line[0])

            elif(line[1] == "3-GRAM"): #the rest are trigrams
                counts_3gram[line[2]+ " "+line[3]+" "+line[4]] = float(line[0])


    #open the devfile to get the list of words
    wordlist = ["*", "*"] #make sure to start with * * tokens
    with open(devfile, "r") as dev_file:
        for line in dev_file:
            line = line.split("\n")
            word = line[0]

            if(len(word) > 0): #not an empty line

                wordlist.append(word)

    wordlist.append("STOP") #append STOP tag at the end



if __name__ == "__main__":
    trigram_tagger("gene_rare.counts", "gene.dev")
