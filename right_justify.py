def right_justify(s):
    """
    INPUT: string
    :return: This function returns the text right justified to the right in column 70
    :rtype: string
    """

    # calculate how many spaces before the text based on the length of the text.
    # and adds text at the end
    print(' ' * (70 - len(s)) + s)

right_justify('monty python')