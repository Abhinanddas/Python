# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.


def find_pair(array):
    
    pair_dict ={}
    
    for num in array:
        if num in pair_dict:
            pair_dict[num] +=  1
        else:
            pair_dict[num] =1
    
    pair_count = 0
    for key,value in pair_dict.items():
        pair_count += (value//2)
    return pair_count










array1=[1,2,1,2,1,3,2]
print(find_pair(array1))