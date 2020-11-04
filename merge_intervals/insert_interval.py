def insert(intervals, new_interval):
    merged = []
    intervals.append(new_interval)

    intervals.sort(key=lambda x: x[0])

    last_interval = intervals[0]

    for cur_interval in intervals[1:]:
        if last_interval[1] >= cur_interval[0]:
            last_interval[1] = max(last_interval[1], cur_interval[1])
        else:
            merged.append(last_interval)
            last_interval = cur_interval

    merged.append(last_interval)
    return merged


print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))
