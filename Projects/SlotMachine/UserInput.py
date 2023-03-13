from GlobalVar import *
def deposit():
    while True:
        amount=input("What would you like to deposit? $:")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def getNumberOfLines():
    while True:
        lines=input("Enter the no.of lines to bet on (1 to"+str(MAX_LINES)+")?:")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid no.of lines.")
        else:
            print("Please enter a number")
    return lines

def getBet():
    while True:
        amount=input("What would you like to bet on each line? $:")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MAX_BET}-{MIN_BET}")
    return amount