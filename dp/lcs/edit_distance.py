def edit_distance(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    if s1[0] == s2[0]:
        return edit_distance(s1[1:], s2[1:])
    # we are inserting to our str1...
    insert = 1+edit_distance(s1, s2[1:])
    # we are deleting from our str2
    delete = 1+edit_distance(s1[1:], s2)
    # we are replacing
    replace = 1+edit_distance(s1[1:], s2[1:])

    return min(insert, delete, replace)


print(edit_distance("bat", "but"))
print(edit_distance("abdca", "cbda"))
print(edit_distance("passpot", "ppsspqrt"))
