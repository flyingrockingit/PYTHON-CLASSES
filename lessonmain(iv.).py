class Parrot:
    # instance attributes
    def __init__(self, name, age, emotion="happy"):
        self.name = name
        self.age = age
        self.emotion = emotion  # new attribute

    # instance methods
    def sing(self, song):
        return f"{self.name} sings {song} and feels {self.emotion}"

    def dance(self):
        return f"{self.name} is now dancing and feels {self.emotion}"

    # method to change emotion
    def set_emotion(self, new_emotion):
        self.emotion = new_emotion

# instantiate the object
blu = Parrot("Blu", 10)

# print default emotion
print(blu.sing("'Happy'"))
print(blu.dance())

# change emotion
blu.set_emotion("excited")
print(blu.sing("'Jingle Bells'"))
print(blu.dance())
