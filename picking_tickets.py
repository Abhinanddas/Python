def quicksort(array):
    
    if len(array) < 2:
        return array
    
    left =0
    pivot =  len(array)-1
    
    while(left < pivot):
        if array[left] > array[pivot]:
            
            array[left], array[pivot -1] = array[pivot -1],array[left]
            array[pivot-1], array[pivot] = array[pivot], array[pivot -1]
            pivot -= 1
        else:
            left +=1
    l = quicksort(array[:pivot])
    r = quicksort(array[pivot+1:])
    
    return l  + [array[pivot]] + r    
    
def make_hash_map(arr):
    
    hash_map ={} 
    
    for x in arr:
        if x in hash_map:
            hash_map[x] +=1
        else:
            hash_map[x] = 1
    return hash_map
    
def picking_tickets(arr):
        
    arr = quicksort(arr)
    
    largest_sub_sequence =0    
    index =0
    for x in arr:
        sub_sequence = [x]
        largest_num_in_sequence = x
        for j in range(len(arr)):
            
            if j == index:
                continue
               
            diff =  arr[j] - largest_num_in_sequence
            if diff in [0,1]:
                sub_sequence.append(arr[j])
                largest_num_in_sequence = arr[j]
            else:
                continue
        
        index +=1
        
        if len(sub_sequence) > largest_sub_sequence:
            largest_sub_sequence = len(sub_sequence)
    
    return largest_sub_sequence
                
        
    
    
print(picking_tickets([4,13,2,3]))
print(picking_tickets([8,5,4,8,4]))
print(picking_tickets([1, 5, 2, 5, 5, 2, 6, 3, 5, 3]))
