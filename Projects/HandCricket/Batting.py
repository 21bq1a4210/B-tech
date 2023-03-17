from random import randint
def bat():
    runs=0
    print("Your BATTING starts now:")
    print("------------------------")
    while True:
        temp=int(input("Hit in between 1 to 6:"))
        comp=randint(1,6)
        print(f"computer's guess:{comp}")
        print(f"Your current score {runs}")
        if 1<=temp<=6:
            runs+=temp
            if temp==comp:
                print("\nComputer guesses same number")
                print("Ohh thats a out..! （￣︶￣）↗")
                print(f"Total runs: {runs}\n")
                return runs
        else:
            print("Yo dont be greedy you cant hit more than 6")