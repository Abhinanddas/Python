def sherlockAndAnagrams(string):
    
    string_subset = {}
    
    n = len(string)
    
    for i in range(n):
        for j in range(i,n):
            cur = string[i:j +1]
            cur = ''.join(sorted(cur))
            string_subset[cur] = string_subset.get(cur, 0) + 1
    
    
    anagram_count = 0
    for word in string_subset:
        
        v = string_subset[word]
        anagram_count += (v * (v-1))//2
    
    print(anagram_count)
    
    
    
sherlockAndAnagrams('abba')   
sherlockAndAnagrams('kkkk')   

# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

# Example

# The list of all anagrammatic pairs is  at positions  respectively.

# Function Description

# Complete the function sherlockAndAnagrams in the editor below.

# sherlockAndAnagrams has the following parameter(s):

# string s: a string
# Returns

# int: the number of unordered anagrammatic pairs of substrings in 
# Input Format

# The first line contains an integer , the number of queries.
# Each of the next  lines contains a string  to analyze.

# Constraints



#  contains only lowercase letters in the range ascii[a-z].

# Sample Input 0

# 2
# abba
# abcd
# Sample Output 0

# 4
# 0
# Explanation 0

# The list of all anagrammatic pairs is  and  at positions  and  respectively.

# No anagrammatic pairs exist in the second query as no character repeats.

# Sample Input 1

# 2
# ifailuhkqq
# kkkk
# Sample Output 1

# 3
# 10
# Explanation 1

# For the first query, we have anagram pairs  and  at positions  and  respectively.

# For the second query:
# There are 6 anagrams of the form  at positions  and .
# There are 3 anagrams of the form  at positions  and .
# There is 1 anagram of the form  at position .

# Sample Input 2

# 1
# cdcd
# Sample Output 2

# 5
# Explanation 2

# There are two anagrammatic pairs of length :  and .
# There are three anagrammatic pairs of length :  at positions  respectively.