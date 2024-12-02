import time

class DragonKingsSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.fundamental_solutions = set()

    def solve(self):
        self.place_dragon_king([-1] * self.n, 0)
        
        print(f"Total solutions: {len(self.solutions)}")
        print(f"Fundamental solutions: {len(self.fundamental_solutions)}")
        
        print("\nFundamental Solutions:")
        for solution in sorted(self.fundamental_solutions):
            print(solution)

    def place_dragon_king(self, board, row):
        if row == self.n:
            self.add_solution(board)
            return

        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row] = col
                self.place_dragon_king(board, row + 1)
                board[row] = -1

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row) or abs(board[i] - col) <= 1 and abs(i - row) <= 1:
                return False
        return True

    def add_solution(self, board):
        self.solutions.append(board[:])
        fundamental = self.get_fundamental_representation(board)
        self.fundamental_solutions.add(fundamental)

    def get_fundamental_representation(self, board):
        representations = [
            ','.join(map(str, board)),
            ','.join(map(str, reversed(board))),
            ','.join(map(str, [self.n - 1 - x for x in board])),
            ','.join(map(str, reversed([self.n - 1 - x for x in board])))
        ]
        return min(representations)

def main():
    n = int(input("Enter the board size (n): "))
    
    start_time = time.time()
    solver = DragonKingsSolver(n)
    solver.solve()
    end_time = time.time()
    
    print(f"\nTime taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
