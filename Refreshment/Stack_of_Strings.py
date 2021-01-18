class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        if isinstance(item, str):
            self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return ', '.join(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(self.data[::-1])}]'
