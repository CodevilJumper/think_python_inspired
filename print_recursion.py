def print_n(s, n):
    """
    :param s: object (str, int, float)
    :type s: object (str, int, float)
    :param n: how many times we can print an object
    :type n: int
    :return: object printed n-times
    :rtype: recursion
    """
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('printing', 3)