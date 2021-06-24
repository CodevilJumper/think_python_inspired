# Opens file and reads from the txt file and print words without letter "e"

file = open('words.txt')

for word in file:
    if 'e' not in word:
        print(word)


def words_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
        else:
            return True

print(words_no_e('california'))