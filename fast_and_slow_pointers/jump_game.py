def circular_array_loop_exists(arr):

    max_so_far = 0

    for i in range(len(arr)):
        if max_so_far < i:
            return False

        max_so_far = max(max_so_far, arr[i]+i)
    return True


print(circular_array_loop_exists([1, 2, -1, 2, 2]))
print(circular_array_loop_exists([2, 2, -1, 2]))
print(circular_array_loop_exists([2, 1, -1, -2]))
