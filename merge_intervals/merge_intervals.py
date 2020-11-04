intervals = [[1,4], [2,5], [7,9]]

intervals1 = [[6,7], [2,4], [5,9]]

intervals2 = [[1,4], [2,6], [3,5]]


def merge_intervals(intervals):

    if not intervals:
        return []
        
    intervals.sort(key=lambda x: x[0])
    res = []

    last_interval = intervals[0]
    for cur_interval in intervals[1:]:
        if last_interval[1] >= cur_interval[0]:
            last_interval[1] = max(cur_interval[1], last_interval[1])
        else:
            res.append(last_interval)
            last_interval = cur_interval

    res.append(last_interval)
    return res


print(merge_intervals(intervals))
print(merge_intervals(intervals1))
print(merge_intervals(intervals2))