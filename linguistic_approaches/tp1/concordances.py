#Ning
#21 Sep
#linguistics tp1

class Concordancer():

    def __init__(self, filename):
        self.raw_text = []
        self.concordances = {}
        with open(filename, "r") as file:
            for line in file:
                line = line.lower()
                self.raw_text.append(line.split()) #insert lines into array, separated by words

    def display(self, key_word):
        """
        Question did not specify how much context to give, so implementation defaults
        at most 5 words for every line.
        """
        for line in self.raw_text:
            i = (x for x, y in enumerate(line) if y == key_word) #this is a generator to find all indexes of matches
            for word in line:
                if word == key_word:
                    loc = next(i) #this gives you the next matched index
                    print(line[loc-5:loc],"\t", line[loc], "\t", line[loc+1:loc+6]) #gives you 5 words before and after the match

if __name__ == "__main__":
    FILENAME = "austen.txt"
    a = Concordancer(FILENAME)
    a.display("emma") #i chose to test emma because these words occur in the beginning, easier to check manually
    a.display("but") #i chose to test but because i remember it appeared more than a couple of times from an_index.py
