class todo_item():
    def __init__(self, id, subject, note):
        self.id = id
        self.subject = subject
        self.note = note
            
    def __str__(self):
        return f"""ID: {self.id}\n 
        Subject: {self.subject} \n 
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

