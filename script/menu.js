
let menuButton = document.getElementById('menu-button').addEventListener("click", displayNavMenu);

function displayNavMenu() {
  let navListSmall = document.getElementById('navigation-list-small-js');
  if (navListSmall.style.display === "none") {
    navListSmall.style.display = "grid";
    // navListSmall.style.transition = "0.8s";
  } else {
    navListSmall.style.display = "none";
  }
}
