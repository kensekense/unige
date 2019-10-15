#Ning
#10 October 2019
#Linguistics TP3

import numpy as np
import pandas as pd

def read_file (filename):
    '''
    read the file and organize it's data into a list
    '''
    words = []
    with open(filename, "r") as fp:
        for line in fp:
            if(len(line) > 1): #not an empty line
                (word, tag) = line.split() #stores the word separately from tag
                words.append(word)

    return words

def get_count (words):
    '''
    get a count of each word in the list of words
    '''
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def replace_words (filename, outfile, freq):
    '''
    replace the word in the doc with _RARE_ if count is < 5
    '''
    output_ = []
    with open(filename, "r") as fp:
        for line in fp:
            if(len(line)>1):
                (word, tag) = line.split() #read the words separately
            if(len(line)<1): #empty line
                output_.append("\n")
                continue
            if freq[word] < 5: #strictly
                output_.append("_RARE_"+"\t"+tag+"\n") #switch to _RARE_
                continue
            else:
                output_.append(word+"\t"+tag+"\n")
                continue

    with open(outfile, "w") as wp:
        wp.writelines(output_)

if __name__ == "__main__":

    replace_words("gene.train","gene_rare.train", get_count(read_file("gene.train")))
