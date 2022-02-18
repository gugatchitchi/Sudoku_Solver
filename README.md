# Sudoku_Solver

The program takes input from users in the form of rows, 9 row in total, which should be like sudoku table rows. For empty spaces 0 should be used. 

After all 9 rows are entered program tryes to solve the table using backpropagation algorithm. Simply said it tryes to find valid number in the next empty square and check
if the table was solved, program stops and if no value could be entered in the next empty box, it looks back to history and tries to alter previous change.

After all it will print the solved table
