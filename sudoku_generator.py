import numpy as np
import random

def generate_sudoku(difficulty='medium'):
    """Gera um tabuleiro de Sudoku com base na dificuldade especificada."""

    def is_valid(board, row, col, num):
        """Verifica se um número pode ser colocado em uma posição específica no tabuleiro."""
        # Verifica a linha
        if num in board[row]:
            return False
        # Verifica a coluna
        if num in board[:, col]:
            return False
        # Verifica a subgrade 3x3
        box_row_start = row - row % 3
        box_col_start = col - col % 3
        if num in board[box_row_start:box_row_start + 3, box_col_start:box_col_start + 3]:
            return False
        return True

    def fill_board(board):
        """Preenche o tabuleiro com uma solução completa e válida de Sudoku."""
        for row in range(9):
            for col in range(9):
                if board[row, col] == 0:  # Procura por células vazias
                    numbers = list(range(1, 10))  # Gera uma lista de números de 1 a 9
                    random.shuffle(numbers)  # Embaralha os números para aleatoriedade
                    for num in numbers:
                        if is_valid(board, row, col, num):
                            board[row, col] = num  # Coloca o número se válido
                            # Continua preenchendo recursivamente; retorna True se completo
                            if not np.any(board == 0) or fill_board(board):
                                return True
                            board[row, col] = 0  # Reseta a célula se o preenchimento falhar
                    return False  # Retorna False se não puder preencher a célula atual
        return True  # Retorna True se o tabuleiro estiver completo

    # Cria um tabuleiro vazio e preenche-o completamente
    board = np.zeros((9, 9), dtype=int)
    fill_board(board)

    # Define o número de células a serem removidas com base na dificuldade
    if difficulty == 'easy':
        num_cells_to_remove = random.randint(30, 40)
    elif difficulty == 'medium':
        num_cells_to_remove = random.randint(40, 50)
    elif difficulty == 'hard':
        num_cells_to_remove = random.randint(50, 60)
    else:
        raise ValueError("Dificuldade inválida. Escolha 'easy', 'medium' ou 'hard'.")

    # Remove números aleatórios para criar o quebra-cabeça
    cells_removed = 0  # Contador de células removidas
    while cells_removed < num_cells_to_remove:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row, col] != 0:  # Evita remover a mesma célula mais de uma vez
            board[row, col] = 0
            cells_removed += 1

    return board  # Retorna o tabuleiro de Sudoku com células removidas para o quebra-cabeça
