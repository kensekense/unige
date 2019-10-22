#Ning
#17 October 2019
#Linguistics TP3

import numpy as np
import pandas as pd
import math

def viterbi(wordlist, tMAT, eMAT, initState):
    '''
    at each stage we are calculating the max(prob tagging gene+transition, prob tagging nogene+transition) along
    with other probabilities like **, *, and STOP.
    '''

    PATH1 = np.empty((len(tMAT), len(wordlist))) #best path so far
    PATH2 = np.empty((len(tMAT), len(wordlist))) #pointer to previous

    #init
    PATH1[:, 0] = initState+eMAT[:,2] #first word begins at index 2
    PATH2[:, 0] = 0

    #calculate the probability at each step
    for i in range(1, len(wordlist)):
        PATH1[:, i] = np.max(PATH1[:, i-1]+tMAT.T+eMAT[np.newaxis,:,i], 0) #probability of previous path, transit prob, emission prob
        PATH2[:, i] = np.argmax(PATH1[:, i-1]+tMAT.T, 0) #keep track of previous max for backtracking

    #backtracking
    result = np.empty(len(wordlist), 'B')
    result[-1] = np.argmax(PATH1[:, len(wordlist)-1])
    for i in reversed(range(1, len(wordlist))):
        result[i-1] = PATH2[result[i], i]

    return result

def emission_setup(wordlist, gene, nogene, gram, bigram):
    '''
    creates the emission matrix
    '''
    eR = len(wordlist)
    tR = len(bigram)
    e_mat = np.zeros((tR, eR))

    for i in range(len(wordlist)):
        #ignore '*' and 'STOP'
        word = wordlist[i]
        if(word != "*" and word != "STOP"):
            if word in gene and word in nogene:
                #split prob
                e_mat[0,i] = math.log2(gene[word]/gram["GENE"])
                e_mat[1,i] = math.log2(nogene[word]/gram["NOGENE"])
            elif word in gene:
                #single prob
                e_mat[0,i] = math.log2(gene[word]/gram["GENE"])
            elif word in nogene:
                #single prob
                e_mat[1,i] = math.log2(nogene[word]/gram["NOGENE"])
            else:
                #_RARE_
                e_mat[0,i] = math.log2(gene["_RARE_"]/gram["GENE"])
                e_mat[1,i] = math.log2(nogene["_RARE_"]/gram["NOGENE"])

    return e_mat

def transition_setup(bigram, trigram):
    '''
    creates the transition matrix
    '''
    tR = len(bigram)
    tp_mat = np.zeros((tR, tR)) #transition probability matrix is a tRxtR matrix where tR is the number of bigram states

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

    #TODO do tagging here, set up initState, tMAT
    emission_matrix = emission_setup(wordlist, gene_emission, nogene_emission, counts_1gram, counts_2gram)
    transition_matrix = transition_setup(counts_2gram, counts_3gram)
    v_result = viterbi(wordlist, transition_matrix, emission_matrix, 0)
    print(v_result)

if __name__ == "__main__":
    trigram_tagger("gene_rare.counts", "gene.dev")
