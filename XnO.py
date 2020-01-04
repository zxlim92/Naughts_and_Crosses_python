# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:43:31 2020

@author: limzi
"""
def tablePrint(tableInput):
    row =0
    for x in range (5):
        if x%2 == 1:
            print("------")
        else:
            print("|".join(tableInput[row]))
            row = row +1
def updateTableO(tableInput,x,y):
    tableInput[x][y] = "X"
    tablePrint(tableInput)
def playerOneTurn(tableInput):
    x,y = map(int,input().split())
    while x >2 or y>2 or tableInput[x][y] != " ":
        print("Either the position is filled or your X or Y values are greater than 2. TRY AGAIN")
        x,y = map(int,input().split())
    updateTableO(tableInput, x, y)
    return 0
def updateTableT(tableInput,x,y):
    tableInput[x][y] = "O"
    tablePrint(tableInput)
def playerTwoTurn(tableInput):
    x,y = map(int,input().split())
    while x >2 or y>2 or tableInput[x][y] != " ":
        print("Either the position is filled or your X or Y values are greater than 2. TRY AGAIN")
        x,y = map(int,input().split())
    updateTableT(tableInput, x, y)
def checkWin(tableInput,symbol):
    for z in range(3):
        if tableInput[0][z] == tableInput[1][z] == tableInput[2][z] !=" ":
            print("Winner")
            return 1
    for b in range(3):
        if tableInput[b][0] == tableInput[b][1] == tableInput[b][2] !=" ":
            print("Winner")
            return 1
    if (tableInput[0][0] == tableInput[1][1] == tableInput[2][2]!= " ") or (tableInput[2][0] == tableInput[1][1] == tableInput[0][2]!= " "):
        print("Winner")
        return 1
    else:
        return 0
tableInput = [[" "," "," "],[" "," "," "],[" "," "," "]]
tablePrint(tableInput)
endGame = 0
counter =0
while endGame == 0:
    oneInput = playerOneTurn(tableInput)
    endGame=checkWin(tableInput,"X")
    if endGame == 1:
        break
    counter = counter +1
    if counter == 9:
        print("no more space")
        break
    twoInput = playerTwoTurn(tableInput)
    endGame=checkWin(tableInput,"O")
    counter = counter +1
print("Endgame")