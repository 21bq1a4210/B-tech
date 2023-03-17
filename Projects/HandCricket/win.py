def checkWin(player_run,comp_runs):
    if player_run>comp_runs:
        print("You won...")
        print(f"You won by {player_run-comp_runs}\n")
    
    else:
        print("Computer won...")
        print(f"Computer won by {comp_runs-player_run}\n")
