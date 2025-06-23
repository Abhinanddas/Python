def bubble_sort(arr):
    length = len(arr)
    swapped = False
    swap_count = 0
    for i in range(length -1):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                swap_count +=1
        if not swapped:
            return arr
    print("Swap Count", swap_count)
    return arr                
    
    
    
arr =[100,90,80,70,60,50,40,30,20,10,0]
print(bubble_sort(arr))
arr =[8,22,7,9,31,19,5,13]
print(bubble_sort(arr))