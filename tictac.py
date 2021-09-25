#!/usr/bin/env python
# coding: utf-8

# In[80]:


#importing libraries
import random


# In[81]:


#Drawing Board
def drawboard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")


# In[82]:


#Assigning letter from user 
def inputPlayerLetter():
    letter= ''
    while letter not in ['X','O']:
        letter = input('Do you want to be X or O?').upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# In[83]:


#First Chance
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    

            


# In[84]:


def playAgain():
    a = input('Do you want to play again?(y/n):').lower()
    if a == 'y':
        return True
    else:
        return False


# In[85]:


def makeMove(board, move, letter):
    board[move] = letter
    


# In[86]:


def isWinner(bo, le):
    return (
            (bo[1] == le and bo[2] == le and bo[3] == le) or # first row
            (bo[4] == le and bo[5] == le and bo[6] == le) or # second row
            (bo[7] == le and bo[8] == le and bo[9] == le) or # third row
            (bo[1] == le and bo[4] == le and bo[7] == le) or # first column
            (bo[2] == le and bo[5] == le and bo[8] == le) or # second column
            (bo[3] == le and bo[6] == le and bo[9] == le) or # third column
            (bo[1] == le and bo[5] == le and bo[9] == le) or # first diagonal
            (bo[3] == le and bo[5] == le and bo[7] == le) # second diagnol
           )


# In[87]:


def getBoardCopy(board):
    dupeboard = []
    for i in board:
        dupeboard.append(i)
    return dupeBoard


# In[88]:


def isSpaceFree(board, move):
    return board[move] == ' '


# In[89]:


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = input("What's your next move? (1-9)")
        return int(move)


# In[90]:


def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return possibleMoves
    else:
        return None


# In[97]:


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    for i in range(1,10):
        if isSpaceFree(copy, i):
            copy = getBoardCopy(board)
            if isWinner(copy, computerLetter):
                makeMove(copy, i, computerLetter)
                return i
            
    for i in range(1,10):
        if isSpaceFree(copy,i):
            copy = getBoardCopy(board)
            if isWinner(copy, playerLetter):
                makeMove(copy, i, computerLetter)
                return i
    
    move = chooseRandomMoveFromList(board, [1,3,7,9]) #copy
    if move != None:
        return move
    
    if isSpaceFree(board, 5): #copy
        return 5
    
    return chooseRandomMoveFromList(board, [2,4,6,8]) #copy
            


# In[98]:


def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    else:
        return True
            


# In[99]:





# In[103]:


print('Welcome To The Tic Tac Toe')
while True:
    theBoard = [' '] * 10
    pL, cL = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + 'is going to begin.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            drawboard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, move, pL)
            
            if isWinner(theBoard, pL):
                drawboard(theBoard)
                print('Oh Fu- you won')
                gameIsPlaying = False
                
            if isBoardFull(theBoard):
                drawboard(theBoard)
                print('Time Barbaad bc')
                gameIsPlaying = False
                
            else:
                turn = 'computer'
                
        else:
            move = getComputerMove(theBoard, cL)
            makeMove(theBoard, move, cL)
                
            if isWinner(theBoard, cL):
                drawboard(theBoard)
                print('Ah you have lost')
                gameIsPlaying = False
                
            if isBoardFull(theBoard):
                drawboard(theBoard)
                print('Time Barbaad bc')
                gameIsPlaying = False
                    
            else:
                    turn = 'player'
                
    if not playAgain():
        break
    


# In[ ]:





# In[ ]:





# In[ ]:



