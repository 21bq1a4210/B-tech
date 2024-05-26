def main():
    print("Valid" if is_valid(input("Plate: ")) else "Invalid")

def is_valid(s):
    return (len(s) >= 2 and len(s) <= 6 and s[:2].isalpha() and s[-1].isdigit() and s[-1] != '0' and s[2:-1].isalpha())

main()
