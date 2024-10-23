function profileOptions() {
    var profileOptions = document.getElementById("profile-options");
    var configOptions = document.getElementById("config-options");
    if (configOptions.style.display === "block") {
        configOptions.style.display = "none";
    }
    if (profileOptions.style.display === "none" || profileOptions.style.display === "") {
        profileOptions.style.display = "block";
    } else {
        profileOptions.style.display = "none";
    }
}

function configOptions() {
    var configOptions = document.getElementById("config-options");
    var profileOptions = document.getElementById("profile-options");
    if (profileOptions.style.display === "block") {
        profileOptions.style.display = "none";
    }
    if (configOptions.style.display === "none" || configOptions.style.display === "") {
        configOptions.style.display = "block";
    } else {
        configOptions.style.display = "none";
    }
}

const toggleButton = document.getElementById('theme-toggle');
const currentTheme = localStorage.getItem('theme');

// Aplica el tema almacenado si existe
if (currentTheme === 'light') {
document.body.classList.add('light-mode');
toggleButton.textContent = 'Cambiar a modo oscuro';
}

toggleButton.addEventListener('click', function() {
document.body.classList.toggle('light-mode');

// Cambiar el texto del botón
if (document.body.classList.contains('light-mode')) {
    toggleButton.textContent = 'Cambiar a modo oscuro';
    localStorage.setItem('theme', 'light');
} else {
    toggleButton.textContent = 'Cambiar a modo claro';
    localStorage.setItem('theme', 'dark');
}
});
