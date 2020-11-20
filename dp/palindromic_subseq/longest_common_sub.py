def longest_comon_subseq_rec(string):

    if not string:
        return 0
    if len(string) == 1:
        return 1
    if string[0] != string[-1]:
        return max(longest_comon_subseq_rec(string[1:]), longest_comon_subseq_rec(string[:-1]))

    return 2 + longest_comon_subseq_rec(string[1:-1])


def main():
    print("recursive ans", longest_comon_subseq_rec("abdbca"))
    print("recursive ans", longest_comon_subseq_rec("cddpd"))
    print("recursive ans", longest_comon_subseq_rec("pqr"))


main()

print("##################################################################")


def longest_comon_subseq(string):
    pass


def main():
    print("recursive ans", longest_comon_subseq("abdbca"))
    print("recursive ans", longest_comon_subseq("cddpd"))
    print("recursive ans", longest_comon_subseq("pqr"))


main()
