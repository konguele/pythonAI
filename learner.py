import json

class Learner:
    def __init__(self):
        self.memory_file = 'memory.json'
        self.load_memory()
    
    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = {}
    
    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f)
    
    def learn_from_interaction(self, user_input, response):
        if user_input not in self.memory:
            self.memory[user_input] = response
        self.save_memory()

