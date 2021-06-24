# this function takes the string and traverse through each element of the strong (character) and checks if letter
# in dictionary. If not in dictionary it adds the letyter with value 1, otherwise increases the value by 1.

def dict_hist(s):
    d = dict()
    for character in s:
        if character not in d:
            d[character] = 1
        else:
            d[character] += 1
    return d

print(dict_hist('brontosaurus'))
