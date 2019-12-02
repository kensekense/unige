from composes.utils import io_utils
from composes.similarity.cos import CosSimilarity
import math
import sys

#kneighbours.py code
#load a space
my_space = io_utils.load("../spaces/wikipedia.pkl") #note the change in file reference here

#print(my_space.get_neighbours(sys.argv[2], int(sys.argv[3]), CosSimilarity()))
neighborsList = my_space.get_neighbours(sys.argv[2], int(100), CosSimilarity())

#run for each neighbors??

#!! hyponymy.py code
DM=open(sys.argv[1],"r",encoding='utf-8')
DM_lines=DM.readlines()
DM.close()

dic={}

for l in DM_lines:
	pair=l.rstrip("\n").split('\t')
	#print(pair[0],"::",pair[1:])
	dic[pair[0]]=pair[1:]


h1=dic[sys.argv[2]]

vals = []

for word in neighborsList:

    h2=dic[word[0]]

    iter=0

    sum_mins=0
    sum_h1=0
    sum_h2=0

    for weight1 in h1:
    	#print(sys.argv[2],w)
    	weight2=h2[iter]
    	sum_mins+=min(float(weight1),float(weight2))
    	sum_h1+=float(weight1)
    	sum_h2+=float(weight2)
    	iter+=1

    clarkeDE=sum_mins/sum_h1
    clarkeDEinv=sum_mins/sum_h2

    invCL=math.sqrt(clarkeDE*(1-clarkeDEinv))

    vals.append((word[0],clarkeDE, invCL, word[1])) #append to list

for item in vals:
    if (abs(item[2]-0.4)) < 0.2 and abs(item[1]-0.6) < 0.2 and item[3] > 0.778:
        print(item)
