
students = [561, 458, 389, 327, 248, 189, 137, 98]

max_parallel = 0
for i in range(len(students)):
    if students[i] > students[max_parallel]:
        max_parallel = i

if max_parallel > 120:
    print(f"Номер самой старшей параллели: {max_parallel}")
