# def binary_search(input_array, value):
#     arr_length = len(input_array)
#     lower =0
#     top = arr_length -1

#     while (lower<=top):
        
#         mid =(lower+top)//2
#         if input_array[mid] == value:
#             return mid
             
#         if input_array[mid] < value:
#             lower = mid + 1
#         else:
#             top = mid -1
#     return -1        
       
def binary_search(input_array,value, left, right):
    
    mid  = (left + right)//2
    if left > right:
        return -1
    
    if input_array[mid] == value:
        return mid
    
    if input_array[mid] > value:
        return binary_search(input_array, value, left, mid-1)
    else:
        return binary_search(input_array, value, mid+1, right)
                 

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1, 0, len(test_list)))
print(binary_search(test_list, test_val2, 0, len(test_list)))
