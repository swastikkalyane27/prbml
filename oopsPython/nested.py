class Human:
    def __init__(self):
        self.name='swasik'
        self.head=self.Head()
    def display(self):
        print("hello am human")
        self.head.talk()
        self.head.brain.think()
    class Head:
        def __init__(self):
            self.brain=self.Brain()
        def talk(self):
            print('i can talk____')
        class Brain:
            def think(self):
                print('i can think____')
h=Human()
h.display()