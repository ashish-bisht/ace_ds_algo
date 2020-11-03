def no_repeat_substring(string):
    char_freq = {}
    left,right = 0,0
    max_string = 0

    while right < len(string):
        right_char = string[right]

        if right_char not in char_freq:
            char_freq[right_char] = 0
        else:
            left = char_freq[right_char]+1
        char_freq[right_char] = right

        max_string = max(max_string, right -left+1)
        right +=1

    return max_string



print("Length of the longest substring: " + str(no_repeat_substring("aabccbb")))
print("Length of the longest substring: " + str(no_repeat_substring("abbbb")))
print("Length of the longest substring: " + str(no_repeat_substring("abccde")))
