var element = document.body;
// var togglebutton = document.getElementById("toggle");
const currentTheme = localStorage.getItem("theme");
console.log("helo", currentTheme);
// If the current theme in localStorage is "dark"...
if (currentTheme == "dark") {
  console.log("Its dark");
  // togglebutton.innerHTML = "Light Mode";
  element.classList.toggle("dark-mode");
  theme = "dark";
  localStorage.setItem("theme", theme);
} else {
  console.log("Its Light");
  // togglebutton.innerHTML = "Dark Mode";
  theme = "light";
  localStorage.setItem("theme", theme);
}

function myfun() {
  console.log("myFunction");
  const currentTheme = localStorage.getItem("theme");
  if (currentTheme == "dark") {
    console.log("prev itss dark now it is light");
    element.classList.toggle("dark-mode");
    theme = "light";
    localStorage.setItem("theme", theme);
    // togglebutton.innerHTML = "Dark Mode";
  } else {
    console.log("prev is light now its dark");
    element.classList.toggle("dark-mode");
    theme = "dark";
    localStorage.setItem("theme", theme);
    // togglebutton.innerHTML = "Light Mode";
  }
}
