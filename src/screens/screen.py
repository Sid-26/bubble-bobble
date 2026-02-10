class Screen:
    def __init__(self, app):
        self.app = app
    
    def update(self, input_state):
        raise NotImplementedError
    
    def draw(self):
        raise NotImplementedError