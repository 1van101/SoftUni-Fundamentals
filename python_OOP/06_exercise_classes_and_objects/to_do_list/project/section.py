from test import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            task_to_be_completed = [x for x in self.tasks if x.name == task_name][0]
            task_to_be_completed.completed = True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        all_tasks = len(self.tasks)
        self.tasks = [x for x in self.tasks if x.completed == False]
        return f"Cleared {all_tasks - len(self.tasks)} tasks."

    def view_section(self):
        details_of_the_tasks = '\n'.join([x.details() for x in self.tasks])
        return f"Section {self.name}:\n{details_of_the_tasks}"

