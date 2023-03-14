import random
from GlobalVar import *;

def getSlotMachineSpin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def printSlotMachine(columns):
    '''for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end='|')
            else:
                print(column[row])'''
    print(f"{columns[0][0]} | {columns[0][1]} | {columns[0][2]}  x1")
    print("---- ----- ----")
    print(f"{columns[1][0]} | {columns[1][1]} | {columns[1][2]}  x2")
    print("---- ----- ----")
    print(f"{columns[2][0]} | {columns[2][1]} | {columns[2][2]}  x1")
