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