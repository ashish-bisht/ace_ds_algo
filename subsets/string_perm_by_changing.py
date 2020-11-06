def find_letter_case_string_permutations(strng):
    permutations = []
    length = len(strng)
    helper(strng, length, '', '', permutations)
    return permutations


def helper(strng, length, cur, cur1, permutations):
    if len(cur) == length:
        permutations.append(cur)
        permutations.append(cur1)
        return

    for i in range(len(strng)):
        helper(strng[i:]+strng[i+1:], length, cur+strng[i],
               cur1+(strng[i]).capitalize(), permutations)


print("String permutations are: " +
      str(find_letter_case_string_permutations("ad52")))
print("String permutations are: " +
      str(find_letter_case_string_permutations("ab7c")))
