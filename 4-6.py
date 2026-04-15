RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
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
    task = input("Please enter a task (or 'done' to finish): " )
    if task.lower() == "done":
        break

    priority = input("Enter priority level (high, medium, low): ")
    if priority.lower() == "high":
        tasks["HIGH"].append(task)

    elif priority.lower() == "medium":
        tasks["MEDIUM"].append(task)

    elif priority.lower() == "low":
        tasks["LOW"].append(task)

with open("tasks.txt", 'w') as f:
    for priority, task_list in tasks.items():
        f.write(priority + ":\n")
        for t in task_list:
            f.write(" - " + t + "\n")
        f.write("\n")


for priority, task_list in tasks.items():
    color = colors.get(priority, RESET)
    print(color + priority + ":" + RESET)
    for t in task_list:
        print(" -", t)
    print()