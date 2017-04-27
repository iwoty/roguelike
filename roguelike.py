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
    board_list = []
    board_list.append(list("X") * width)
    for value in range(height - 2):
        board_list.append(list("X" + " " * (width - 2) + "X"))
    board_list.append(board_list[0])
    return board_list


def print_board(board_list_with_player):
    for row in board_list_with_player:
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
    # position_x = list(range(1, width-1))
    # position_y = list(range(1, height-1))
    # x = random.choice(position_x)
    # y = random.choice(position_y)
    x = 5
    y = 5
    height = 20
    width = 20

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
