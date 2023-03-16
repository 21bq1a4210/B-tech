def checkWinnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    '''for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check =column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    '''
    if columns[0][0]==columns[0][1]==columns[0][2]:
        winnings+=values[columns[0][0]]*bet
        winning_lines.append(1)
    if columns[1][0]==columns[1][1]==columns[1][2]:
        winnings+=values[columns[0][0]]*bet*2
        winning_lines.append(2)
    if columns[2][0]==columns[2][1]==columns[2][2]:
        winnings+=values[columns[0][0]]*bet*3
        winning_lines.append(3)
            
    return winnings,winning_lines