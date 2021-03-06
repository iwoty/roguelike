import random
import os   # for screen clearing
import sys, tty, termios    # for getch() function
import datetime  # for time counting

font_green = ('\033[1;32;40m')  # changing font colors
font_blue = ('\033[1;37;44m')
font_red = ('\033[1;37;41m')
font_normal = ('\033[1;37;0m')


def getch():    # WASD moving
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)  # wczytaj z systemu, z podstawowego wejscia, jeden znak
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


'''
def create_board(board_width=100, board_height=30):  # board with size
    board_list = []
    board_list.append(list("X") * board_width)
    for row in range(board_height - 2):
        board_list.append(list("X" + " " * (board_width - 2) + "X"))
    board_list.append(board_list[0])
    board_list.append('Press P to exit')
    board_list.append('Press H for Highscore')
    return board_list
'''


def create_board(life_points, npc_killed, level, board_width=100, board_height=25):
    board_list = []
    for row in range(board_height):
        board_list.append([])
    for row in range(board_width):
        board_list[0].append('X')     # first row
        board_list[board_height-1].append('X')    # last row
    for i in range(board_width):
        for i in range (1,board_height-1):
            board_list[i].append(' ')
    for row in range(board_height):
        board_list[row][0] = ('X')               # first column
        board_list[row][board_width-1] = ('X')         # last column
    board_list.append(['Life: ', str(life_points)])
    board_list.append(['Enemies killed: ', str(npc_killed)])
    board_list.append(['Level: ', str(level)])
    board_list.append('Press P to exit')
    board_list.append('Press H for Highscore')
    return board_list


def print_board(board_list):
    for row in board_list:
        print("".join(row))


def insert_player(board, x, y):
    board[y][x] = (font_red + '@' + font_normal)
    return board


def border_touch(x, y, board_height, board_width):  # if touch border - exit
    if x == 0 or x == board_width-1 or y == 0 or y == board_height-1:
        exit()


def moving(key_input, x, y):
    if key_input == ("w"):
        y -= 1
        broadcast = "a"
    elif key_input == ("a"):
        x -= 1
        broadcast = "a"
    elif key_input == ("s"):
        y += 1
        broadcast = "a"
    elif key_input == ("d"):
        x += 1
        broadcast = "a"
    elif key_input == ("p"):
        os.system('clear')
        broadcast = "a"
        exit()
    elif key_input == ("h"):
        os.system('clear')
        broadcast = "HIGH"
    return x, y, broadcast


def highscore(time_start, player_name, level, npc_killed, life_left, board_width=111, board_height=30):  # board with size
    '''Highscore'''
    time_end = datetime.datetime.today()  # set stopwatch off
    gamedate = datetime.date.today()  # date of game
    player_time = (time_end - time_start).seconds  # how long did player play
    points = int(int(level) * int(npc_killed) * int(life_left) / int(player_time))
    players_score = [make_it_short(i, 13) for i in [player_name, gamedate, level,
                                                    player_time, npc_killed, life_left, points]]

    with open('highscores.txt', 'a') as highscore_add:  # opens and adds result to highscore
        highscore_add.write(" | ".join(players_score) + "\n")

    # HIGHSCORE SORT
    highscore = []
    with open('highscores.txt', 'r') as read:  # opens highscores.txt in read mode
        for i in range(sum(1 for line in open('highscores.txt'))):
            highscore.append(read.readline().split("|"))    # rozjebujemy liste zeby dostac sie do punktow

    highscore = sorted(highscore, key=lambda y: y[int(6)])    # sortujemy wg punktow

    for i in range(len(highscore)):
        highscore[i] = ("|".join(highscore[i]))

    board_list = []
    board_list.append(list("X") * board_width)
    board_list.append("X                                           So far highscores:                                                X")
    board_list.append("X Soldier name|     Date      |   Max level   |      Time     |   NPC killed  |  Final life   |   Points      X")
    board_list.append(highscore)
    board_list.append(board_list[0])
    return board_list


def make_it_short(word, length):
    '''HIGHSCORE - Make length of the word equal to chosen length and returns it'''
    if len(str(word)) <= length:
        word = (length - len(str(word))) * " " + str(word)
        return str(word)
    elif len(str(word)) > length:
        word = str(word)[0:length]
        return str(word)


def print_ascii_arts(i):
    '''Create list with ASCII arts, print with life_points'''
    ascii_art_list = []
    try:
        ascii_art_list.append(open('screens_start.txt', 'r'))  # open txt files with ASCII arts and create list with them
        '''ascii_art_list.append(open('hangman4.txt', 'r'))
        ascii_art_list.append(open('hangman3.txt', 'r'))
        ascii_art_list.append(open('hangman2.txt', 'r'))
        ascii_art_list.append(open('hangman1.txt', 'r'))'''
    except FileNotFoundError:
        print(font_red, 'Missing some of ASCII arts files :( Bye!', font_normal)
        exit()
    print(ascii_art_list[i].read())


def main():
    player_name = input('Enter your name soldier: ')
    os.system('clear')
    board_width = 120
    board_height = 25
    player_position = [15, 15]
    life_points = 100  # number of lifes
    time_start = datetime.datetime.today()  # set stopwatch on
    level = 10
    npc_killed = 100
    life_left = 99
    print_ascii_arts(0)
    while True:
        print_board(insert_player(create_board(life_points, npc_killed, level, board_width, board_height), player_position[0], player_position[1]))
        key_input = getch()
        player_position = moving(key_input, player_position[0], player_position[1])
        border_touch(player_position[0], player_position[1], board_height, board_width)
        os.system('clear')

        broadcast = player_position[2]
        if broadcast == "HIGH":
            break

    print_board(highscore(time_start, player_name, level, npc_killed, life_left))

if __name__ == '__main__':
    main()
