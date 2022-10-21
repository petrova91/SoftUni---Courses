jobs = [int(x) for x in input().split(", ")]
index = int(input())

cycles = 0
jobs_copy = jobs.copy()

index_is_found = False
for _ in range(len(jobs)):
    job = min(jobs_copy)
    for index_job, clock_cycle in enumerate(jobs):
        if clock_cycle == job:
            cycles += clock_cycle
            jobs_copy.remove(job)
            if index_job == index:
                index_is_found = True
                break
    if index_is_found:
        break

print(cycles)