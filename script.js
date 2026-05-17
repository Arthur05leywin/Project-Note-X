const navToggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".site-nav");

if (navToggle && nav) {
  navToggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });
}

const modeToggle = document.querySelector("[data-mode-toggle]");
if (modeToggle) {
  modeToggle.addEventListener("click", () => {
    document.body.classList.toggle("focus-mode");
  });
}