def min_del_ins(s1, s2):
    ans = 0
    common_seq = helper(s1, s2)

    ans = len(s1) - common_seq + len(s2) - common_seq
    return ans


def helper(s1, s2):
    if not s1 or not s2:
        return 0

    if s1[0] == s2[0]:
        return 1 + helper(s1[1:], s2[1:])

    return max(helper(s1[1:], s2), helper(s1, s2[1:]))


def main():
    print(min_del_ins("abc", "fbc"))
    print(min_del_ins("abdca", "cbda"))
    print(min_del_ins("passport", "ppsspt"))


main()
