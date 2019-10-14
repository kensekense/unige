#Ning
#14 October 2019
#Linguistics TP3

def simple_gene_tagger(counts_file, dev_file):

    emissions_gene = {}
    emissions_nogene = {}
    counts_gene = {}
    counts_nogene = {}

    with open(counts_file, "r") as fp:
        for line in fp:
            segment = line.split()

            if(segment[1]=="WORDTAG"): #doing WORDTAG section
                if(segment[3] == "GENE\n" and not(segment[2] in emissions_gene)):
                    emissions_gene[segment[2]] = segment[0] #store word with emission count
                elif(segment[3] == "NOGENE\n" and not(segment[2] in emissions_nogene)):
                    emissions_nogene[segment[2]] = segment[0] #store word with emission count

            elif(segment[1]=="1-GRAM"): #doing 1-GRAM section
                if(segment[3] == "GENE\n" and not(segment[2] in counts_gene)):
                    counts_gene[segment[2]] = segment[0]
                elif(segment[3] == "NOGENE\n" and not(segment[2] in counts_nogene)):
                    counts_nogene[segment[2]] = segment[0]

            else: #we're not doing anything beyond 1-GRAM
                break

    #read the dev file and tag here
