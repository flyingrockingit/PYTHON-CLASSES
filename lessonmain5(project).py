from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

# Subclasses
class Human(Animal):
    def move(self):
        print("👨 I can walk and run")

class Snake(Animal):
    def move(self):
        print("🐍 I can hiss and crawl")

class Dog(Animal):
    def move(self):
        print("🐶 I can bark and run")

class Lion(Animal):
    def move(self):
        print("🦁 I can roar and hunt")

class Bird(Animal):
    def move(self):
        print("🐦 I can fly")

class Dolphin(Animal):
    def move(self):
        print("🐬 I can swim gracefully")

# Main function
def main():
    animals = {
        "1": Human(),
        "2": Snake(),
        "3": Dog(),
        "4": Lion(),
        "5": Bird(),
        "6": Dolphin()
    }

    while True:
        print("\n=== Animal Movement Simulator ===")
        print("Choose an animal:")
        print("1. Human")
        print("2. Snake")
        print("3. Dog")
        print("4. Lion")
        print("5. Bird")
        print("6. Dolphin")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("👋 Goodbye!")
            break
        elif choice in animals:
            animals[choice].move()
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
