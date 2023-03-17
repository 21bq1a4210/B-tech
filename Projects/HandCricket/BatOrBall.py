from random import choices
def chooseBorB(chosser):
    if chosser=='player':
        while True:
            choice=input("Bat or Ball:?").lower()
            if choice=='bat':
                print("you chossen BATTING")
                return choice
            elif choice=='ball':
                print("You chossen BOWLLING")
                return choice
            else:
                print("choose bat or ball ONLY")
                continue
    else:
        list_of_options=['bat',"ball"]
        comp_choice=choices(list_of_options)
        print(f"Computer chossen {comp_choice[0]}")
        return comp_choice[0]