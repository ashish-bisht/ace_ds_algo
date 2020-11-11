import collections
import heapq


def sort_character_by_frequency(str):

    str_dict = collections.Counter(str)
    heap = []
    for key, val in str_dict.items():
        heapq.heappush(heap, (-val, key))

    final_string = ''

    while heap:
        val, char = heapq.heappop(heap)
        final_string = final_string + -(val) * char

    return final_string


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
