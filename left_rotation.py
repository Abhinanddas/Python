def left_rotate(arr, rotate):
    
    length = len(arr)
    
    shift_factor = rotate%length
    
    if shift_factor:
        arr = arr[shift_factor:] + arr[:shift_factor]
    
    return arr


arr = [1,2,3,4,5,6,7]

print(left_rotate(arr,3))