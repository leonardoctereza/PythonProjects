table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#user1 = input('Row and colum to mark X')
#user2 = input('Row and colum to mark O')

def print_table():
    print '       '
    print table[0][0], '|' , table[0][1], '|', table[0][2]
    print '__________'

    print table[1][0], '|' , table[1][1], '|', table[1][2]
    print '__________'

    print table[2][0], '|' ,table[2][1], '|', table[2][2]


def check_winUser1():
    if table[0][0] == 'X' and table[0][1]=='X' and table[0][2] == 'X':
        return True
    elif table[1][0] == 'X' and table[1][1]=='X' and table[1][2] == 'X':
        return True
    elif table[2][0] == 'X' and table[2][1]=='X' and table[2][2] == 'X':
        return True
    elif table[0][0] == 'X' and table[1][0]=='X' and table[2][0] == 'X':
        return True
    elif table[0][1] == 'X' and table[1][1]=='X' and table[2][1] == 'X':
        return True
    elif table[0][2] == 'X' and table[1][2]=='X' and table[2][2] == 'X':
        return True
    elif table[0][0] == 'X' and table[1][1]=='X' and table[2][2] == 'X':
        return True
    elif table[0][2] == 'X' and table[1][1]=='X' and table[2][0] == 'X':
        return True
    else:
        return False
    
def check_winUser2():
    if table[0][0] == 'O' and table[0][1]=='O' and table[0][2] == 'O':
        return True
    elif table[1][0] == 'O' and table[1][1]=='O' and table[1][2] == 'O':
        return True
    elif table[2][0] == 'O' and table[2][1]=='O' and table[2][2] == 'O':
        return True
    elif table[0][0] == 'O' and table[1][0]=='O' and table[2][0] == 'O':
        return True
    elif table[0][1] == 'O' and table[1][1]=='O' and table[2][1] == 'O':
        return True
    elif table[0][2] == 'O' and table[1][2]=='O' and table[2][2] == 'O':
        return True
    elif table[0][0] == 'O' and table[1][1]=='O' and table[2][2] == 'O':
        return True
    elif table[0][2] == 'O' and table[1][1]=='O' and table[2][0] == 'O':
        return True
    else:
        return False
    
def check_position(row, column):
    if table[row][column] == 'X' or table[row][column] == 'O' :
        print 'Position already occupied'
        return False
    else : return True
        
def play():
    print 'Choose the row [0,1,2]:'
    row = input()
    print 'Choose the column [0,1,2]:'
    column = input()
    if(check_position(row,column) == False):
        play()
    else: 
        if rounds%2 ==0:
            table[row][column] = move['user2']
        else: table[row][column] = move['user1'] 
    
rounds = 1
move = {'user1':'X','user2':'O'}    
while(rounds<9):
    print_table()
    play()
    rounds +=1
    print_table()
    if check_winUser1():
        print 'User1 you are the winner!!!'
        print_table()
        break
    play()
    rounds +=1
    if check_winUser2():
        print 'User2 you are the winner!!!'
        print_table()
        break
if rounds == 9:
    print "There's a tie"
    print_table()

    