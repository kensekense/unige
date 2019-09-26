#Ning
#21 Sep
#linguistics tp1

def count_freq (text):
    lower = [i.lower() for i in text.split()] #convert text into lower case
    freq = {}
    for item in lower: #hash the values into a dictionary
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return sorted(freq.items()) #return the sorted dictionary by key

if __name__ == "__main__":
    text = "Le poids politique de Lorient s’affirme à partir de la Révolution française et la ville gagne un rôle administratif à partir du premier Empire Les activités commerciales restent alors en retrait dans la première moitié du 19e siècle en raison des conflits fréquents mais les activités militaires gagnent en importance"
    for item in count_freq(text): #print the dictionary so it looks nice
        print(item)
