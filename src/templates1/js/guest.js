function copy() {
    var text = document.getElementById("gmail");
    navigator.clipboard.writeText(text.textContent);
}