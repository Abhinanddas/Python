def fetch_min_and_max(arr):
    
    largest = arr[0]
    smallest = arr[0]
    sum = 0
    for x in arr:
        if x > largest:
            largest =x
        
        if x < smallest:
            smallest = x
        
        sum+=x
    
    print("{}  {}".format(sum-smallest, sum-largest))
fetch_min_and_max([1,3,5,7,9])
