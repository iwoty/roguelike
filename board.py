def create_board(width, hight):
    board_list = []
    board_list.append(list("x") * width)
    for value in range(hight - 2):
        board_list.append(list("x" + " " * (width - 2) + "x"))
    board_list.append(board_list[0])
    return board_list

def add_player(board_list)
    board_list[hight]

def print_board(board_list):
    for item in board_list:
        print("".join(item))





def main():
    width = int(input("Give  width"))
    hight = int(input("Give hight"))

    print_board(create_board(width, hight))

if __name__ == '__main__':
   main()
