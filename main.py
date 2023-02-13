def maxEarnings(jobs, n):
    jobs.sort(key = lambda x: x[2], reverse = True)
    task = 0
    time = 0
    for i in range(n):
        if time <= int(jobs[i][0]):
            task += 1
            time = int(jobs[i][1])
    return [n-task, sum(j[2] for j in jobs[task:])]

n = int(input("Enter the number of Jobs: "))
jobs = []
for i in range(n):
    start_time = input("Enter job start time: ")
    end_time = input("Enter job end time: ")
    profit = int(input("Enter job profit: "))
    jobs.append([start_time, end_time, profit])

result = maxEarnings(jobs, n)
print("The number of tasks and earnings available for others:")
print("Task:", result[0])
print("Earnings:", result[1])
