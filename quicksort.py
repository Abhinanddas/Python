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

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
