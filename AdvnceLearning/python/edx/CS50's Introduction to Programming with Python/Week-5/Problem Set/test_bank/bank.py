def main():
    print(value(input("Greeting: ")))

def value(gre):
    if gre.lower().startswith('h'):
        if gre.startswith('hello'):
            return 0
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()
