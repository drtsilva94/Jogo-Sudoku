document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('sudoku-container');
    const newGameBtn = document.getElementById('new-game-btn');
    const gridSize = 9;
    const cells = [];

    function createSudokuGrid() {
        container.innerHTML = '';
        for (let i = 0; i < gridSize * gridSize; i++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            const input = document.createElement('input');
            input.type = 'text';
            input.maxLength = 9;
            input.addEventListener('input', handleInput);
            cell.appendChild(input);
            container.appendChild(cell);
            cells.push(cell);
        }
    }

    function handleInput(event) {
        const input = event.target;
        const cell = input.parentElement;
        const value = input.value;

        if (value.length > 1) {
            cell.innerHTML = '';
            const miniGrid = document.createElement('div');
            miniGrid.className = 'mini-grid';

            value.split('').forEach((char, index) => {
                const miniCell = document.createElement('div');
                miniCell.textContent = char;
                miniGrid.appendChild(miniCell);
            });

            cell.appendChild(miniGrid);
        }
    }

    newGameBtn.addEventListener('click', createSudokuGrid);

    createSudokuGrid();
});

 // Funções para alternar tamanhos
 function setGridSize(size) {
    const cells = document.querySelectorAll('.cell');
    cells.forEach(cell => {
        if (size === 'small') {
            cell.style.width = '30px';
            cell.style.height = '30px';
        } else {
            cell.style.width = '50px';
            cell.style.height = '50px';
        }
    });

    const inputs = document.querySelectorAll('.cell input');
    inputs.forEach(input => {
        if (size === 'small') {
            input.style.fontSize = '1rem';
        } else {
            input.style.fontSize = '1.5rem';
        }
    });

    const miniGrids = document.querySelectorAll('.mini-grid');
    miniGrids.forEach(miniGrid => {
        if (size === 'small') {
            miniGrid.style.fontSize = '0.3rem';
        } else {
            miniGrid.style.fontSize = '0.5rem';
        }
    });
}

// Event listeners para os botões de tamanho
const smallSizeBtn = document.createElement('button');
smallSizeBtn.innerText = 'Pequeno';
smallSizeBtn.addEventListener('click', () => setGridSize('small'));

const normalSizeBtn = document.createElement('button');
normalSizeBtn.innerText = 'Normal';
normalSizeBtn.addEventListener('click', () => setGridSize('normal'));

document.body.insertBefore(smallSizeBtn, container);
document.body.insertBefore(normalSizeBtn, container);
});