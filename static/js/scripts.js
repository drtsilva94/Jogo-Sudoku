// Executa o código quando o conteúdo da página é totalmente carregado
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('sudoku-container'); // Container para o tabuleiro de Sudoku
    const newGameBtn = document.getElementById('new-game-btn'); // Botão para iniciar um novo jogo
    const gridSize = 9; // Tamanho da grade (9x9)
    const cells = []; // Armazena as células criadas

    // Função para criar o tabuleiro de Sudoku
    function createSudokuGrid() {
        container.innerHTML = ''; // Limpa o container para o novo tabuleiro
        cells.length = 0; // Limpa o array de células

        // Cria as células do tabuleiro
        for (let i = 0; i < gridSize * gridSize; i++) {
            const cell = document.createElement('div'); // Elemento de célula
            cell.className = 'cell'; // Adiciona a classe 'cell' para estilização
            const input = document.createElement('input'); // Elemento de entrada de texto para cada célula
            input.type = 'text';
            input.maxLength = 9; // Define o limite de 9 caracteres
            input.addEventListener('input', handleInput); // Adiciona evento para manipular a entrada do usuário
            cell.appendChild(input); // Anexa o input à célula
            container.appendChild(cell); // Adiciona a célula ao container
            cells.push(cell); // Armazena a célula na lista de células
        }
    }

    // Manipula a entrada do usuário na célula
    function handleInput(event) {
        const input = event.target;
        const cell = input.parentElement;
        const value = input.value;

        if (value.length > 1) { // Verifica se há mais de um número inserido
            cell.innerHTML = ''; // Limpa o conteúdo da célula

            // Cria uma mini-grade para exibir múltiplos números
            const miniGrid = document.createElement('div');
            miniGrid.className = 'mini-grid'; // Aplica a classe de mini-grade

            // Adiciona cada número como um elemento separado dentro da mini-grade
            value.split('').forEach((char) => {
                const miniCell = document.createElement('div'); // Elemento para cada número
                miniCell.textContent = char; // Define o número no mini-elemento
                miniGrid.appendChild(miniCell); // Adiciona o mini-elemento à mini-grade
            });

            cell.appendChild(miniGrid); // Adiciona a mini-grade à célula
        }
    }

    // Evento para o botão de novo jogo, recriando a grade
    newGameBtn.addEventListener('click', createSudokuGrid);

    // Inicializa o tabuleiro de Sudoku ao carregar a página
    createSudokuGrid();

    // Função para ajustar o tamanho da grade do Sudoku
    function setGridSize(size) {
        const cells = document.querySelectorAll('.cell'); // Seleciona todas as células
        cells.forEach(cell => {
            if (size === 'small') {
                cell.style.width = '30px';
                cell.style.height = '30px';
            } else {
                cell.style.width = '50px';
                cell.style.height = '50px';
            }
        });

        const inputs = document.querySelectorAll('.cell input'); // Seleciona todas as entradas das células
        inputs.forEach(input => {
            input.style.fontSize = size === 'small' ? '1rem' : '1.5rem';
        });

        const miniGrids = document.querySelectorAll('.mini-grid'); // Seleciona todas as mini-grades
        miniGrids.forEach(miniGrid => {
            miniGrid.style.fontSize = size === 'small' ? '0.3rem' : '0.5rem';
        });
    }

    // Criação dos botões para alternar tamanhos e adicionar seus eventos
    const smallSizeBtn = document.createElement('button');
    smallSizeBtn.innerText = 'Pequeno';
    smallSizeBtn.addEventListener('click', () => setGridSize('small'));

    const normalSizeBtn = document.createElement('button');
    normalSizeBtn.innerText = 'Normal';
    normalSizeBtn.addEventListener('click', () => setGridSize('normal'));

    // Insere os botões de tamanho no documento, antes do container do Sudoku
    document.body.insertBefore(smallSizeBtn, container);
    document.body.insertBefore(normalSizeBtn, container);
});
