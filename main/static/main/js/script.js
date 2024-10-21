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