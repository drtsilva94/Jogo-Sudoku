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
    # Logic to check if the Sudoku is solved correctly
    # ...

    # Example placeholder
    if not np.any(current_sudoku == 0):
        message = "Sudoku solucionado corretamente!"
    else:
        message = "O Sudoku ainda não está completo."
        
    return render_template('sudoku.html', sudoku=current_sudoku.tolist(), message=message, initial_values=initial_values.tolist())

if __name__ == '__main__':
    app.run(debug=False)