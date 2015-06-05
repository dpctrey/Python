#include <iostream>

class TicTacToe:
    
    def __init__(self):
        self.board = [" "," "," "," "," "," "," "," "," "]
        self.xTurn = True
        
    def isFull(self):
        for i in self.board:
            if i == " ":
                return False
        print("CAT!")
        return True
        
    def choose(self):
        while self.isWinner() == False and self.isFull() == False:
            myMark = input("Please enter a place (1-9): ")
            if (myMark == '1' or myMark == '2' or myMark == '3' or myMark == '4' or myMark == '5' 
            or myMark == '6' or myMark == '7' or myMark == '8' or myMark == '9'):
                myMark = int(myMark)
                self.mark(myMark)
                self.printBoard()
            else: print("Please make another selection!")
        
    def mark(self, place):
        if self.xTurn == True:
            self.board[place - 1] = "X"
            self.xTurn = False
            return True
        else:
            self.board[place - 1] = "O"
            self.xTurn = True
            return True
        
    def isWinner(self):
        if self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X":
            print("There is a winner!")
            return True
        if self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X":
            print("There is a winner!")
            return True
        if self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X":
            print("There is a winner!")
            return True
        if self.board[0] == "X" and self.board[3] == "X" and self.board[6] == "X":
            print("There is a winner!")
            return True
        if self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X":
            print("There is a winner!")
            return True
        if self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X":
            print("There is a winner!")
            return True
        if self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X":
            print("There is a winner!")
            return True
        if self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X":
            print("There is a winner!")
            return True
        if self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O":
            print("There is a winner!")
            return True
        if self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O":
            print("There is a winner!")
            return True
        if self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O":
            print("There is a winner!")
            return True
        if self.board[0] == "O" and self.board[3] == "O" and self.board[6] == "O":
            print("There is a winner!")
            return True
        if self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O":
            print("There is a winner!")
            return True
        if self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O":
            print("There is a winner!")
            return True
        if self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O":
            print("There is a winner!")
            return True
        if self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O":
            print("There is a winner!")
            return True
        else: return False
        
    def printBoard(self):
        print("-------")
        print("|" + str(self.board[0]) + "|" + str(self.board[1]) + "|" + str(self.board[2]) + "|")
        print("-------")
        print("|" + str(self.board[3]) + "|" + str(self.board[4]) + "|" + str(self.board[5]) + "|")
        print("-------")
        print("|" + str(self.board[6]) + "|" + str(self.board[7]) + "|" + str(self.board[8]) + "|")
        print("-------")
        
        
b = TicTacToe()
b.choose()