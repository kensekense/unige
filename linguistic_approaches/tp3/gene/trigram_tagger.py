#Ning
#17 October 2019
#Linguistics TP3

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

    #open the devfile to tag the words
    


if __name__ == "__main__":
    trigram_tagger("gene_rare.counts", "gene.dev")
