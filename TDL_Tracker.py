RED = "\033[31m"     # HIGH
YELLOW = "\033[33m"  # MEDIUM
GREEN = "\033[32m"   # LOW
RESET = "\033[0m"

colors = {
    "HIGH": RED,
    "MEDIUM": YELLOW,
    "LOW": GREEN
}

tasks = {
    "HIGH": [],
    "MEDIUM": [],
    "LOW": []
}

while True:
    task = input("Enter a task (or 'done' to finish): ")
    if task.lower() == "done":
        break

    priority = input("Priority (HIGH, MEDIUM, LOW): ").upper()
    if priority not in tasks:
        print("Invbalid priority, defaulting to MEDIUM.")
        priority = "MEDIUM"

    tasks[priority].append(task)

for priority, task_list in tasks.items():
    print(colors[priority] + priority + RESET, "tasks:")
    for t in task_list:
        print(" -", t)
    print()

most_tasks = None
highest_count = 0

for priority, tank_list in tasks.items():
    count = len(task_list)
    print(priority, "has", count, "tasks")
    if count > highest_count:
        highest_count = count
        most_tasks = priority

print("Priority with most tasks:", most_tasks, "with", highest_count)