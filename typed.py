import time
import sys

def type(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

type("This sentence is typed.")