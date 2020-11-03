def longest_substring_with_k_distinct(string, k):
    visited = {} ### setting the count of characters
    left = right = 0
    max_length = 0
    while  right < len(string):
        right_char = string[right]

        ### fill dict nice way
        if right_char not in visited:
            visited[right_char] = 0
        
        visited[right_char] +=1

        ## shrnking window
        while len(visited) > k:
            left_char = string[left]
            visited[left_char] -=1
            if visited[left_char] == 0:
                del visited[left_char]
            left +=1
       
        max_length = max(max_length, right-left+1)
        right +=1

    return max_length

print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
print("Length of the longest substring: " + str(longest_substring_with_k_distinct("i", 3)))