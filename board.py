
class Board:

    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    # Prints Board in the console with lines
    def print_board(self):
        # Print Columns
        for j in range(len(self.numbers_list)):

            # Row separator
            if j%3==0 and j != 0:
                print(' - ' * 9)

            # Print rows
            for i in range(len(self.numbers_list[0])):
                if i%3==0 and i!=0:
                    print('|', end='')
                print(' ' + str(self.numbers_list[j][i]) + ' ', end='')

            # New line after each row
            print()

    # Checks if the board is solved
    def check_if_solved(self):
        # Valid set to compare for
        valid_set = set(range(1, len(self.numbers_list)+1))

        # Check rows and columns
        row_nums = []
        for row in range(len(self.numbers_list[0])):
            row_nums.append(self.numbers_list[0][row])
            # Check columns
            col_nums = []
            for col in range(len(self.numbers_list)):
                col_nums.append(self.numbers_list[col][row])
            if set(col_nums) != valid_set:
                return False
        if set(row_nums) != valid_set:
            return False

        # Check each box
        for box_y in range(int(len(self.numbers_list[0])/3)):
            for box_x in range(int(len(self.numbers_list)/3)):
                # new box
                box_nums = []
                # row 1
                box_nums.append(self.numbers_list[box_x * 3][box_y * 3])
                box_nums.append(self.numbers_list[box_x * 3][box_y * 3 + 1])
                box_nums.append(self.numbers_list[box_x * 3][box_y * 3 + 2])
                # row 2
                box_nums.append(self.numbers_list[box_x * 3 + 1][box_y * 3])
                box_nums.append(self.numbers_list[box_x * 3 + 1][box_y * 3 + 1])
                box_nums.append(self.numbers_list[box_x * 3 + 1][box_y * 3 + 2])
                # row 3
                box_nums.append(self.numbers_list[box_x * 3 + 2][box_y * 3])
                box_nums.append(self.numbers_list[box_x * 3 + 2][box_y * 3 + 1])
                box_nums.append(self.numbers_list[box_x * 3 + 2][box_y * 3 + 2])
                # check box
                if set(box_nums) != valid_set:
                    return False

        return True