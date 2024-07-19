from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from sudoku_generator import generate_sudoku

app = Flask(__name__)

# Store the current Sudoku puzzle
current_sudoku = generate_sudoku()

@app.route('/')
def index():
    global current_sudoku
    return render_template('sudoku.html', sudoku=current_sudoku.tolist())

@app.route('/new_game')
def new_game():
    global current_sudoku
    current_sudoku = generate_sudoku()
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
        
    return render_template('sudoku.html', sudoku=current_sudoku.tolist(), message=message)

if __name__ == '__main__':
    app.run(debug=False)