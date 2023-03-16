import UserInput
import Machine
from GlobalVar import *
import FinalOutput

def spin(BAL):
    lines=UserInput.getNumberOfLines()
    while True:
        bet=UserInput.getBet()
        tot_bet=lines*bet
        
        if tot_bet>BAL:
            print(f"You do not have enough to bet that amount, your current balance is:{BAL}\n")
            while True:
                ans=input("Press enter to DEPOSIT (b to back).")
                if ans=='b':
                    break
                else:
                    BAL+=UserInput.deposit()
                    print(f"After deopsiting your bal {BAL}")
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
    BAL= UserInput.deposit()
    while True:
        print(f"Current balance is ${BAL}")
        ans=input("Press enter to PLAY (q to quit).")
        if ans == 'q':
            break
        else:
            print()
            BAL+=spin(BAL)
    print(f"\nYou left with ${BAL}")
    print("Come again when your free <3")
    print("ﾉ(◕ヮ◕)ﾉ*:･ﾟ✧ Bye ")
main() 