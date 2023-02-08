# using nested functions
def TicTacToe():
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  end = False
  # we may choose any one 
  #MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]
  #MagicSquare = [8, 3, 4, 1, 5, 9, 6, 7, 2]
  MagicSquare = [2, 7, 6, 9, 5, 1, 4, 3, 8]
  def PrintBoard():
    print()
  #  print("-------|-------|------|")
    print('',board[0],"/",MagicSquare[0], "|", board[1],"/",MagicSquare[1], "|", 
board[2],"/",MagicSquare[2])
    print("-------|-------|------")
    print('',board[3],"/",MagicSquare[3], "|", board[4],"/",MagicSquare[4], 
"|",board[5],"/",MagicSquare[5])
    print("-------|-------|------") 
    print('',board[6],"/",MagicSquare[6], "|", board[7],"/",MagicSquare[7], 
"|",board[8],"/",MagicSquare[8])
 #   print("-------|-------|------|") 
    print()
  def GetNumber():
    while True:
      number = input()
      try:
        number  = int(number)
        if number in range(1, 10):
          return number
        else:
          print("\nInvalid Number.........Chooses Position not found on board")
          print("Input some one number which is on the board:")
      except ValueError:
        print("\nThat's not a number. Try again")
        continue
  def Turn(player):
    placing_index = GetNumber() - 1
    if board[placing_index] == "X" or board[placing_index] == "O":
      print("\nSquare already occupied. Input some other one")
      Turn(player)
    else:
      board[placing_index] = player
  def CheckWin(player):
    count = 0
    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if board[x] == player and board[y] == player and board[z] == player:
              if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                print("Player", player ,"win the game\n")
                return True
    for a in range(9):
      if board[a] == "X" or board[a] == "O":
        count += 1
      if count == 9:
        print("ooh.... game ends with Tie\n")
        return True
  while not end:
    PrintBoard()
    end = CheckWin("O")
    if end == True:
      break
    print("Machine Turn(X)")
    Turn("X")
    PrintBoard()
    end = CheckWin("X")
    if end == True:
      break
    print("Human Turn(O)")
    Turn("O")
# Drive Code
print('Welcome to Tic Tac Toe!\n implemented by using magic square approach')
print('Assumptions :')
print("1. It is a game betwen two human users only")
print("2. Machine will play first")
print("3. Initial Board Position is and each sqare can be represented as position/element of magic sqaure")
print("4. One use is  Human and another user is machine")
TicTacToe()