#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    def isSquare(n):
        a = math.sqrt(n)
        if (a-int(a)>0):        
            return False
        elif (a-int(a)==0):
            return True
        else:
            return RuntimeError
#--------------------------------------------------            
    counter = 0
    for x in range(a,b+1):
        if(isSquare(x)==True):
            counter = counter + 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
