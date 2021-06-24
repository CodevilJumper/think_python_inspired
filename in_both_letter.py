# Function is checking if letter from word1 is present in word2 and prints it is True

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('apples', 'oranges')