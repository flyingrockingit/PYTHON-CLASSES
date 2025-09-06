# Define a class Robot
class Robot:
    species = "Artificial Intelligence Robot"
    
    def __init__(self, name, model, year):
        self.name = name       
        self.model = model      
        self.year = year        
    
    def introduce(self):
        print(f"Hello! I am {self.name}, model {self.model}, created in {self.year}.")
        print(f"I am a {Robot.species}.")
    
    def perform_action(self, action):
        print(f"{self.name} is now {action}.")

robot1 = Robot("RoboMax", "X100", 2025)
robot2 = Robot("AI-Buddy", "A200", 2024)

robot1.introduce()
robot1.perform_action("dancing")

print()  

robot2.introduce()
robot2.perform_action("singing")
