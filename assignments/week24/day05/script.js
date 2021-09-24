var words = ["elephant", "dog", "cat", "giraffe", "gorilla", "chimpanzee", "snake", "owl", "horse", "lion", "mouse", "gazelle", "eagle", "wolf", "donkey", "rhinoceros", "penguin", "flamingo", "seagull", "turtle"]; 
var buttons = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']; 
var mistakes = 6; 
var score = 0;
var failed = 0; 
var tries = []; 
var mystery;
var randNum;
var chosenWord;
var wordStatus = null;

function handleGuess(str) {
    tries.indexOf(str) === -1 ? tries.push(str) : null;
    document.getElementById("display2").value += str + " ";
    var button = document.getElementById(str);
    button.style.backgroundColor = "grey";
    button.disabled = true;

    if (chosenWord.indexOf(str) >= 0) {
        updateScore();
        guessedWord();
        checkIfGameWon();
    } else {
        failed++;
        updateMistakes();
        checkIfGameLost();
    }
}

function generateWord() { 
    randNum = Math.floor(Math.random() * words.length);
    chosenWord = words[randNum].toUpperCase();
}

function Start() { 
    generateWord();
    defaultImg();
    resetCanvas();
    mystery = chosenWord.replace(/[A-Z]/g, '_ ');
    console.log(chosenWord)
    tries = [];
    failed = 0;
    for (let i = 0; i < buttons.length; i++) {
        document.getElementById(buttons[i]).disabled = false;
        var kb = document.getElementById(buttons[i]);
        kb.style.backgroundColor = "red";
    }
    document.getElementById("display1").value = mystery;
    document.getElementById("display2").value = "";
    document.getElementById("score").value = score;
    document.getElementById("fails").value = failed;
    if (chosenWord.length >= 10) {
        showHint();
    }
}

function showHint() {
    var randNum = Math.floor(Math.random() * chosenWord.length);
    var randLetter = chosenWord[randNum];
    handleHint(randLetter);
}

function handleHint(str) {
    tries.push(str);
    var button = document.getElementById(str);
    button.style.backgroundColor = "grey";
    button.disabled = true;
    guessedWord()
}

function defaultImg() {
    var canvas = document.querySelector("canvas");
    canvas.setAttribute("style", "display: none;");
    var image = document.querySelector("img");
    image.setAttribute("style", "display: block;")
}

function replaceImg() {
    var image = document.querySelector("img");
    image.setAttribute("style", "display: none;")
    var can = document.querySelector("canvas");
    can.setAttribute("style", "display: block;")
}

function guessedWord() {
    wordStatus = chosenWord.split('').map(letter => (tries.indexOf(letter) >= 0 ? letter.toLowerCase() : "_ ")).join('');
    document.getElementById('display1').value = wordStatus;
}

function updateMistakes() {
    replaceImg();
    loadCanvasOnError();
    document.getElementById("score").value = score;
    document.getElementById('fails').value = failed;
}

function updateScore() {
    document.getElementById("score").value = score;
}

function checkIfGameWon() {
    if (wordStatus === chosenWord.toLowerCase()) {
        score++;
        for (let i = 0; i < buttons.length; i++) {
            document.getElementById(buttons[i]).disabled = true;
            var kb = document.getElementById(buttons[i]);
            kb.style.backgroundColor = "red";
        }
        updateScore();
        document.getElementById("display2").value = "You won!";
    }
}

function checkIfGameLost() {
    if (failed === mistakes) {
        score--;
        for (let i = 0; i < buttons.length; i++) {
            document.getElementById(buttons[i]).disabled = true;
            var kb = document.getElementById(buttons[i]);
            kb.style.backgroundColor = "red";
        }
        updateScore();
        document.getElementById('display1').value = chosenWord.toLowerCase();
        document.getElementById("display2").value = "Game over, you have lost!";
    }
}

function resetCanvas() {
    var canvas = document.querySelector("canvas");
    var context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
}

function loadCanvasOnError() {
    var hangman = document.querySelector("canvas");
    var h = hangman.getContext('2d');

    switch (failed) {
        case 1:
            h.beginPath();
            h.moveTo(75, 120);
            h.lineTo(170, 120);
            h.moveTo(100, 60);
            h.lineTo(130, 30);
            h.moveTo(100, 120);
            h.lineTo(100, 30);
            h.lineTo(180, 30);
            h.stroke();
            break;
        case 2:
            h.beginPath();
            h.moveTo(150, 30)
            h.lineTo(150, 90);
            h.arc(140, 50, 10, 0, Math.PI * 2, false);
            h.stroke();
            break;
        case 3:
            h.beginPath();
            h.moveTo(150, 65); 
            h.lineTo(135, 75); 
            h.stroke();
            break;
        case 4:
            h.moveTo(150, 65);
            h.lineTo(165, 75);
            h.stroke();
            break;
        case 5:
            h.beginPath();
            h.moveTo(150, 90); 
            h.lineTo(145, 110); 
            h.stroke();
            break;
        case 6:
            h.beginPath();
            h.moveTo(150, 90); 
            h.lineTo(155, 110); 
            h.moveTo(135, 47.5);  
            h.lineTo(137.5, 50); 
            h.moveTo(135, 50);
            h.lineTo(137.5, 47.5); 
            h.moveTo(142.5, 47.5); 
            h.lineTo(145, 50); 
            h.moveTo(142.5, 50); 
            h.lineTo(145, 47.5);
            h.moveTo(142.5, 56.5); 
            h.arc(140, 56.5, 3, 0, 1 * Math.PI, true); 
            h.stroke();

    }
}