def print_board(board):
    line = '-' * 9
    print(f'''{line}
| {board[0][0]} {board[0][1]} {board[0][2]} |
| {board[1][0]} {board[1][1]} {board[1][2]} |
| {board[2][0]} {board[2][1]} {board[2][2]} |
{line}''')
    pass


def win(board):

    for i in range(0, 2):
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            winner = board[i][0]
            print(winner, 'wins')
            quit()
        if board[0][i] != ' ' and board[0][i] == board[1][i] == board[2][i]:
            winner = board[0][i]
            print(winner, 'wins')
            quit()
        if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
            winner = board[0][0]
            print(winner, 'wins')
            quit()
        if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
            winner = board[0][2]
            print(winner, 'wins')
            quit()
    pass


def main():
    turn = 'X'
    start = '         '
    attempts = 0

    game_board = [[start[0], start[1], start[2]],
                  [start[3], start[4], start[5]],
                  [start[6], start[7], start[8]]]
    print_board(game_board)

    while True:
        spot = input(f'Input coordinates (row, column) for "{turn}":\n').split()

        try:
            if game_board[int(spot[0]) - 1][int(spot[1]) - 1] != ' ':
                print('This cell is occupied! Choose another one!')
                continue

            game_board[int(spot[0]) - 1][int(spot[1]) - 1] = turn

        except IndexError:
            print('Coordinates should be from 1 to 3!')
            continue

        except ValueError:
            print('You should enter numbers!')
            continue

        print_board(game_board)
        win(game_board)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        attempts += 1

        if attempts == 9:
            print('Draw')
            break
        continue


if __name__ == '__main__':
    main()
