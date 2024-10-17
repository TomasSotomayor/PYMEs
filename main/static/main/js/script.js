function toggleButtons() {
    var buttonContainer = document.getElementById("button-container");
    if (buttonContainer.style.display === "none" || buttonContainer.style.display === "") {
        buttonContainer.style.display = "block";
    } else {
        buttonContainer.style.display = "none";
    }
}
