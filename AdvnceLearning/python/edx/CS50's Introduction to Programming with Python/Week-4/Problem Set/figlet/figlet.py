import sys
import pyfiglet

def print_usage_and_exit():
    print("Invalid usage")
    sys.exit(1)

def main():
    if len(sys.argv) == 1:
        font = None
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
    else:
        print_usage_and_exit()

    text = input("Enter text: ")
    fig = pyfiglet.Figlet(font=font)
    print(fig.renderText(text))

if __name__ == "__main__":
    main()
# pip install pyfiglet