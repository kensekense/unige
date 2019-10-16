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
                if(segment[3] == "GENE"):
                    emissions_gene[segment[2]] = float(segment[0]) #hash the word and the tag counts

                elif(segment[3] == "NOGENE"):
                    emissions_nogene[segment[2]] = float(segment[0])

            elif(segment[1]=="1-GRAM"): #doing 1-GRAM section
                if segment[2] in counts:
                    counts[segment[2]] += float(segment[0])
                else:
                    counts[segment[2]] = float(segment[0])

            else: #we're not doing anything beyond 1-GRAM
                break

    #read dev file and tag
    tags = []
    with open(dev_file, "r") as devfp:

        for line in devfp:
            line = line.split("\n")
            line = line[0]
            if(len(line)>0):

                if(line in emissions_gene and line in emissions_nogene): #in both, i.e: "a"
                    prob_gene = emissions_gene[line]/counts[line]
                    prob_nogene = emissions_nogene[line]/counts[line]
                    if(max(prob_gene, prob_nogene) == prob_gene):
                        tags.append(line + " " + "GENE"+"\n") #proper tag
                    else:
                        tags.append(line + " " + "NOGENE"+"\n") #reverses the tag

                elif(line in emissions_gene):
                    tags.append(line + " " + "GENE"+"\n") #proper tag

                elif(line in emissions_nogene):
                    tags.append(line + " " + "NOGENE"+"\n") #proper tag

                else: #_RARE_ word (tm)
                    #always output max and NOGENE > GENE for _RARE_
                    tags.append(line + " " + "NOGENE"+"\n")
            else:
                tags.append("\n")

    with open("gene.dev.p1.out", "w") as devp1out:
        devp1out.writelines(tags)

if __name__ == "__main__":
    simple_gene_tagger("gene_rare.counts", "gene.dev")
