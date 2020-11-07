# ek tarah se 23 pointer

def dutch_flag_sort(arr):
    left, right = 0, len(arr)-1
    zero = 0

    while left <= right:
        if arr[left] == 2:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1

        elif arr[left] == 0:
            arr[zero], arr[left] = arr[left], arr[zero]
            left += 1
            zero += 1

        else:
            left += 1

    return arr


print(dutch_flag_sort([1, 0, 2, 1, 0]))
print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
