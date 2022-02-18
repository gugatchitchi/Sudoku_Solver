
class Board:

    # Initializing
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list
        self.size = len(numbers_list)
        self.history = []


    # Prints Board in the console with lines
    def print_board(self):
        # Top margin
        print('\n New Table')
        # Print Columns
        for j in range(self.size):

            # Row separator
            if j%3==0 and j != 0:
                print(' - ' * 9)

            # Print rows
            for i in range(self.size):
                if i%3==0 and i!=0:
                    print('|', end='')
                print(' ' + str(self.numbers_list[j][i]) + ' ', end='')

            # New line after each row
            print()


    # Adds next number on the board
    def add_number(self):
        # Find first zero number
        for col in range(self.size):
            for row in range(self.size):
                if self.numbers_list[col][row]==0:
                    # When zero is found we should add some number
                    # If board is happy with that number we stop
                    # if it is not we check next number
                    if self.update_number(row, col, 1):
                        print('Number was Updated Succesfuly')
                        return
                    # If board does not like any number for that position
                    # We should change previous numbers, until board likes it
                    for hist in range(self.history):
                        row = hist['row']
                        col = hist['col']
                        num = hist['num']



    def update_number(self, row, col, min_num):
        # We check if any numbers could be added to that coordinate
        for num in range(min_num, self.size + 1):
            self.numbers_list[col][row] = num
            if self.check_board():
                self.history.append({
                    'row': row,
                    'col': col,
                    'num': num
                })
                return True
        # If no number can be put there we leave that coordinate
        # as 0 and return false
        self.numbers_list[col][row] = 0
        return False


    # Checks board after every itteration
    def check_board(self):
        # Check rows
        for row in range(self.size):
            row_nums = []
            for col in range(self.size):
                if self.numbers_list[row][col] not in row_nums and self.numbers_list[row][col] != 0:
                    row_nums.append(self.numbers_list[row][col])
                elif self.numbers_list[row][col] == 0:
                    continue
                else:
                    print('Number was doubled in a row: ', row+1)
                    self.print_board()
                    return False

        # Check columns
        for col in range(self.size):
            col_nums = []
            for row in range(self.size):
                if self.numbers_list[row][col] not in col_nums and self.numbers_list[row][col] != 0:
                    col_nums.append(self.numbers_list[row][col])
                elif self.numbers_list[row][col] == 0:
                    continue
                else:
                    print('Number was doubled in a column: ', col+1)
                    self.print_board()
                    return False

        # Check each box
        # Number of boxes is based on the size of the board
        for box_y in range(int(len(self.numbers_list[0]) / 3)):
            for box_x in range(int(len(self.numbers_list) / 3)):
                box_nums = []
                # Each box will always be 3x3 matrix
                # Here we generate the numbers in boxes
                for x in range(3):
                    for y in range(3):
                        if self.numbers_list[box_x * 3 + x][box_y * 3 + y] not in box_nums and self.numbers_list[box_x * 3 + x][box_y * 3 + y] != 0:
                            box_nums.append(self.numbers_list[box_x * 3 + x][box_y * 3 + y])
                        elif self.numbers_list[box_x * 3 + x][box_y * 3 + y] == 0:
                            continue
                        else:
                            print('Number was doubled in a box: ', box_x + 1, '-', box_y + 1)
                            self.print_board()
                            return False

        # Final state if all the checks are successful
        return True
