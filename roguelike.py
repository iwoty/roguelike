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
    board_list = []
    board_list.append(list("X") * width)
    for value in range(height - 2):
        board_list.append(list("X" + " " * (width - 2) + "X"))
    board_list.append(board_list[0])
    board_list.append('Press P to exit')
    return board_list


def print_board(board_list_with_player):
    for row in board_list_with_player:
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
