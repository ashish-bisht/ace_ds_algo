def longest_common_subseq(s1, s2):
    if not s1 or not s2:
        return 0

    if s1[0] == s2[0]:
        return 1 + longest_common_subseq(s1[1:], s2[1:])

    return max(longest_common_subseq(s1[1:], s2), longest_common_subseq(s1, s2[1:]))


def main():
    print(longest_common_subseq("abdca", "cbda"))
    print(longest_common_subseq("passport", "ppsspt"))


main()
