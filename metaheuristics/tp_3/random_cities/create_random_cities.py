#Ning
import math
import random

def generate_five_TSPs(size):

    for j in range(1,6):

        lines = []

        for i in range(0,size):
            x = random.uniform(0,200)
            y = random.uniform(0,200)
            lines.append("c{0} {1} {2}\n".format(str(i), str(x), str(y)))


        #write to file
        write_filename = "cities_{0}_{1}.dat".format(str(size),str(j))
        with open(write_filename, "w") as wfile:
            wfile.writelines(lines)

if __name__ == "__main__":
    generate_five_TSPs(50)
    generate_five_TSPs(60)
    generate_five_TSPs(80)
    generate_five_TSPs(100)
