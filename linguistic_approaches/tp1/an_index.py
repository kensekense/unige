#Ning
#21 Sep
#linguistics tp1

def read_file_and_hash(filename, freq, version=1):
    '''
    Takes a filename, and a dictionary and outputs a list of tuple (key, values).
    Version allows you to allow/disallow keeping track of multiple appearances in a given line.
    '''
    line_num = 1
    with open(filename, 'r') as file:
        for line in file:
            if(not version):
                freq = hash_words(line, freq, line_num) #update the freq dictionary per line
            else:
                freq = hash_words_2(line, freq, line_num)
            line_num += 1 #increment the line number
    return sorted(freq.items()) #return sorted dictionary

def hash_words(text, freq, line_number):
    """
    NOTE: The question did not specify what happens if a word appears multiple times in a given line.
    This version implements index outputs that reflect the number of times the word appears in each line.
    """
    lower = [i.lower() for i in text.split()] #apply lowercase to each word in text given
    for item in lower: #hashes word into the freq dictionary
        if item in freq:
            freq[item].append(line_number) #refer to NOTE
        else:
            freq[item] = [line_number]

    return freq

def hash_words_2(text, freq, line_number):
    """
    NOTE: The question did not specify what happens if a word appears multiple times in a given line.
    This version implements index outputs that only give you the line in which it occurs with no repeats.
    This is the default version used in read_file_and_hash
    """
    lower = [i.lower() for i in text.split()] #apply lowercase to each word in text given
    for item in lower: #hashes word into the freq dictionary
        if item in freq:
            freq[item].add(line_number) #refer to NOTE
        else:
            freq[item] = {line_number}

    return freq

if __name__ == "__main__":
    FILENAME = "austen.txt" #austen.txt has to be in the same directory
    freq_dict = {}
    result = read_file_and_hash(FILENAME, freq_dict) #note here we're using default version
    for item in result: #print the dictionary so it looks nice
        print(item)
