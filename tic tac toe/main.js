document.addEventListener('DOMContentLoaded', () => {
    const gameBoard = document.getElementById('game');
    const difficultySelect = document.getElementById('difficulty');
    const cells = Array(9).fill(null);
    let currentPlayer = 'X';

    function createBoard() {
        gameBoard.innerHTML = '';
        cells.forEach((_, index) => {
            const cell = document.createElement('div');
            cell.classList.add('border', 'border-gray-400', 'flex', 'items-center', 'justify-center', 'text-2xl', 'cursor-pointer');
            cell.addEventListener('click', () => handleCellClick(index));
            gameBoard.appendChild(cell);
        });
    }

    function handleCellClick(index) {
        if (!cells[index]) {
            cells[index] = currentPlayer;
            renderBoard();
            playSound(currentPlayer);
            if (checkWin()) {
                alert(`${currentPlayer} wins!`);
                resetGame();
            } else if (cells.every(cell => cell)) {
                alert('Draw!');
                resetGame();
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
                if (currentPlayer === 'O') {
                    cpuMove();
                }
            }
        }
    }

    function renderBoard() {
        gameBoard.childNodes.forEach((cell, index) => {
            cell.textContent = cells[index];
        });
    }

    function checkWin() {
        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ];
        return winPatterns.some(pattern => 
            pattern.every(index => cells[index] === currentPlayer)
        );
    }

    function cpuMove() {
        const difficulty = difficultySelect.value;
        if (difficulty === 'easy') {
            randomMove();
        } else {
            minimaxMove();
        }
    }

    function randomMove() {
        const emptyCells = cells.map((cell, index) => cell === null ? index : null).filter(index => index !== null);
        const randomIndex = emptyCells[Math.floor(Math.random() * emptyCells.length)];
        handleCellClick(randomIndex);
    }

    function minimaxMove() {
        const bestMove = minimax(cells, 'O').index;
        handleCellClick(bestMove);
    }

    function minimax(newBoard, player) {
        const availSpots = newBoard.map((cell, index) => cell === null ? index : null).filter(index => index !== null);

        if (checkWinCondition(newBoard, 'X')) {
            return { score: -10 };
        } else if (checkWinCondition(newBoard, 'O')) {
            return { score: 10 };
        } else if (availSpots.length === 0) {
            return { score: 0 };
        }

        const moves = [];
        for (let i = 0; i < availSpots.length; i++) {
            const move = {};
            move.index = availSpots[i];
            newBoard[availSpots[i]] = player;

            if (player === 'O') {
                const result = minimax(newBoard, 'X');
                move.score = result.score;
            } else {
                const result = minimax(newBoard, 'O');
                move.score = result.score;
            }

            newBoard[availSpots[i]] = null;
            moves.push(move);
        }

        let bestMove;
        if (player === 'O') {
            let bestScore = -Infinity;
            for (let i = 0; i < moves.length; i++) {
                if (moves[i].score > bestScore) {
                    bestScore = moves[i].score;
                    bestMove = i;
                }
            }
        } else {
            let bestScore = Infinity;
            for (let i = 0; i < moves.length; i++) {
                if (moves[i].score < bestScore) {
                    bestScore = moves[i].score;
                    bestMove = i;
                }
            }
        }

        return moves[bestMove];
    }

    function checkWinCondition(board, player) {
        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ];
        return winPatterns.some(pattern => 
            pattern.every(index => board[index] === player)
        );
    }

    function resetGame() {
        cells.fill(null);
        currentPlayer = 'X';
        createBoard();
    }

    createBoard();

    const xSound = new Audio('x-sound.mp3');
    const oSound = new Audio('o-sound.mp3');

    function playSound(player) {
        if (player === 'X') {
             xSound.play();
            } else {
                oSound.play();
            }
}
});


