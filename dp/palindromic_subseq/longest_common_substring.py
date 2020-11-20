def longest_comon_substring_rec(string):

    if not string:
        return 0
    if len(string) == 1:
        return 1
    if string[0] != string[-1]:
        return max(longest_comon_substring_rec(string[1:]), longest_comon_substring_rec(string[:-1]))

    return 2 + longest_comon_substring_rec(string[1:-1])


def main():
    print("recursive ans", longest_comon_substring_rec("abdbca"))
    print("recursive ans", longest_comon_substring_rec("cddpd"))
    print("recursive ans", longest_comon_substring_rec("pqr"))


main()

print("##################################################################")


def longest_comon_substring(string):
    pass


def main():
    print("recursive ans", longest_comon_substring("abdbca"))
    print("recursive ans", longest_comon_substring("cddpd"))
    print("recursive ans", longest_comon_substring("pqr"))


main()
