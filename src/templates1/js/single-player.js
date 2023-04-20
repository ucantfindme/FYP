function copy() {
    var text = document.getElementById("gmail");
    navigator.clipboard.writeText(text.textContent);
}

const countdownNumberEl = document.getElementById("countdown-number");
let countdown = 60;
let interval;
countdownNumberEl.textContent = countdown;

const startTimer = () => {
    countdown = 60;

    clearInterval(interval);
    interval = setInterval(() => {
        countdown = --countdown <= 0 ? 0 : countdown;
        let foram = countdown >= 10 ? `${countdown}` : `0${countdown}`;
        countdownNumberEl.textContent = foram;
    }, 1000);
};
startTimer();