def search_triplets(arr):
    arr.sort()
    tripplets = []

    for i in range(len(arr)):
        if i > 0 and arr[i-1] == arr[i]:  # dont entertain duplicates....
            continue
        helper(arr, i+1, -arr[i], tripplets)
    return tripplets


def helper(arr, left, sum_to_find, tripplets):
    right = len(arr)-1

    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == sum_to_find:
            tripplets.append([-sum_to_find, arr[left], arr[right]])
            # agar next bhe same ho to
            while left < right and arr[left] == arr[left+1]:
                left += 1
            while left < right and arr[right] == arr[right-1]:
                right -= 1

            left += 1  # next se aage
            right -= 1

        elif cur_sum < sum_to_find:
            left += 1

        else:
            right -= 1


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))
