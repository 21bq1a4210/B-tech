from random import randint
def chooseEvenOdd():
    n = randint(1,6)
    while True:
        u=input('EVEN or ODD:').lower()
        if u=='even' or u=='odd':
            while True:
                chance=input('enter any number in between 1 to 6:')
                if chance.isdigit():
                    chance=int(chance)
                    if 1<=chance<=6:
                        print('computer choose:',n)
                        return chooseBatBall(chance,n,u)
                    else:
                        print("Please enter the values in between 1 and 6")
                else:
                    print("please enter valid input")
        else:
            print("Hey please choose odd or even only")

def chooseBatBall(player,computer,player_EorO):
    add=player+computer
    if add%2==0:
        print(f"{player} + {computer} = {add} (is even)")
        if player_EorO=='even':
            return "player"
        else:
            return "computer"
    elif add%2!=0:
        print(f"{player} + {computer} = {add} (is odd)")
        if player_EorO=="odd":
            return 'player'
        else:
            return 'computer'



