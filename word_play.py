# Opens file and reads and prints every word form the txt file in new line

fin = open('words.txt')

for line in fin:
    word = line.strip()
    print(word)


