function toggleButtons() {
    var buttonContainer = document.getElementById("button-container");
    if (buttonContainer.style.display === "none" || buttonContainer.style.display === "") {
        buttonContainer.style.display = "block";
    } else {
        buttonContainer.style.display = "none";
    }
}

function openModal() {
    document.getElementById('profileOptions').style.display = 'flex';
}

function closeModal() {
    document.getElementById('profileOptions').style.display = 'none';
}