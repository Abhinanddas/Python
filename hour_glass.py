def fetch_sum(hour_glass):
    sum =0
    
    for x in hour_glass:
        sum +=x
    
    return sum

def make_array(arr):
    
    hour_glass_arr =[]
    for hour_glass in arr:
        hour_glass = hour_glass.split(' ')
        hour_glass_arr.append(hour_glass)
    return hour_glass_arr

def fetch_max_hourglass(arr):
    
    arr = make_array(arr)
    row_limit =4
    column_limit =4
    iteration =0
    
    for row in range(row_limit):
        for column in range(column_limit):
            hour_glass=[
                int(arr[row][column]),
                int(arr[row][column+1]),
                int(arr[row][column+2]),
                int(arr[row+1][column+1]),
                int(arr[row+2][column]),
                int(arr[row+2][column+1]),
                int(arr[row+2][column+2]),
            ]
            
            hour_glass_sum = fetch_sum(hour_glass) 
            
            if not iteration:
                max_sum =hour_glass_sum
                iteration +=1
                
            if hour_glass_sum > max_sum:
                max_sum = hour_glass_sum
    return max_sum


arr = [
    '-9 -9 -9 1 1 1',
    '0 -9 0 4 3 2',
    '-9 -9 -9 1 2 3',
    '0 0 8 6 6 0',
    '0 0 0 -2 0 0',
    '0 0 1 2 4 0'
]

print(fetch_max_hourglass(arr))

arr =[
    '1 1 1 0 0 0',
    '0 1 0 0 0 0',
    '1 1 1 0 0 0',
    '0 0 2 4 4 0',
    '0 0 0 2 0 0',
    '0 0 1 2 4 0'
]
print(fetch_max_hourglass(arr))

arr = [
    '-1 -1 0 -9 -2 -2',
    '-2 -1 -6 -8 -2 -5',
    '-1 -1 -1 -2 -3 -4',
    '-1 -9 -2 -4 -4 -5',
    '-7 -3 -3 -2 -9 -9',
    '-1 -3 -1 -2 -4 -5'
]
print(fetch_max_hourglass(arr))
