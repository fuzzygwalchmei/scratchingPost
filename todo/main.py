class todo_item():
    def __init__(self, id, subject, note):
        self.id = id
        self.subject = subject
        self.note = note
            
    def __str__(self):
        return f"""ID: {self.id}
        Subject: {self.subject}
        Note: {self.note}"""

    
class todo_list():
    def __init__(self):
        self.id = 0
        self.store = []

    def add(self, subject, note):
        self.store.append(todo_item(self.id, subject, note))
        self.id += 1
    
    def list_all(self):
        for item in self.store:
            print(item)

    def save(self):
        filename = 'Todo_list.txt'
        with open(filename, 'w') as f:
            for item in self.store:
                f.writelines(f'{item.id},{item.subject},{item.note}\n')

    def load(self):
        filename = 'Todo_list.txt'
        with open(filename, 'r') as f:
            info = f.readlines()
        
        for item in info:
            id, subject, note = item.split(',')
            self.store.append(todo_item(id, subject, note))