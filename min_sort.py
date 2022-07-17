def hash(arr):
    
    hash = {}
    
    index =0
    for x in arr:
        hash[x] = index
        index +=1
    return hash
    
def min_swap(arr):
    
    temp = arr.copy()
    temp.sort()
    n = len(arr)
    count =0
    hash_map = hash(arr)
    for x in range(n):
        if arr[x] != temp[x]:
            count +=1
            swap_index = hash_map[temp[x]]
            arr[x],arr[swap_index] = arr[swap_index],arr[x]
            hash_map = hash(arr)
    
    print("Min swap", count)


arr = [1,5,4,3,2]
min_swap(arr)
min_swap([101, 758, 315, 730,472, 619, 460, 479])
