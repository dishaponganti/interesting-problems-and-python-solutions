# Python 3.6.4 |Anaconda custom (64-bit)| (default, Mar 12 2018, 20:20:50) 
# Created by dponganti on 3/8/2019

import numpy as np

input = "[[)(]]"

class stackclass:
    stack = []
    top = 0
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, val):
        self.stack.append( val)

    def pop(self):
        if self.stacktop() == 0:
            val = self.stack[self.stacktop()]
            self.stack = []
        else:
            val = self.stack[self.stacktop()]
            self.stack = self.stack[:self.stacktop()]

        return val

    def empty(self):
        return len(self.stack)==0

    def stacktop(self):
        return len(self.stack) - 1



if __name__ == '__main__':

    s = stackclass()
    final_str = []

    for b in list(input):

        if b in ('(','{','['):
            s.push(b)

        elif b in (')','}',']'):
            popped = s.pop()
            top = s.top

            if (popped == '(' and b != ')' ) or (popped == '[' and b != ']') or (popped == '{' and b != '}'):
                print("Not balanced yaar")
                break

        else:
            print("Invalid input")
            break

    if s.empty():
        print("Balanced")
    else:
        print("Not balanced")

