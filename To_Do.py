class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark(self):
        self.done = True

    def status(self):
        if self.done:
            print(f"[X] {self.title}")
        else:
            print(f"[ ] {self.title}")

tasks = []

while True:
    title = input("Write your task today: ")
    new_task = Task(title)
    tasks.append(new_task)

    add_task = input("do you want another task? (yes/no) ")
    if add_task != "yes":
        break

for t in tasks:
    t.status()

def done():
    for t in tasks:
        ask_done = input(f"Did you do this task: {t.title}? (yes/no) ")
        if ask_done == "yes":
            t.mark()
        t.status()

done()

import json

def save_tasks():
    data = []
    for t in tasks:
        data.append({"title": t.title, "done": t.done})

    with open("tasks.json", "w") as file:
        json.dump(data, file)