function checkAnswer(selected, correct) {
    fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ selected, correct })
    })
    .then(response => response.json())
    .then(data => {
        const resultText = data.result ? "Correct!" : "Wrong!";
        document.getElementById("result").innerText = resultText;
        speak(resultText);
    });
}

function speak(text) {
    const msg = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(msg);
}