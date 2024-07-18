from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    grid = np.zeros((9, 9), dtype=int)  # Exemplo de grid vazio
    return render_template('sudoku.html', sudoku=grid.tolist())

# Adicionar 'enumerate' ao ambiente global do Jinja2
app.jinja_env.globals.update(enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)