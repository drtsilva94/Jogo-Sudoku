from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from sudoku_generator import generate_sudoku

app = Flask(__name__)

# Store the current Sudoku puzzle and the cells that are initially filled
current_sudoku = generate_sudoku()
initial_values = np.copy(current_sudoku)  # Store initial values to determine editable cells

@app.route('/')
def index():
    global current_sudoku, initial_values
    # Pass the initial values to the template to determine editable cells
    return render_template('sudoku.html', sudoku=current_sudoku.tolist(), initial_values=initial_values.tolist())

@app.route('/multi_numbers')
def multi_numbers():
    global current_sudoku
    return render_template('sudoku_multi_numbers.html', sudoku=current_sudoku.tolist())

@app.route('/new_game')
def new_game():
    global current_sudoku, initial_values
    current_sudoku = generate_sudoku()
    initial_values = np.copy(current_sudoku)  # Update initial values for the new game
    return redirect(url_for('index'))

@app.route('/check', methods=['POST'])
def check():
    global current_sudoku
    
    # Verificar se o Sudoku está resolvido corretamente
    def is_sudoku_solved(sudoku):
        for row in sudoku:
            if not np.array_equal(np.sort(row), np.arange(1, 10)):
                return False
        
        for col in sudoku.T:
            if not np.array_equal(np.sort(col), np.arange(1, 10)):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = sudoku[i:i+3, j:j+3].flatten()
                if not np.array_equal(np.sort(block), np.arange(1, 10)):
                    return False
        
        return True
    
   # Parse the form data into the current_sudoku array
    for i in range(9):
        for j in range(9):
            cell_value = request.form.get(f'cell-{i}-{j}')
            if cell_value and cell_value.isdigit():
                current_sudoku[i][j] = int(cell_value)
            else:
                current_sudoku[i][j] = initial_values[i][j]  # Preserve initial values

    # Check if the Sudoku is solved
    if is_sudoku_solved(current_sudoku):
        message = "Sudoku solucionado corretamente!"
    else:
        message = "O Sudoku ainda não está completo ou contém erros."
    
    return render_template('sudoku.html', sudoku=current_sudoku.tolist(), message=message, initial_values=initial_values.tolist())

if __name__ == '__main__':
    app.run(debug=False)