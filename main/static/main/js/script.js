function profileOptions() {
    var profileOptions = document.getElementById("profile-options");
    if (profileOptions.style.display === "none" || profileOptions.style.display === "") {
        profileOptions.style.display = "block";
    } else {
        profileOptions.style.display = "none";
    }
}