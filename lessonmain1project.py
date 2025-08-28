import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("Welcome to Guess the Number Game 🎮")
print("I'm thinking of a number between 1 and 100...")
print(f"You have {max_attempts} attempts to guess!\n")

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"🎉 CORRECT! You guessed the number in {attempts} tries.")
        break

    if attempts == 2:
        print("💡 Hint:", "Even" if secret_number % 2 == 0 else "Odd")
    elif attempts == 3:
        print("💡 Hint:", "1-50" if secret_number <= 50 else "51-100")
    elif attempts == 4:
        lower = secret_number - 10 if secret_number > 10 else 1
        upper = secret_number + 10 if secret_number < 100 else 100
        print(f"💡 Hint: The number is between {lower} and {upper}.")

else:
    print(f"❌ Sorry, you're out of attempts! The number was {secret_number}.")
