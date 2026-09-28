def create_task(name,priority,completed_text):
    completed = completed_text == "是"
    task={
        "name":name,
        "priority":priority,
        "completed":completed
    }

    return task

def count_completed(tasks):
    count = 0
    for task in tasks:
        if task["completed"]:
            count += 1

    return count