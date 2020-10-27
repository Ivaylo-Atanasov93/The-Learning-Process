class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        completed_task = [task for task in self.tasks if task.name == task_name]
        if len(completed_task) == 0:
            return f"Could not find task with the name {task_name}"
        completed_task[0].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        for task in self.tasks:
            if task.completed:
                cleared_tasks += 1
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        details = f'Section {self.name}:\n'
        for task in self.tasks:
            details += f'{task.details()}\n'
        return details



# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())

# task = Task("Tst", "27.04.2020")
# task.add_comment("pay the bills")
# message = task.edit_comment(1, "finish my homework")
# expected = "Cannot find comment."
# print(message)