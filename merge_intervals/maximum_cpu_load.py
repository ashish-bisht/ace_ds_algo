def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x[0])
    merged_jobs = []

    last_job = jobs[0]

    for cur_job in jobs[1:]:
        if last_job[1] >= cur_job[0]:
            last_job[1] = max(last_job[1], cur_job[1])
            last_job[2] += cur_job[2]
        else:
            merged_jobs.append(last_job)
            last_job = cur_job
    merged_jobs.append(last_job)

    merged_jobs.sort(key=lambda x: x[2])
    return merged_jobs[-1][2]




print("Maximum CPU load at any time: " + str(find_max_cpu_load([[1,4,3], [2,5,4], [7,9,6]])))
print("Maximum CPU load at any time: " + str(find_max_cpu_load([[6,7,10], [2,4,11], [8,12,15]])))
print("Maximum CPU load at any time: " + str(find_max_cpu_load([[1,4,2], [2,4,1], [3,6,5]])))
