import UserInput
import Machine
from GlobalVar import *
import FinalOutput

def spin(bal):
    lines=UserInput.getNumberOfLines()
    while True:
        bet=UserInput.getBet()
        tot_bet=lines*bet
        
        if tot_bet>bal:
            print(f"You do not have enough to bet that amount, your current balance is:{bal}")
            while True:
                ans=input("Press enter to DEPOSIT (b to back).")
                if ans=='b':
                    break
                else:
                    bal+=UserInput.deposit()
        else:
            break
    print(f"your are betting ${bet} on {lines} lines.\n Total bet is equal to {tot_bet}")
    slots=Machine.getSlotMachineSpin(ROWS,COLS,symbol_count)
    print()
    Machine.printSlotMachine(slots)
    print()
    winnings,win_lines=FinalOutput.checkWinnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *win_lines)
    return winnings-tot_bet

def main():
    bal= UserInput.deposit()
    while True:
        print(f"Current balance is ${bal}")
        ans=input("Press enter to PLAY (q to quit).")
        if ans == 'q':
            break
        else:
            print()
            bal+=spin(bal)
    print(f"You left with ${bal}")
    print("Come again when your free <3")
main()