def long_com_substring(s1, s2):
    return helper(s1, s2, 0)


def helper(s1, s2, count):
    if not s1 or not s2:
        return count

    if s1[0] == s2[0]:
        count = helper(s1[1:], s2[1:], count+1)

    return max(count, max(helper(s1[1:], s2, 0), helper(s1, s2[1:], 0)))


def main():
    print(long_com_substring("abdca", "cbda"))
    print(long_com_substring("passport", "ppsspt"))


main()
