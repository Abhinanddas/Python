# There is a string "s", of lowercase English letters that is repeated infinitely many times.
# Given an integer "n" , find and print the number of lett er a's in the first  letters of the infinite string.

# def count_string(string, n):
    
    
#     full_iteration = n //len(string)
#     reminder = n % len(string)
    
#     count_of_a = full_iteration * string.count('a') + string[0: reminder].count('a')
    
#     return count_of_a

count_string = lambda string,n: (n//len(string) * string.count('a') + string[0: n%len(string)].count('a'))
        
print(count_string('a',1000000000000))
print(count_string('abcac',10))
