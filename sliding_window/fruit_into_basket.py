def fruits_into_baskets(fruits,k):
    fruits_freq = {}
    max_fruits = 0
    left, right = 0,0

    while right < len(fruits):
        cur_right = fruits[right]

        if cur_right not in fruits_freq:
            fruits_freq[cur_right] = 0

        fruits_freq[cur_right] +=1

        while len(fruits_freq) > k:
            left_char = fruits[left]
            fruits_freq[left_char] -=1
            if fruits_freq[left_char] == 0:
                del fruits_freq[left_char]
            left +=1

        max_fruits = max(max_fruits, right-left+1)
        right +=1
    return max_fruits

    

print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'],2)))
print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'],2)))