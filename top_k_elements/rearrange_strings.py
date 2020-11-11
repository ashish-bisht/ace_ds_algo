import heapq
import collections


def rearrange_string(str):
    str_counter = collections.Counter(str)
    heap = []
    ans = ""

    for key, val in str_counter.items():
        heapq.heappush(heap, (-val, key))

    last_char = ''
    last_freq = 0
    while heap:
        freq, char = heapq.heappop(heap)

        ans += char

        if last_freq > 0:
            heapq.heappush(heap, (-last_freq, last_char))

        last_char = char
        last_freq = -(freq+1)
    return ans if len(ans) == len(str) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
