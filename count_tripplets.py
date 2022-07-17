from collections import Counter

def count_triplets(arr, ratio):
    
    triplet_count = 0
    
    map1 = {}
    map2 ={}
    
    for num in arr:
        
        if num in map2:
            triplet_count += map2[num]
            
        if num in map1:
            map2[num * ratio] = map2.get(num*ratio , 0) + map1[num]
            
        map1[num * ratio] = map1.get(num*ratio,0) +1
    print(triplet_count)
        
    
count_triplets([1,5,5,25,125], 5)
# count_triplets([1,3,9,9,27,81], 3)
# count_triplets([1,2,2,4], 2)

# arr =[1 for x in range(100)]
# count_triplets(arr,1)