

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
    
def is_win(i):
    if(board[1]==board[2]==board[3] and board[1]==i):
        return True
    elif(board[1]==board[4]==board[7] and board[1]==i):
         return True
    elif(board[1]==board[5]==board[9] and board[1]==i):
         return True
    elif(board[2]==board[5]==board[8] and board[2]==i):
         return True
    elif(board[3]==board[6]==board[9] and board[3]==i):
         return True
    elif(board[3]==board[5]==board[7] and board[3]==i):
         return True
    elif(board[4]==board[5]==board[6] and board[4]==i):
         return True
    elif(board[7]==board[8]==board[9] and board[7]==i):
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
        pos=int(input("Already Occupied!Enter New Position"))
        insert(i,pos)


def human_move(i):
    pos=int(input("Enter the Position"))
    insert(i,pos)

def computer_move(i):
    bestscore =-100
    best_pos = 0
    for index in range(1,len(board)):
        if available(index):
            board[index]=i
            score = minmax(board,False)
            board[index]=" "
            if score > bestscore:
                bestscore =score
                best_pos = index
    insert(i,best_pos)
    return


def minmax(board,is_maximising):
    if is_win(computer):
        return 10
    elif is_win(human):
        return -10
    elif draw():
        return 0
    if is_maximising:
        bestscore=-100
        for index in range(1,len(board)):
            if available(index):
                board[index]=computer
                score = minmax(board,False)
                board[index]=" "
                bestscore=max(bestscore,score)
        return bestscore
    else:
        bestscore=100
        for index in range(1,len(board)):
            if available(index):
                board[index]=human
                score = minmax(board,True)
                board[index]=" "
                bestscore=min(bestscore,score)
        return bestscore
                
    


display_board(board)
while not win():
    computer_move(computer)
    human_move(human)
    
