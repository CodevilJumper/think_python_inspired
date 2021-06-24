def print_key_value(dict):
    """
    This function takes a dictionary and prints the key and a value for the key
    :INPUT type: dictionary
    :type dict
    :OUTPUT return: key-value pair
    :rtype: pair of values
    """
    for item in dict:
        print(item, dict[item])

d = {'a':'one','s':'two','d':'tree'}
print_key_value(d)
