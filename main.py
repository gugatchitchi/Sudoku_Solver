import board as b

# Good Board
# final_board = b.Board([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])

# Starting Board
# initial_board = b.Board([
#     [0, 0, 5, 3, 6, 0, 0, 8, 1],
#     [9, 0, 0, 0, 0, 8, 6, 2, 0],
#     [0, 0, 8, 0, 0, 0, 4, 0, 0],
#     [0, 0, 0, 8, 0, 0, 0, 0, 0],
#     [0, 0, 0, 6, 7, 2, 8, 5, 9],
#     [8, 5, 0, 9, 0, 0, 0, 0, 0],
#     [0, 0, 0, 7, 0, 6, 3, 4, 0],
#     [2, 0, 3, 0, 0, 0, 7, 0, 6],
#     [0, 0, 6, 0, 3, 9, 0, 0, 0]
# ])

# Initializing list
starting_list = []

# Let users enter their board
for i in range(9):
    row = []
    # Asking for the row from users until we get 9 numbers
    while len(row) != 9:
        print('Please enter 9 digits')
        from_users = list(input(f"Row #{i+1} : "))
        row = [int(r) for r in from_users]
    # Adding the row to the numbers list
    starting_list.append(row)

# Initialising board
initial_board = b.Board(starting_list)
initial_board.print_board()

# Finding solution
while True:
    if initial_board.check_if_done():
        break
    initial_board.add_number()

# Printing solution
initial_board.print_board()
print('Total itterations: ', initial_board.total_iterations)