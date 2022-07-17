def find_max_candles(arr):
    
    max = 0
    candle_count = {}
    
    for x in arr:
        if x > max:
            max = x
            
        if x in candle_count:
            candle_count[x] +=1
        else:
            candle_count[x] = 1
            
    return candle_count[max]


print(find_max_candles([3,2,1,3]))
print(find_max_candles([4,4,1,3]))