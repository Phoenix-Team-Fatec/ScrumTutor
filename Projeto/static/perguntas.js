function checkAnswer(question, clickedButton) {
    var buttons = document.querySelectorAll('[data-question="' + question + '"]');
    var correctAnswer;
    var wrongAnswers = [];

    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i].getAttribute('data-answer') === 'correct') {
            correctAnswer = buttons[i];
        } else {
            wrongAnswers.push(buttons[i]);
        }
    }

    for (var i = 0; i < wrongAnswers.length; i++) {
        wrongAnswers[i].style.backgroundColor = '#FF7070';
    }
    correctAnswer.style.backgroundColor = '#79FBAD';
    clickedButton.style.backgroundColor = clickedButton.getAttribute('data-answer') === 'correct' ? '#79FBAD' : '#FF7070';
}