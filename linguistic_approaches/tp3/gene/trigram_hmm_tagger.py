#Ning
#23 October 2019
#Linguistics TP3

import numpy as np
import math
from collections import defaultdict

def setup_dictionaries(countsfile):
    '''
    set up the required hashing dictionaries in order to retrieve emission probabilities
    '''
    gene_emission = {}
    nogene_emission = {}
    counts_1gram = {}
    counts_2gram = {}
    counts_3gram = {}

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

    return gene_emission, nogene_emission, counts_1gram, counts_2gram, counts_3gram

def setup_wordlist(devfile):
    '''
    set up the wordlist so that it has all the words from the devfile
    '''
    #open the devfile to get the list of words
    #wordlist = ["*", "*"] #make sure to start with * * tokens
    wordlist = []
    wordlist_with_spaces = []

    with open(devfile, "r") as dev_file:
        for line in dev_file:
            line = line.split("\n")
            word = line[0]

            if(len(word) > 0): #not an empty line
                wordlist.append(word)
                wordlist_with_spaces.append(word)
            else:
                wordlist_with_spaces.append("\n")
    #wordlist.append("STOP") #append STOP tag at the end

    return wordlist, wordlist_with_spaces


def setup_emissions (wordlist, gene, nogene, gram):
    '''
    given the word and GENE/NOGENE
    taglist = ["GENE", "NOGENE"]
    gets the emission probabilities for each word
    returns a dictionary of emission probabilities
    '''
    e = {}
    #need to iterate
    #for word in wordlist:
    #q[('WORD', 'GENE')] = gene[word]/gram["GENE"]
    #check for whether or not it is in GENE/NOGENE in viterbi proper
    for word in wordlist:
        if word in gene and word in nogene:
            e[(word, "GENE")] = math.log2(gene[word])-math.log2(gram["GENE"])
            e[(word, "NOGENE")] = math.log2(nogene[word])-math.log2(gram["NOGENE"])
        elif word in gene:
            e[(word, "GENE")] = math.log2(gene[word])-math.log2(gram["GENE"])

        elif word in nogene:
            e[(word, "NOGENE")] = math.log2(nogene[word])-math.log2(gram["NOGENE"])
        else:
            e[(word, "GENE")] = math.log2(gene["_RARE_"])-math.log2(gram["GENE"])
            e[(word, "NOGENE")] = math.log2(gene["_RARE_"])-math.log2(gram["NOGENE"])

    return e

def setup_transition (bigram, trigram):
    '''
    calculate the transitions
    '''
    q = {}
    taglist = ["GENE", "NOGENE"]
    #q[("GENE","GENE","NOGENE")] = trigram["GENE NOGENE GENE"]/bigram["GENE NOGENE"]
    for tag_2 in taglist:
        for tag_1 in taglist:
            for tag in taglist: #three times for good luck and also because trigrams
                q[(tag, tag_2, tag_1)] = math.log2(trigram["{0} {1} {2}".format(tag_2, tag_1, tag)])-math.log2(bigram["{0} {1}".format(tag_2, tag_1)])

    #special characters
    q[("STOP", "GENE","GENE")] = math.log2(trigram["GENE GENE STOP"])-math.log2(bigram["GENE GENE"])
    q[("STOP", "GENE","NOGENE")] = math.log2(trigram["GENE NOGENE STOP"])-math.log2(bigram["GENE NOGENE"])
    q[("STOP", "NOGENE","GENE")] = math.log2(trigram["NOGENE GENE STOP"])-math.log2(bigram["NOGENE GENE"])
    q[("STOP", "NOGENE","NOGENE")] = math.log2(trigram["NOGENE NOGENE STOP"])-math.log2(bigram["NOGENE NOGENE"])
    q[("GENE", "*", "*")] = math.log2(trigram["* * GENE"])-math.log2(bigram["* *"])
    q[("NOGENE", "*", "*")] = math.log2(trigram["* * NOGENE"])-math.log2(bigram["* *"])

    return q


def viterbi(wordlist, taglist, e, q):
    '''
    taglist = ["GENE", "NOGENE"]
    where k is the position of the wordlist (sequence), u is TAG_k-1, v is TAG_k
    e is the emission dictionary
    q is the transition dictionary
    '''
    trellis = {}
    bp = {}


    #init values
    trellis[(0, "*", "*")] = 0.0

    #accomodate for * *
    def S(k):
        if k in (-1, 0):
            return {"*"}
        else:
            return taglist

    #viterbi proper
    for k in range(1, len(wordlist)+1): #k is the position
        for u in S(k-1): #u is TAG_k-1
            for v in S(k): #v is TAG_k

                max_score = float('-Inf')
                max_tag = None

                for w in S(k-2): #w is TAG_k-2

                    #need to make sure we have a word
                    if e.get((wordlist[k-1], v), 0) != 0:
                        score = trellis.get((k-1, w, u), -1000) + q.get((w, u, v), -1000) + e.get((wordlist[k-1], v))
                        #establish a max and a tag for backtracking
                        if score > max_score:
                            max_score = score
                            max_tag = w

                trellis[(k, u, v)] = max_score
                bp[(k, u, v)] = max_tag


    #doing the ending
    max_score = float('-Inf')
    u_end, v_end = None, None
    for u in S(len(wordlist)-1):
        for v in S(len(wordlist)):
            score = trellis.get((len(wordlist), u, v), -1000) + q.get((u, v, "STOP"), -1000)
            if score > max_score:
                max_score = score
                u_end = u
                v_end = v

    #zipping together tags
    tags = []
    tags.append(v_end)
    tags.append(u_end)

    for i, k in enumerate(range(len(wordlist)-2, 0, -1)):
        tags.append(bp[(k+2, tags[i+1], tags[i])]) #append the proper tags, but know its backwards
    tags.reverse() #flip

    sentence_with_tags = []
    for j in range(0, len(wordlist)):
        sentence_with_tags.append(wordlist[j]+" "+tags[j]+"\n")

    return sentence_with_tags


if __name__ == "__main__":

    RARE_COUNTS_FILE = "gene_rare.counts"
    DEV_FILE = "gene.test"

    #setup the proper resources to implement tagging
    gene, nogene, gram, bigram, trigram = setup_dictionaries(RARE_COUNTS_FILE)
    wordlist, wws = setup_wordlist(DEV_FILE)
    e = setup_emissions(wordlist, gene, nogene, gram)
    q = setup_transition(bigram, trigram)

    #testing center
    #print(viterbi(wordlist, ["GENE", "NOGENE"], e, q))
    tag_results = viterbi(wordlist, ["GENE", "NOGENE"], e, q)

    for i in range(0, len(wws)):
        if wws[i] == "\n":
            tag_results.insert(i, "\n")


    with open("gene.test.p2.out", "w") as call_my_therapist:
        call_my_therapist.writelines(tag_results)
