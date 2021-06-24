### Recursion example for counting down to Blastoff in seconds

import time

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

countdown(25)