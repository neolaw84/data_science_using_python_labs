import random

random.seed(42)

class Car(object):
    def __init__(self, transmission:str="auto"):
        self.started=False
        self.transmission=transmission
    
    def drive(self):
        print ("driving car ... ")
        
    def start(self):
        print ("starting car ...")
        if random.randint(0, 10) < 7:
            print("car started.")
            self.started=True
        else:
            self.started=False
            
    def push_start(self):
        if random.randint(0, 10) < 5:
            print("car started")
            self.started=True
        else:
            self.started=False
        
car = Car()

class Workshop(object):
    def call(self):
        print("calling workshop")
        
workshop = Workshop()