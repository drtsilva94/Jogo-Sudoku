import numpy as np
import random

def generate_sudoku(difficulty='medium'):
    def is_valid(board, row, col, num):
        # Check if num is not in the current row
        if num in board[row]:
            return False
        # Check if num is not in the current column
        if num in board[:, col]:
            return False
        # Check if num is not in the current 3x3 box
        box_row_start = row - row % 3
        box_col_start = col - col % 3
        if num in board[box_row_start:box_row_start + 3, box_col_start:box_col_start + 3]:
            return False
        return True

    def fill_board(board):
        for row in range(9):
            for col in range(9):
                if board[row, col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(board, row, col, num):
                            board[row, col] = num
                            if not np.any(board == 0) or fill_board(board):
                                return True
                            board[row, col] = 0
                    return False
        return True

    board = np.zeros((9, 9), dtype=int)
    fill_board(board)

    # Defina o número de células a serem removidas com base na dificuldade
    if difficulty == 'easy':
        num_cells_to_remove = random.randint(30, 40)
    elif difficulty == 'medium':
        num_cells_to_remove = random.randint(40, 50)
    elif difficulty == 'hard':
        num_cells_to_remove = random.randint(50, 60)

    # Remover números aleatórios para criar o quebra-cabeça
    for _ in range(num_cells_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row, col] == 0:  # Evitar remover a mesma célula mais de uma vez
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row, col] = 0

    return board