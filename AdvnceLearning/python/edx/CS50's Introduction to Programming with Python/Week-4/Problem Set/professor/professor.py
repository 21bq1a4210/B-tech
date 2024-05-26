import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        tries = 0
        while tries < 3:
            answer = input(f"{x} + {y} = ")
            try:
                answer = int(answer)
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        else:
            print(f"{x + y}")
    print(f"Score: {score}/10")


def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            print("Please enter 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        max_value = 9
    elif level == 2:
        max_value = 99
    elif level == 3:
        max_value = 999
    else:
        raise ValueError("Invalid level")
    x = random.randint(0, max_value)
    y = random.randint(0, max_value)
    return x, y


if __name__ == "__main__":
    main()
