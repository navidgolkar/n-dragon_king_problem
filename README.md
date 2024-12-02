# n-dragon_king_problem
This program solves a variation of the n-Queens problem, where instead of a queen, it considers the movement and placement of a Dragon King from the game Shogi. In the Shogi game, the Dragon King is a piece that can move like a rook (horizontally or vertically) and a king (adjacent squares), making its placement more restricted than the traditional queen.

The program's goal is to place n Dragon Kings on an n x n board such that no two Dragon Kings threaten each other. The program efficiently finds all possible configurations where the Dragon Kings are placed on the board, ensuring they do not attack one another according to the movement rules.

Key features of the program:

1. Fundamental Solutions: The program handles symmetry by generating only unique solutions. It transforms each solution into its fundamental representation (taking into account rotations and reflections) and eliminates duplicates.
2. Output Format: The fundamental solutions are displayed in an n x n matrix format, where 1 represents the placement of a Dragon King and 0 represents an empty square. This helps visualize the board configuration for each solution.
3. Performance: The program measures and prints the time taken to solve the problem, offering insights into the efficiency of the algorithm.
