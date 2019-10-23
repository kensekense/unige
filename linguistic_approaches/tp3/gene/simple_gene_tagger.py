#Ning
#14 October 2019
#Linguistics TP3

def simple_gene_tagger(counts_file, dev_file):

    emissions_gene = {}
    emissions_nogene = {}
    counts = {}

    with open(counts_file, "r") as fp:
        for line in fp:
            segment = line.split()

            if(segment[1]=="WORDTAG"): #doing WORDTAG section

                if(segment[2] == "GENE"):
                    emissions_gene[segment[3]] = float(segment[0]) #hash the word and the tag counts

                elif(segment[2] == "NOGENE"):
                    emissions_nogene[segment[3]] = float(segment[0])

            elif(segment[1]=="1-GRAM"): #doing 1-GRAM section
                counts[segment[2]] = float(segment[0])

            else: #we're not doing anything beyond 1-GRAM
                break

    #read dev file and tag
    tags = []
    with open(dev_file, "r") as devfp:

        for line in devfp:
            line = line.split("\n")
            line = line[0]
            if(len(line)>0): #not an empty line

                #do the emission probability here
                if(line in emissions_gene and line in emissions_nogene): #has both tags, find more likely
                    gene_prob = emissions_gene[line]/counts["GENE"]
                    nogene_prob = emissions_nogene[line]/counts["NOGENE"]

                    choice = max(gene_prob, nogene_prob)

                    if(choice == gene_prob):
                        tags.append(line+" "+"GENE"+"\n")
                    elif(choice == nogene_prob):
                        tags.append(line+" "+"NOGENE"+"\n")

                elif(line in emissions_gene):
                    gene_prob = emissions_gene[line]/counts["GENE"]
                    nogene_prob = 0/counts["NOGENE"]

                    choice = max(gene_prob, nogene_prob)

                    if(choice == gene_prob):
                        tags.append(line+" "+"GENE"+"\n")
                    elif(choice == nogene_prob):
                        tags.append(line+" "+"NOGENE"+"\n")

                elif(line in emissions_nogene):
                    gene_prob = 0/counts["GENE"]
                    nogene_prob = emissions_nogene[line]/counts["NOGENE"]

                    choice = max(gene_prob, nogene_prob)

                    if(choice == gene_prob):
                        tags.append(line+" "+"GENE"+"\n")
                    elif(choice == nogene_prob):
                        tags.append(line+" "+"NOGENE"+"\n")

                else:#_RARE_ ALWAYS TAKES GENE
                    gene_prob = emissions_gene["_RARE_"]/counts["GENE"]
                    nogene_prob = emissions_nogene["_RARE_"]/counts["NOGENE"]

                    choice = max(gene_prob, nogene_prob)

                    if(choice == gene_prob):
                        tags.append(line+" "+"GENE"+"\n")
                    elif(choice == nogene_prob):
                        tags.append(line+" "+"NOGENE"+"\n")

            else:
                tags.append("\n") #otherwise an empty line

    with open("gene.test.p1.out", "w") as devp1out:
        devp1out.writelines(tags)

if __name__ == "__main__":
    simple_gene_tagger("gene_rare.counts", "gene.test")
