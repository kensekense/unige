#Ning
#19 Sep
#linguistics tp1

text1 = ["This", "is", "a", "list", "of", "words", "that", "we", "are", "looking", "at"]
print(text1)
#sum([len(w) for w in text1]) should find the sum of the lengths of the words in text1, i.e: number of characters in our context
sum_len = sum([len(w) for w in text1])
print(sum_len) #confirms previous comment

mean_length = [sum_len/len(text1)] #mean length means number of characters/number of words
print(mean_length)

list_given = "she sells sea shells by the sea shore".split(" ") #for simplicity, it is equal to an array of words
words_sh = [w for w in list_given if w[0:2]=='sh'] #put the word in the list only if first letters are sh
words_4 = [w for w in list_given if len(w) > 4] #outputs words with 5 ch or more

#display
print(words_sh)
print(words_4)
