import random
import os   # for screen clearing
import sys, tty, termios    # for getch() function


def getch():    # WASD moving
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)  # wczytaj z systemu, z podstawowego wejscia, jeden znak
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
    if x == 0 or x == width-1 or y == 0 or y == height-1:
        exit()


def moving(key_input, x, y):
    if key_input == ("w"):
        y -= 1
    elif key_input == ("a"):
        x -= 1
    elif key_input == ("s"):
        y += 1
    elif key_input == ("d"):
        x += 1
    elif key_input == ("p"):
        os.system('clear')
        exit()
    return x, y


def main():
    os.system('clear')
    width = 50
    height = 20
    x = 5
    y = 5

    while True:
        print_board(insert_player(create_board(width, height), x, y))
        key_input = getch()
        x, y = moving(key_input, x, y)
        border_touch(x, y, height, width)
        os.system('clear')


if __name__ == '__main__':
    main()
