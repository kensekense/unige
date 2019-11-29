# Linguistics TP6
Ning Tientso
28 November 2019

# Building the Semantic Space
1. The kinds of words that end up at the top of the distribution are words the co-occur with "Queen" most often in the text, meaning that they appear next to Queen in the text. The nearest neighbors are words that are deemed to be most similar to Queen (measured in cosine similarity).
2. When you reduce the column/row size in the semantic space, the frequency values and nearest neighbors change. This is because you're utilizing less words in order to determine co-occurrences as well as similarity, and thus when disregarding words, co-occurrences and nearest neighbors will obviously be different.
3. The frequencies distribution of co-occurrences of the words will alter with window-size, since you have more words in your window that you are accounting for. The nearest neighbors should also see changes.
4. Without tagged data, you would most likely get co-occurrences with prepositions, since they are the connectors of nouns and phrases, making them the most likely to co-occur with nouns.

# Investigating a large semantic space
