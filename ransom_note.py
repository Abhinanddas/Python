#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    
    word_map ={}
    word_count = 0
    
    for word in note:
        if word in word_map:
            word_map[word] +=1
        else:
            word_map[word] =1
            word_count +=1
    
    for word in magazine:
        
        if word in word_map:
            word_map[word] -=1
            if word_map[word] == 0:
                word_count -=1
        if word_count ==0:
            return True
    
    return False

magazine = ['give', 'me', 'one', 'grand', 'today', 'night']

note = ['give', 'one', 'grand', 'today']

 
print(checkMagazine(magazine, note))
