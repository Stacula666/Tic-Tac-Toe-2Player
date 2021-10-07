
#                                            TIC TAC TOE

#  Imports

import random

#  Designing the board

#  Top blank, bottom blank -- Used for all 9 blanks
row_top_blank = ([' ' * 14 + '|', ' ' * 14 + '|', ' ' * 14])

#  Board separator line -- Used with every row but bottom row
row_under_all = (['_' * 14 + '|', '_' * 14 + '|', '_' * 14])

#  Designing an X to integrate blank lines on an individual box scope

#  Top Line of X for all 3 boxes
top_left_x_line_one = 6 * ' ' + '\\  /' + ' ' * 4 + '|'
top_center_x_line_one = 5 * ' ' + '\\  /' + ' ' * 5 + '|'
top_right_x_line_one = 4 * ' ' + '\\  /' + ' ' * 9

#  2nd Line of X  for all three boxes
top_left_x_line_two = 7 * ' ' + '\\/' + ' ' * 5 + '|'
top_center_x_line_two = 6 * ' ' + '\\/' + ' ' * 6 + '|'
top_right_x_line_two = 5 * ' ' + '\\/' + ' ' * 9

#  3rd Line of X for all three boxes
top_left_x_line_three = 7 * ' ' + '/\\' + ' ' * 5 + '|'
top_center_x_line_three = 6 * ' ' + '/\\' + ' ' * 6 + '|'
top_right_x_line_three = 5 * ' ' + '/\\' + ' ' * 9

#  4th Line of X for all three boxes
top_left_x_line_four = 6 * ' ' + '/  \\' + ' ' * 4 + '|'
top_center_x_line_four = 5 * ' ' + '/  \\' + ' ' * 5 + '|'
top_right_x_line_four = 4 * ' ' + '/  \\' + ' ' * 5

#  Combining all the lines from above for letter X, each box per row, 3 boxes in the scope, 3 separate objects
top_row_x_line_one = ([top_left_x_line_one, top_center_x_line_one, top_right_x_line_one])
top_row_x_line_two = ([top_left_x_line_two, top_center_x_line_two, top_right_x_line_two])
top_row_x_line_three = ([top_left_x_line_three, top_center_x_line_three, top_right_x_line_three])
top_row_x_line_four = ([top_left_x_line_four, top_center_x_line_four, top_right_x_line_four])

#  Making an O to integrate blank lines on an individual box scope

#  Top Line of O - Top Row
top_left_o_line_one = (6 * ' ' + '____' + ' ' * 4 + '|')
top_center_o_line_one = (5 * ' ' + '____' + ' ' * 5 + '|')
top_right_o_line_one = (4 * ' ' + '____')

#  2nd Line of O - Top Row
top_left_o_line_two = (5 * ' ' + '|' + ' ' * 4 + '|' + 3 * ' ' + '|')
top_center_o_line_two = (4 * ' ' + '|' + ' ' * 4 + '|' + ' ' * 4 + '|')
top_right_o_line_two = (3 * ' ' + '|' + ' ' * 4 + '|')

#  3rd Line of O - Top Row
top_left_o_line_three = (5 * ' ' + '|' + ' ' * 4 + '|' + 3 * ' ' + '|')
top_center_o_line_three = (4 * ' ' + '|' + ' ' * 4 + '|' + ' ' * 4 + '|')
top_right_o_line_three = (3 * ' ' + '|' + ' ' * 4 + '|')

#  4th Line of O - Top Row
top_left_o_line_four = (5 * ' ' + '|____|' + 3 * ' ' + '|')
top_center_o_line_four = (4 * ' ' + '|____|' + ' ' * 4 + '|')
top_right_o_line_four = (3 * ' ' + '|____|' + 4 * ' ')

#  Making an 0 to integrate with above blank lines on an individual box scope
top_row_o_line_one = ([top_left_o_line_one, top_center_o_line_one, top_right_o_line_one])
top_row_o_line_two = ([top_left_o_line_two, top_center_o_line_two, top_right_o_line_two])
top_row_o_line_three = ([top_left_o_line_three, top_center_o_line_three, top_right_o_line_three])
top_row_o_line_four = ([top_left_o_line_four, top_center_o_line_four, top_right_o_line_four])
#  End of board and letter design and logic

#  Functions


def make_top_row(top):
    """
        Top row of Tic Tac Toe board. Takes all 27 possibilities for row
    """

    #  'X' AND 'O' INDIVIDUALLY ONLY WITH BLANKS, IE, NO MIXING OF 'X AND 'O'

    if top[0] == '7' and top[1] == '8' and top[2] == '9':

        for z in range(0, 5):
            print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'X' and top[1] == 'X' and top[2] == 'X':
        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == 'O' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == '8' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == '8' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == 'X' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == 'O' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == 'X' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == 'O' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'X' and top[1] == '8' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == '8' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'X' and top[1] == '8' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == '8' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'X' and top[1] == 'X' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == 'O' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    #  'X' AND 'O' TOGETHER WITHOUT BLANKS

    elif top[0] == 'X' and top[1] == 'X' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == 'O' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'X' and top[1] == 'O' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == 'X' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'X' and top[1] == 'O' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == 'X' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    # 'X' AND 'O' TOGETHER WITH BLANKS

    elif top[0] == 'X' and top[1] == 'O' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == 'X' and top[2] == '9':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'X' and top[1] == '8' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == 'O' and top[1] == '8' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == 'X' and top[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif top[0] == '7' and top[1] == 'O' and top[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')
    else:
        print('Something is wrong. Should make row. Call your IT guy or call me')

#  Make center row


def make_center_row(center):
    """
        Center row of Tic Tac Toe Board. The print statements uses top_row variables because
        I figured out how to use the same pattern for all 3 rows and separated the last line
        for the box borders. X
    """

    #  'X' AND 'O' INDIVIDUALLY ONLY WITH BLANKS, IE, NO MIXING OF 'X AND 'O'

    if center[0] == '4' and center[1] == '5' and center[2] == '6':

        for dog in range(0, 5):
            print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'X' and center[1] == 'X' and center[2] == 'X':
        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == 'O' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == '5' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == '5' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == 'X' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == 'O' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == 'X' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == 'O' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'X' and center[1] == '5' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == '5' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'X' and center[1] == '5' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == '5' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'X' and center[1] == 'X' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == 'O' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    #  'X' AND 'O' TOGETHER WITHOUT BLANKS

    elif center[0] == 'X' and center[1] == 'X' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == 'O' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'X' and center[1] == 'O' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == 'X' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'X' and center[1] == 'O' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == 'X' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    # 'X' AND 'O' TOGETHER WITH BLANKS

    elif center[0] == 'X' and center[1] == 'O' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == 'X' and center[2] == '6':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'X' and center[1] == '5' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == 'O' and center[1] == '5' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == 'X' and center[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')

    elif center[0] == '4' and center[1] == 'O' and center[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

        print(f'{row_under_all[0]}{row_under_all[1]}{row_under_all[2]}')
    else:
        print('Something is wrong. Should make row. Call your IT guy or call me')

#  Make bottom_row


def make_bottom_row(floor):
    """
       Bottom row of Tic Tac Toe Board. The print statements uses top_row variables because
       I figured out how to use the same pattern for all 3 rows
    """

    #  'X' AND 'O' INDIVIDUALLY ONLY WITH BLANKS, IE, NO MIXING OF 'X AND 'O'

    if floor[0] == '1' and floor[1] == '2' and floor[2] == '3':

        for z in range(0, 6):
            print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')

    elif floor[0] == 'X' and floor[1] == 'X' and floor[2] == 'X':
        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

    elif floor[0] == 'O' and floor[1] == 'O' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

    elif floor[0] == '1' and floor[1] == '2' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

    elif floor[0] == '1' and floor[1] == '2' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

    elif floor[0] == '1' and floor[1] == 'X' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

    elif floor[0] == '1' and floor[1] == 'O' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

    elif floor[0] == '1' and floor[1] == 'X' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')

        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

    elif floor[0] == '1' and floor[1] == 'O' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

    elif floor[0] == 'X' and floor[1] == '2' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

    elif floor[0] == 'O' and floor[1] == '2' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

    elif floor[0] == 'X' and floor[1] == '2' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{row_top_blank[2]}')

    elif floor[0] == 'O' and floor[1] == '2' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{row_top_blank[2]}')

    elif floor[0] == 'X' and floor[1] == 'X' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

    elif floor[0] == 'O' and floor[1] == 'O' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

    #  'X' AND 'O' TOGETHER WITHOUT BLANKS

    elif floor[0] == 'X' and floor[1] == 'X' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

    elif floor[0] == 'O' and floor[1] == 'O' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

    elif floor[0] == 'X' and floor[1] == 'O' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{top_row_o_line_four[2]}')

    elif floor[0] == 'O' and floor[1] == 'X' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{top_row_x_line_four[2]}')

    elif floor[0] == 'X' and floor[1] == 'O' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

    elif floor[0] == 'O' and floor[1] == 'X' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

    # 'X' AND 'O' TOGETHER WITH BLANKS

    elif floor[0] == 'X' and floor[1] == 'O' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{top_row_o_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_two[0]}{top_row_o_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_three[0]}{top_row_o_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_four[0]}{top_row_o_line_four[1]}{row_top_blank[2]}')

    elif floor[0] == 'O' and floor[1] == 'X' and floor[2] == '3':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{top_row_x_line_one[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_two[0]}{top_row_x_line_two[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_three[0]}{top_row_x_line_three[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_four[0]}{top_row_x_line_four[1]}{row_top_blank[2]}')

    elif floor[0] == 'X' and floor[1] == '2' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_x_line_one[0]}{row_top_blank[1]}{top_row_o_line_one[2]}')
        print(f'{top_row_x_line_two[0]}{row_top_blank[1]}{top_row_o_line_two[2]}')
        print(f'{top_row_x_line_three[0]}{row_top_blank[1]}{top_row_o_line_three[2]}')
        print(f'{top_row_x_line_four[0]}{row_top_blank[1]}{top_row_o_line_four[2]}')

    elif floor[0] == 'O' and floor[1] == '2' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{top_row_o_line_one[0]}{row_top_blank[1]}{top_row_x_line_one[2]}')
        print(f'{top_row_o_line_two[0]}{row_top_blank[1]}{top_row_x_line_two[2]}')
        print(f'{top_row_o_line_three[0]}{row_top_blank[1]}{top_row_x_line_three[2]}')
        print(f'{top_row_o_line_four[0]}{row_top_blank[1]}{top_row_x_line_four[2]}')

    elif floor[0] == '1' and floor[1] == 'X' and floor[2] == 'O':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_one[1]}{top_row_o_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_two[1]}{top_row_o_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_three[1]}{top_row_o_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_x_line_four[1]}{top_row_o_line_four[2]}')

    elif floor[0] == '1' and floor[1] == 'O' and floor[2] == 'X':

        print(f'{row_top_blank[0]}{row_top_blank[1]}{row_top_blank[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_one[1]}{top_row_x_line_one[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_two[1]}{top_row_x_line_two[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_three[1]}{top_row_x_line_three[2]}')
        print(f'{row_top_blank[0]}{top_row_o_line_four[1]}{top_row_x_line_four[2]}')

    else:
        print('Something is wrong. Should make row. Call your IT guy or call me')

#  mini_board


def mini_board():
    """
    Printing a mini-board of the real board with letters and numbers representing the button choices
    """

    print('  ' * 9 + f'{top_row_game[0]}  {top_row_game[1]}  {top_row_game[2]}')
    print('  ' * 9 + f'{center_row_game[0]}  {center_row_game[1]}  {center_row_game[2]}')
    print('  ' * 9 + f'{bottom_row_game[0]}  {bottom_row_game[1]}  {bottom_row_game[2]}')

#  Choose who goes first


def choose_first() -> object:
    jaret = random.randint(1, 2)

    if jaret == 1:
        print('Player1 will go first')
        print()
    else:
        print('Player2 will go first')
        print()
    return jaret

#  Choosing to use X or O


def player_choice(x):

    if x == 1:
        marker = input("Player1, please pick a marker: 'X' or 'O'    ")
        while marker != 'X' and marker != 'O':
            marker = input("Please pick a marker: 'X' or 'O'    ")
        if marker == 'X':
            playa1 = marker
            playa2 = 'O'
        else:
            playa1 = marker
            playa2 = 'X'
    else:
        marker = input("Player2, please pick a marker: 'X' or 'O'    ")
        while marker != 'X' and marker != 'O':
            marker = input("Please pick a marker Player2: 'X' or 'O'    ")
        if marker == 'X':
            playa2 = marker
            playa1 = 'O'
        else:
            playa2 = marker
            playa1 = 'X'

    return playa1, playa2

#  Eliminate clutter in output display


def space():

    for i in range(1, 100):
        print()

#  Input Select for player


def input_choice():
    byebyeloop: bool = False

    while not byebyeloop:

        print('Above is the TIC-TAC-TOE board. Below the board is the numerical layout. GOOD LUCK!')
        position = input('please pick a number 1-9      ')

        if position.isdigit() and position in selection_list:

            return position

        else:
            pass

#  Select O during runs


def select_o(m):

    if m == '1':

        bottom_row_game[0] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '2':

        bottom_row_game[1] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '3':

        bottom_row_game[2] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '4':

        center_row_game[0] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '5':

        center_row_game[1] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '6':

        center_row_game[2] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '7':

        top_row_game[0] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '8':

        top_row_game[1] = 'O'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '9':

        top_row_game[2] = 'O'
        return top_row_game, center_row_game, bottom_row_game


#  Select X during runs


def select_x(m):

    if m == '1':

        bottom_row_game[0] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '2':

        bottom_row_game[1] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '3':

        bottom_row_game[2] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '4':

        center_row_game[0] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '5':

        center_row_game[1] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '6':

        center_row_game[2] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '7':

        top_row_game[0] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '8':

        top_row_game[1] = 'X'
        return top_row_game, center_row_game, bottom_row_game

    elif m == '9':

        top_row_game[2] = 'X'
        return top_row_game, center_row_game, bottom_row_game


#  for X


def check_for_x():
    if top_row_game[0] == 'X' and top_row_game[1] == 'X' and top_row_game[2] == 'X':
        return True
    elif center_row_game[0] == center_row_game[1] == center_row_game[2] == 'X':
        return True
    elif bottom_row_game[0] == bottom_row_game[1] == bottom_row_game[2] == 'X':
        return True

    # Check vertically for X

    elif top_row_game[0] == center_row_game[0] == bottom_row_game[0] == 'X':
        return True
    elif top_row_game[1] == center_row_game[1] == bottom_row_game[1] == 'X':
        return True
    elif top_row_game[2] == center_row_game[2] == bottom_row_game[2] == 'X':
        return True

    # Check diagonally for X

    elif top_row_game[0] == center_row_game[1] == bottom_row_game[2] == 'X':
        return True
    elif top_row_game[2] == center_row_game[1] == bottom_row_game[0] == 'X':
        return True
    else:
        return False


#  Check horizontally for O


def check_for_o():

    if top_row_game[0] == top_row_game[1] == top_row_game[2] == 'O':
        return True
    elif center_row_game[0] == center_row_game[1] == center_row_game[2] == 'O':
        return True
    elif bottom_row_game[0] == bottom_row_game[1] == bottom_row_game[2] == 'O':
        return True

    # Check vertically for O

    elif top_row_game[0] == center_row_game[0] == bottom_row_game[0] == 'O':
        return True
    elif top_row_game[1] == center_row_game[1] == bottom_row_game[1] == 'O':
        return True
    elif top_row_game[2] == center_row_game[2] == bottom_row_game[2] == 'O':
        return True

    # Check diagonally for O

    elif top_row_game[0] == center_row_game[1] == bottom_row_game[2] == 'O':
        return True
    elif top_row_game[2] == center_row_game[1] == bottom_row_game[0] == 'O':
        return True

    else:
        return False


#  Variables

# rows = (['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'])

top_row_game = (['7', '8', '9'])
center_row_game = (['4', '5', '6'])
bottom_row_game = (['1', '2', '3'])

player1 = 'Player 1'
player2 = 'Player 2'

selection_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# First line of the program becoming interactive

opening = choose_first()

if opening == 1:
    player1 = player1, 'odd'
    player2 = player2, 'even'
else:
    player1 = player1, 'even'
    player2 = player2, 'odd'


pickmarker = player_choice(opening)

player1 = player1[0], pickmarker[0], player1[1]
player2 = player2[0], pickmarker[1], player2[1]

winner_o = False
winner_x = False
tie = False
t = 1

while t < 10 and not winner_o and not winner_x and not tie:

    space()

    make_top_row(top_row_game)
    make_center_row(center_row_game)
    make_bottom_row(bottom_row_game)
    print()
    mini_board()
    print()

    tm = t % 2 == 0

    s = input_choice()
    space()

    if tm:

        if 'even' in player1:

            if 'X' in player1:
                select = select_x(s)

            else:
                select = select_o(s)

        else:

            if 'X' in player2:
                select = select_x(s)

            else:
                select = select_o(s)

    else:

        if 'odd' in player1:

            if 'X' in player1:
                select = select_x(s)

            else:
                select = select_o(s)

        else:

            if 'X' in player2:
                select = select_x(s)

            else:

                select = select_o(s)

    top_row_game = select[0]
    center_row_game = select[1]
    bottom_row_game = select[2]

    selection_list.remove(s)

    check_o = check_for_o()

    winner_o = check_o

    check_x = check_for_x()

    winner_x = check_x

    t += 1

    make_top_row(top_row_game)
    make_center_row(center_row_game)
    make_bottom_row(bottom_row_game)
    print()
    mini_board()
    print()

    if winner_x:
        print('Congratulations!! Way to play the X')
    else:
        pass

    if winner_o:
        print('Congratulations!! Way to play the O')
    else:
        pass

    if len(selection_list) == 1 and not winner_x and not winner_o:
        final = []
        if 'odd' in player1:
            if 'X' in player1:
                final = select_x(selection_list[0])
            elif 'O' in player1:
                final = select_o(selection_list[0])
        else:
            if 'X' in player2:
                final = select_x(selection_list[0])
            elif 'O' in player2:
                final = select_o(selection_list[0])

        top_row_game = final[0]
        center_row_game = final[1]
        bottom_row_game = final[2]

        check_o = check_for_o()

        winner_o = check_o

        check_x = check_for_x()

        winner_x = check_x

        print()
        print()
        if winner_x:
            print('Congratulations!! Way to play the X')
            print()
        elif winner_o:
            print('Congratulations!! Way to play the O')
            print()
        else:
            print('Wow!!!!!  A TIE!!! Great jobs Player 1 and Player 2')
            tie = True
            print()

    make_top_row(top_row_game)
    make_center_row(center_row_game)
    make_bottom_row(bottom_row_game)
    print()
    mini_board()
    print()
