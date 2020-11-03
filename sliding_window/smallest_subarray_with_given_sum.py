### leetcode 209

def smallest_subarray_with_given_sum(sum, array):
    left = right = 0
    min_numbers = float("inf")

    cur_window = 0
    while right < len(array) :
        cur_window += array[right]

        while cur_window >= sum:
            min_numbers = min(min_numbers,right -left+1)
            cur_window -= array[left]
            left+=1
        right +=1

    return min_numbers

print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))