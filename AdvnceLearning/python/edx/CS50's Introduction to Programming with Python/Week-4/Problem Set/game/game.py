import random

def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def get_guess():
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
            if guess > 0:
                return guess
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    level = get_level()
    target = random.randint(1, level)

    while True:
        guess = get_guess()
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
