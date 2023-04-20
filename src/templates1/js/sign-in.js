function flip() {
    document.getElementById("inside").style.transform = 'rotateY(0.5turn)';
    document.getElementById("register").style.clipPath = "circle(75%)";
    document.getElementById("login").style.display = "none";
    document.getElementById("right").style.backgroundColor = "transparent";
}

function rflip() {
    document.getElementById("register").style.clipPath = "circle(0%)";
    document.getElementById("inside").style.transform = 'rotateY(0turn)';
    document.getElementById("login").style.display = "contents";
    document.getElementById("right").style.backgroundColor = "#201f1fdf";
}

var current = null;
document.querySelector('#username').addEventListener('focus', function(e) {
    if (current) current.pause();
    current = anime({
        targets: 'path',
        strokeDashoffset: {
            value: 0,
            duration: 700,
            easing: 'easeOutQuart'
        },
        strokeDasharray: {
            value: '240 1386',
            duration: 700,
            easing: 'easeOutQuart'
        }
    });
});
document.querySelector('#password').addEventListener('focus', function(e) {
    if (current) current.pause();
    current = anime({
        targets: 'path',
        strokeDashoffset: {
            value: -336,
            duration: 700,
            easing: 'easeOutQuart'
        },
        strokeDasharray: {
            value: '240 1386',
            duration: 700,
            easing: 'easeOutQuart'
        }
    });
});
document.querySelector('#submit').addEventListener('focus', function(e) {
    if (current) current.pause();
    current = anime({
        targets: 'path',
        strokeDashoffset: {
            value: -730,
            duration: 700,
            easing: 'easeOutQuart'
        },
        strokeDasharray: {
            value: '530 1386',
            duration: 700,
            easing: 'easeOutQuart'
        }
    });
});