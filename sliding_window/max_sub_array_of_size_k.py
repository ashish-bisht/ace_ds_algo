def max_sub_array_of_size_k(k, arr):
    max_size = 0
    left = 0
    right = 0
    while right < k:
        max_size += arr[right]
        right +=1

    cur_window = max_size
    
    while right < len(arr):
        cur_window = cur_window - arr[left]+ arr[right]
        right +=1
        left +=1
        max_size = max(max_size, cur_window)
    return max_size


print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))