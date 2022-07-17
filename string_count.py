# There is a string, , of lowercase English letters that is repeated infinitely many times.
# Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

import math


def count_character(string):
    
    count = 0
    
    for char in string:
        if char=='a':
            count+=1
    
    return count


def count_string(string, n):
    
    count_of_a =0
    iteration = math.floor(n/len(string))
    
    if iteration:
        count_of_a = count_character(string) * iteration
        
    slice_count = n%len(string)
    
    count_of_a += count_character(string[0:slice_count])
    
    return count_of_a
        
print(count_string('a',1000000000000))
