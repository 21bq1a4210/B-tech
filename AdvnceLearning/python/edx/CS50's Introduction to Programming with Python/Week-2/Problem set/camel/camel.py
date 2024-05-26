def main():
    # Prompt the user for a camel case variable name
    camel_case = input("camelCase: ").strip()

    # Convert the camel case variable name to snake case
    snake_case = convert_to_snake_case(camel_case)

    # Output the snake case variable name
    print("snake_case:", snake_case)

def convert_to_snake_case(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()
