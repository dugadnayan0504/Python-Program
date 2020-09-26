import math
import os
import random
import re
import sys


#def diagonalDifference(arr):

if __name__ == '__main__':
    
    
    n = int(input("Please Enter Number:").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

   
    a = sum(arr[i][i]  for i in range(n) ) 
    print(str(a))



    