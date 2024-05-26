# def main():
#     text = input("Input: ")
#     print(shorten(text))

# def shorten(text):
#     vowels = "AEIOUaeiou"
#     return ''.join([char for char in text if char not in vowels])

# if __name__ == "__main__":
#     main()

print(''.join([char for char in input("Input: ") if char not in "AEIOUaeiou"]))
