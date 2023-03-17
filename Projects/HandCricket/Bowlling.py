from random import randint
def ball():
    comp_runs=0
    print("Your BOWLLING starts now:")
    print("------------------------")
    while True:
        temp=int(input("Throw in between 1 to 6:"))
        comp=randint(1,6)
        print(f"computer's guess:{comp}")
        comp_runs+=comp
        print(f"Computer current score{comp_runs}\n")
        if 1<=temp<=6:
            if temp==comp:
                print("\nYou guesses same number")
                print("Ohh thats a out..! （￣︶￣）↗")
                print(f"Total computer runs: {comp_runs}\n")
                return comp_runs
        else:
            print("Yo dont be greedy you cant hit more than 6")
