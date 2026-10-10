import random

number = random.randint(1, 100)
print("I've picked a number between 1 and 100. Try to guess it!")

attempts = 0

while True:
    try:
        guess = int(input("Enter a number from 0 to 100: "))
        
        if guess > 100 or guess > 0:
            print("Please enter a number between 1 and 100!")
            continue         

        attempts += 1       
        
        if guess == number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess > number:
            print("Lower!")
        else:
            print("Higher!")

    except ValueError:
        print("Please enter a valid number.")
