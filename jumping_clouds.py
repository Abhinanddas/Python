def find_path(clouds):
    
    path =[]
    length = len(clouds)
    
    for index, x in enumerate(clouds):
        
        if index == 0:
            path.append(x)
        
        if index and index not in path:
            continue
        
        
        if  (index +2) < length and clouds[index+2] ==0:
            path.append(index +2) 
            continue
        
        if (index+1 < length) and clouds[index+1] ==0:
            path.append(index+1)
            continue
    
    return len(path) - 1

print(find_path([0,1,0,0,0,1,0]))