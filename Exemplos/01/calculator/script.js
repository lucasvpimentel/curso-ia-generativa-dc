// Variáveis para armazenar o estado atual da calculadora
let currentOperand = ''; // Número que está sendo digitado atualmente
let previousOperand = ''; // Número anterior armazenado após escolher uma operação
let operation = undefined; // Operador atual (+, -, *, /)

// Seletores do DOM (ligando as variáveis aos elementos HTML)
const previousOperandTextElement = document.getElementById('previous-operand');
const currentOperandTextElement = document.getElementById('current-operand');
const numberButtons = document.querySelectorAll('[data-number]');
const operationButtons = document.querySelectorAll('[data-action]');
const equalsButton = document.getElementById('equals');
const clearButton = document.getElementById('clear');

// Função para limpar todos os dados do visor
function clear() {
    currentOperand = '0';
    previousOperand = '';
    operation = undefined;
}

// Função para remover o último dígito inserido
function deleteNumber() {
    if (currentOperand === '0') return;
    // Pega a string atual e remove o último caractere. Se ficar vazia, volta para '0'.
    currentOperand = currentOperand.toString().slice(0, -1);
    if (currentOperand === '') currentOperand = '0';
}

// Função para adicionar números no visor
function appendNumber(number) {
    // Evita adicionar mais de um ponto decimal na mesma operação
    if (number === '.' && currentOperand.includes('.')) return;
    // Substitui o '0' inicial, caso contrário concatena os números
    if (currentOperand === '0' && number !== '.') {
        currentOperand = number.toString();
    } else {
        currentOperand = currentOperand.toString() + number.toString();
    }
}

// Função executada ao clicar em um operador matemático (+, -, etc.)
function chooseOperation(op) {
    if (currentOperand === '' && op !== 'subtract') return;
    
    // Suporte para números negativos começando vazios
    if(currentOperand === '0' && op === 'subtract') {
        currentOperand = '-';
        updateDisplay();
        return;
    }

    if (currentOperand === '-') return; // Não faz nada se tiver só o sinal

    // Se já houver um número anterior armazenado, calcula o resultado parcial antes de seguir
    if (previousOperand !== '') {
        compute();
    }
    operation = op;
    // Passa o valor atual para o armazenador e limpa a tela principal para o próximo número
    previousOperand = currentOperand;
    currentOperand = '';
}

// Função principal de cálculo matemático
function compute() {
    let computation;
    const prev = parseFloat(previousOperand); // Converte string para número com casas decimais
    const current = parseFloat(currentOperand);
    
    // Se não for um número válido, não faz o cálculo
    if (isNaN(prev) || isNaN(current)) return;

    // Executa a operação baseada no operador escolhido
    switch (operation) {
        case 'add':
            computation = prev + current;
            break;
        case 'subtract':
            computation = prev - current;
            break;
        case 'multiply':
            computation = prev * current;
            break;
        case 'divide':
            if (current === 0) {
                alert("Erro: Divisão por zero não é permitida.");
                clear();
                return;
            }
            computation = prev / current;
            break;
        default:
            return;
    }
    
    // Arredondamento para evitar problemas clássicos de JS (ex: 0.1 + 0.2)
    computation = Math.round(computation * 10000000000) / 10000000000;
    
    // Atualiza o estado
    currentOperand = computation.toString();
    operation = undefined;
    previousOperand = '';
}

// Formatação do número para colocar vírgulas nos milhares (opcional, melhoria de UX)
function getDisplayNumber(number) {
    if(number === '-') return '-';
    const stringNumber = number.toString();
    const integerDigits = parseFloat(stringNumber.split('.')[0]);
    const decimalDigits = stringNumber.split('.')[1];
    let integerDisplay;
    
    if (isNaN(integerDigits)) {
        integerDisplay = '';
    } else {
        integerDisplay = integerDigits.toLocaleString('pt-BR', { maximumFractionDigits: 0 });
    }
    
    if (decimalDigits != null) {
        return `${integerDisplay},${decimalDigits}`; // Troca ponto por vírgula para visual BR
    } else {
        return integerDisplay;
    }
}

// Atualiza os elementos HTML com os valores das variáveis de estado
function updateDisplay() {
    if(currentOperand === '0' || currentOperand === '') {
         currentOperandTextElement.innerText = currentOperand === '' ? '0' : currentOperand;
    } else {
         // Exibe os números em formato pt-BR no front-end, mantendo em inglês na lógica
         let display = currentOperand.replace('.', ',');
         currentOperandTextElement.innerText = display;
    }

    if (operation != null) {
        // Mapeia o nome da operação para o símbolo correto
        let symbol = '';
        if(operation === 'add') symbol = '+';
        if(operation === 'subtract') symbol = '−';
        if(operation === 'multiply') symbol = '×';
        if(operation === 'divide') symbol = '÷';

        // Mostra a operação parcial no visor superior
        let displayPrev = previousOperand.replace('.', ',');
        previousOperandTextElement.innerText = `${displayPrev} ${symbol}`;
    } else {
        previousOperandTextElement.innerText = '';
    }
}

// ---- Event Listeners (Tratamento de cliques do usuário) ----

// Clique nos números
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        appendNumber(button.innerText);
        updateDisplay();
    });
});

// Clique nas operações
operationButtons.forEach(button => {
    button.addEventListener('click', () => {
        if(button.dataset.action === 'delete') {
            deleteNumber();
        } else {
            chooseOperation(button.dataset.action);
        }
        updateDisplay();
    });
});

// Clique no igual
equalsButton.addEventListener('click', button => {
    compute();
    updateDisplay();
});

// Clique no limpar (C)
clearButton.addEventListener('click', button => {
    clear();
    updateDisplay();
});

// ---- Suporte ao teclado (Melhoria extra solicitada no plano) ----
document.addEventListener('keydown', (event) => {
    // Teclas numéricas
    if ((event.key >= 0 && event.key <= 9) || event.key === '.' || event.key === ',') {
        let key = event.key === ',' ? '.' : event.key; // Converte vírgula para ponto pro motor
        appendNumber(key);
        updateDisplay();
    }
    // Teclas de operação
    if (event.key === '+') {
        chooseOperation('add'); updateDisplay();
    }
    if (event.key === '-') {
        chooseOperation('subtract'); updateDisplay();
    }
    if (event.key === '*') {
        chooseOperation('multiply'); updateDisplay();
    }
    if (event.key === '/') {
        event.preventDefault(); // Impede busca no navegador
        chooseOperation('divide'); updateDisplay();
    }
    // Enter ou igual
    if (event.key === 'Enter' || event.key === '=') {
        event.preventDefault(); // Impede o envio de form ou outro comportamento padrão
        compute(); updateDisplay();
    }
    // Backspace para apagar 1 caractere
    if (event.key === 'Backspace') {
        deleteNumber(); updateDisplay();
    }
    // Esc ou 'c' para limpar tudo
    if (event.key === 'Escape' || event.key.toLowerCase() === 'c') {
        clear(); updateDisplay();
    }
});

// Inicializa a tela com o valor zerado
clear();
updateDisplay();
