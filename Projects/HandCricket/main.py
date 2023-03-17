import Toss
import Batting
import Bowlling
import BatOrBall
import win

def main():
  while True:
    play_again=input("Enter to play (q to quit)")
    if play_again!='q':
        toss=Toss.chooseEvenOdd()
        field=BatOrBall.chooseBorB(toss)
        if field=='bat':
            if toss=='player':
               player_runs,comp_runs=Batting.bat(),Bowlling.ball()
            else:
               comp_runs,player_runs=Bowlling.ball(),Batting.bat()
        if field=="ball":
           if toss=='player':
              comp_runs,player_runs=Bowlling.ball(),Batting.bat()
           else:
              player_runs,comp_runs=Batting.bat(),Bowlling.ball()
        win.checkWin(player_runs,comp_runs)
    else:
       quit()

main()