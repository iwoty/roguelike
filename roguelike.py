import random
import os   # for screen clearing


def getch():    # WASD moving
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def create_board(width=50, height=20):  # board with size
    board = []
    for row in range(height):
        board.append([])
    for row in range(width):
        board[0].append('X')     # first row
        board[height-1].append('X')    # last row
    for i in range(width):
        for i in range(1, height-1):
            board[i].append(' ')
    for row in range(height):
        board[row][0] = ('X')               # first column
        board[row][width-1] = ('X')         # last column
    return board


def print_board(board):
    for row in board:
        print("".join(row))


def insert_player(board, x, y):
    board[y][x] = ('@')
    return board


def border_touch(x, y, height, width):  # if touch border - exit
    if x == 0 or x == width or y == 0 or y == height-2:
        exit()


def main():
    # width = int(input('Enter map width: '))
    # height = int(input('Enter map height: '))
    width = 50
    height = 20
    # position_x = list(range(1, width-1))
    # position_y = list(range(1, height-1))
    # x = random.choice(position_x)
    # y = random.choice(position_y)
    x = 5
    y = 5

    while True:
        print_board(insert_player(create_board(width, height), x, y))
        key_input = getch()
        print(key_input)
        if key_input == ("w"):
            y -= 1
            #border_touch()
        elif key_input == ("a"):
            x -= 1
            #border_touch()
        elif key_input == ("s"):
            y += 1
            #border_touch()
        elif key_input == ("d"):
            x += 1
            #border_touch()
        elif key_input == ("p"):
            os.system('clear')
            exit()
        border_touch(x, y, height, width)
        os.system('clear')

if __name__ == '__main__':
    main()
