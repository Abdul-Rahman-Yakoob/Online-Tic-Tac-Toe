import socket
# Input values for player 1 and 2, customizable
Player_one = 1
Player_two = 2
neutral = 0

def Board_status(board) -> int:
    for i in (board):
        one_win = True
        two_win = True
        for j in i:
            if(j == neutral):
                one_win = False
                two_win = False
            elif(j == Player_two):
                one_win = False
            elif(j == Player_one):
                two_win = False
            else:
                print(f'Unkown character: "{j}" on board')
                return neutral
        if(one_win):
            return Player_one
        elif(two_win):
            return Player_two
    for i in range(len(board)):
        one_win = True
        two_win = True
        for j in range(len(board)):
            if(board[j][i] == neutral):
                one_win = False
                two_win = False
            elif(board[j][i] == Player_two):
                one_win = False
            elif(board[j][i] == Player_one):
                two_win = False
            else:
                print(f'Unkown Character: {board[j][i]} on board')
                return neutral
        if(one_win):
            return Player_one
        elif(two_win):
            return Player_two
    one_win = True
    two_win = True
    for i in range(len(board)):
        if(board[i][i] == neutral):
            one_win = False
            two_win = False
            break
        elif(board[i][i] == Player_one):
            two_win = False
        elif(board[i][i] == Player_two):
            one_win = False
        else:
                print(f'Unkown Character: {board[i][i]} on board')
                return neutral
    if(one_win):
        return Player_one
    elif(two_win):
        return Player_two
    one_win = True
    two_win = True
    for i in range(len(board)):
        if(board[i][len(board)-i-1] == neutral):
            one_win = False
            two_win = False
            break
        elif(board[i][len(board)-i-1] == Player_one):
            two_win = False
        elif(board[i][len(board)-i-1] == Player_two):
            one_win = False
        else:
                print(f'Unkown Character: {board[j][i]} on board')
                return neutral
    if(one_win):
        return Player_one
    elif(two_win):
        return Player_two
    return neutral
        
def print_board(board):
    for i in range(len(board)):
        print(board[i])

# status = Board_status(
#     [[0,1,0],
#      [1,1,0],
#      [0,1,1]]
# )

size = 3

game_mode = input(f'Do you want to play "Online" or "Offline"? ')
game_mode = game_mode.lower()
online_role = 'server'
opponent_socket = None
server_ip = ''
server_port = 12345
if(game_mode.lower() == 'online'):
    online_role = input(f'Are you the "Server" or "Client"? ')
    online_role = online_role.lower()
    if(online_role.lower() == 'server'):
        print(f'Waiting for client to connect....')
        server_socket = socket.socket()
        server_socket.bind(('', server_port))
        server_socket.listen(50)
        while(True):
            opponent_socket, addr = server_socket.accept()
            print(f'Connection from {addr} has been established!!')
            opponent_socket.send('Thank you for connecting'.encode())
            break
    else:
        server_ip = input(f'Enter server IP: ')
        server_port = int(input(f'Enter server port: '))
        opponent_socket = socket.socket()
        opponent_socket.connect((server_ip, server_port))
        print(f'Connecting to server....')
        if(opponent_socket.recv(1024).decode() == 'Thank you for connecting'):
            print('Connected to the server successfully!!')

print('''\nNote: The rows and columns are numbered as 1,2,3,....\n To change the value of square respresented by row: 'r' and column: 'c', input: 'r,c'\n''')

while((game_mode.lower() == 'offline' or online_role.lower() == 'server')):
    board_size = input(f'Enter board size: ')
    if(board_size.isdigit):
        board_size = int(board_size)
        if(board_size > 0):
            size = board_size
            break
        else:
            print(f'Enter a positive number!!')
    else:
        print(f'Enter a number!!')
if(game_mode.lower() == 'online' and online_role.lower() == 'server'):
    opponent_socket.send(str(size).encode())
elif(game_mode.lower() == 'online' and online_role.lower() == 'client'):
    size = int(opponent_socket.recv(1024).decode())

board : list[list[int]] = []

for i in range(size):
    temp = []
    for j in range(size):
        temp.append(neutral)
    board.append(temp)
freeSquares = size**2
turn = 'Player_one'
while(1):
    print_board(board)
    # print(f'Current turn: {turn}')
    status = Board_status(board)
    if(status == Player_one):
        if(game_mode == 'offline'):
            print(f'Player one({Player_one}) has Won!!')
        elif(online_role == 'server'):
            print(f'You({Player_one}) have Won!!')
        else:
            print(f'Opponent({Player_one}) has Won!!')
        break
    elif(status == Player_two):
        if(game_mode == 'offline'):
            print(f'Player two({Player_two}) has Won!!')
        elif(online_role == 'client'):
            print(f'You({Player_one}) have Won!!')
        else:
            print(f'Opponent({Player_one}) has Won!!')
        break
    elif(freeSquares == 0):
        print(f'Draw!!')
        break
    # if(status == neutral):
    #     print(f'Current turn: {turn}')
    # else:
    #     print(f'Draw!!')
    r,c=0,0
    if((online_role.lower() == 'server' and turn == 'Player_one') or (online_role.lower() == 'client' and turn == 'Player_two')):
        while(1):
            r,c = input(f'{turn}: ').split(',')
            if(not r.isdigit() or not c.isdigit()):
                print(f'Enter a number!!')
                continue
            r = int(r)
            r = int(r)
            r = int(r)
            c = int(c)
            r = r-1
            c = c-1
            if(r<=-1 or r>=size or c<=-1 or c>=size):
                print(f'Enter a number between({0},{size})!!')
                continue
            elif(board[r][c] is not neutral):
                print(f'Square already occupied!!')
                continue
            else:
                break
    elif(game_mode == 'offline'):
        while(1):
            r,c = input(f'{turn}: ').split(',')
            if(not r.isdigit() or not c.isdigit()):
                print(f'Enter a number!!')
                continue
            r = int(r)
            r = int(r)
            r = int(r)
            c = int(c)
            r = r-1
            c = c-1
            if(r<=-1 or r>=size or c<=-1 or c>=size):
                print(f'Enter a number between({0},{size})!!')
                continue
            elif(board[r][c] is not neutral):
                print(f'Square already occupied!!')
                continue
            else:
                break
    if(game_mode == 'online'):
        if(online_role == 'server' and turn == 'Player_two'):
            while(1):
                r,c = opponent_socket.recv(1024).decode().split(',')
                r = int(r)
                c = int(c)
                break
        elif(online_role == 'client' and turn == 'Player_two'):
            opponent_socket.send(f'{r},{c}'.encode())
        elif(online_role == 'server' and turn == 'Player_one'):
            opponent_socket.send(f'{r},{c}'.encode())
        elif(online_role == 'client' and turn == 'Player_one'):
            while(1):
                r,c = opponent_socket.recv(1024).decode().split(',')
                r = int(r)
                c = int(c)
                break

    freeSquares = freeSquares-1
    if(turn == 'Player_one'):
        board[r][c] = Player_one
    else:
        board[r][c] = Player_two
    if(turn == 'Player_one'):
        turn = 'Player_two'
    else:
        turn = 'Player_one'

if(game_mode == 'online'):
    opponent_socket.close()
    if(online_role == 'server'):
        server_socket.close()
    print(f'Connection closed!!')