import heapq
def min_meeting_rooms(meetings):
      meetings.sort(key=lambda x: x[0])

      heap = []
      heap.append(meetings[0][1])

      for meeting in meetings[1:]:
            if meeting[0] >= heap[0]:
                  heapq.heapreplace(heap, meeting[1]) 
            else:
                  heapq.heappush(heap, meeting[1])


      return len(heap)


print("Minimum meeting rooms required: " +
      str(min_meeting_rooms([[1, 4], [2, 5], [7, 9]])))  # 2
print("Minimum meeting rooms required: " +
      str(min_meeting_rooms([[6, 7], [2, 4], [8, 12]])))  # 1
print("Minimum meeting rooms required: " +
      str(min_meeting_rooms([[1, 4], [2, 3], [3, 6]])))  # 2
print("Minimum meeting rooms required: " +
      str(min_meeting_rooms([[4, 5], [2, 3], [2, 4], [3, 5]])))  # 2


