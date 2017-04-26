import random


def create_board(width=5, height=3):
    board = []
    for row in range(height):
        board.append([])
    for row in range(width):
        board[0].append('X')     # first row
        board[height-1].append('X')    # last row
    for i in range(width):
        for i in range (1,height-1):
            board[i].append(' ')
    for row in range(height):
        board[row][0] = ('X')               # first column
        board[row][width-1] = ('X')         # last column
    return board

def print_board(board):
    for row in board:
        print("".join(row))

def insert_player(board, x, y):
    board[x][y] = ('@')
    return board

def main():
    width = int(input('Enter map width: '))
    height = int(input('Enter map height: '))
    position_x = list(range(1, width-1))
    position_y = list(range(1, height-1))
    print(position_x)
    print(position_y)
    x = random.choice(position_x)
    y = random.choice(position_y)
    print_board(insert_player(create_board(width, height),x,y))

if __name__ == '__main__':
    main()
