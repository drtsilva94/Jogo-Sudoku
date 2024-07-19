from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

def generate_sudoku():
    # Função para gerar um novo Sudoku
    # Aqui você deve substituir com sua lógica de geração de Sudoku
    return np.zeros((9, 9), dtype=int)  # Sudoku vazio para exemplo

@app.route('/')
def index():
    grid = generate_sudoku()
    return render_template('sudoku.html', sudoku=grid.tolist())

@app.route('/new_game')
def new_game():
    grid = generate_sudoku()
    return render_template('sudoku.html', sudoku=grid.tolist())

@app.route('/check', methods=['POST'])
def check():
    # Função para verificar o Sudoku
    # Aqui você deve adicionar sua lógica de verificação
    grid = generate_sudoku()  # Para fins de exemplo, estamos apenas gerando um novo Sudoku
    return render_template('sudoku.html', sudoku=grid.tolist(), message="Novo jogo gerado!")

if __name__ == '__main__':
    app.run(debug=True)