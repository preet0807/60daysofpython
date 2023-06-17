#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
       for item in s.split():
            if item.isalpha():
                capitalized_string= item.capitalize()
                s.replace(item, capitalized_string)

                
       return (s)
    
   

if __name__ == '__main__':
    

    s = input()

    result = solve(s)
    print (result)



