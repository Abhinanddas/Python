


def calculate_valley(arr):
    
    count , iteration, valley, mountain =0, 0, 0,0
    direction = None
    for x in arr:
        
        if count ==0:
            direction = None
            
        if count > 0:
            direction = True
            
        if count < 0:
            direction = False
        
        
        if x == 'U':
            count = count+1
            
        if x=='D':
            count =count-1
    
        if iteration != 0:
            if count ==0:
                if direction:
                    mountain += 1
                
                if not direction:
                    valley +=1      
        iteration +=1
    return valley, mountain
    
    
arr= 'UDDDUDUU'
print(calculate_valley(arr))
print(calculate_valley('DDUUUUDD'))
            