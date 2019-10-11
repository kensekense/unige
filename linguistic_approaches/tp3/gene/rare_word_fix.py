#Ning
#10 October 2019
#Linguistics TP3

def read_file (filename):
    '''
    read the file and organize it's data into a list
    '''
    words = []
    while open(filename, "r") as fp:
        if(len(fp.readline()) > 0):
            (word, tag) = fp.readline().split() #stores the word separately from tag
            words.append(word)

    return words

def get_count (words):
    '''
    get a count of each word in the list of words
    '''
    counts = [0]*len(words)

    for word in words:
        for i in range(0, len(words)): #search for every word how many times it appears
            if(word == words[i]):
                counts[i] += 1

    return counts

def replace_words (counts):
    '''
    replace the word in the doc with _RARE_ if count is < 5
    '''
    
