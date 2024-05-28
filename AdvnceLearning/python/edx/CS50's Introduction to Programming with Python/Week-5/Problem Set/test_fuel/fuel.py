def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                continue
            percentage = (x / y) * 100
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage:.0f}%")
            break
        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()
