import random
board=[' ']*10
computer ="O"
human= "X"


def display_board(board):
    print()
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print()
    print('-'*10)


def win():
    if(board[1]==board[2]==board[3] and board[1]!=" "):
        return True
    elif(board[1]==board[4]==board[7] and board[1]!=" "):
         return True
    elif(board[1]==board[5]==board[9] and board[1]!=" "):
         return True
    elif(board[2]==board[5]==board[8] and board[2]!=" "):
         return True
    elif(board[3]==board[6]==board[9] and board[3]!=" "):
         return True
    elif(board[3]==board[5]==board[7] and board[3]!=" "):
         return True
    elif(board[4]==board[5]==board[6] and board[4]!=" "):
         return True
    elif(board[7]==board[8]==board[9] and board[7]!=" "):
         return True
    else:
         return False
def available(pos):
     return True if board[pos]==" " else False

def draw():
     if board.count(' ')<2:
          return True
     else:
          return False
          
     
    
def  insert(i,pos):
    if available(pos):
          board[pos]=i
          display_board(board)
          if win():
               if i==computer:
                    print("Computer wins")
                    exit()
               else:
                    print("Human wins")
                    exit()
          if draw():
               print("Draw")
               exit()
    else:
        if i==human:
              pos=int(input("Enter the position"))
        elif i==computer:
              pos=random.randint(1,9)
        insert(i,pos)


def human_move(i):
     pos=int(input("Enter the position"))
     insert(i,pos)

def computer_move(i):
     pos=random.randint(1,9)
     insert(i,pos)
     





while not win():
    display_board(board)
    computer_move(computer)
    human_move(human)
 

