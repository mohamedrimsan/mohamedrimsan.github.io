document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  const nav = document.querySelector("nav");
  const hamburger = document.querySelector(".hamburger");

  // Theme Setup
  let savedTheme = localStorage.getItem("theme") || (
    window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"
  );
  document.documentElement.setAttribute("data-theme", savedTheme);
  if (themeToggle) themeToggle.checked = savedTheme === "dark";

  themeToggle?.addEventListener("change", function () {
    const newTheme = this.checked ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
  });

  // Greeting Message
  const greetingElement = document.getElementById("greeting");
  if (greetingElement) {
    const hour = new Date().getHours();
    greetingElement.textContent =
      hour < 12 ? "Good Morning ☀️" :
      hour < 15 ? "Good Afternoon 🌤️" :
                  "Good Evening 🌙";
  }
  // Typing Effect
  const typedText = document.getElementById("typed-text");
  if (typedText) {
    const words = [
      "an IT Undergraduate",
      "a Defensive Cybersecurity Enthusiast",
      "a Tech Enthusiast"
    ];
    let wordIndex = 0, charIndex = 0, isDeleting = false;

    const type = () => {
      const word = words[wordIndex];
      typedText.textContent = isDeleting
        ? word.substring(0, charIndex--)
        : word.substring(0, charIndex++);

      let delay = isDeleting ? 75 : 150;

      if (!isDeleting && charIndex === word.length + 1) {
        isDeleting = true;
        delay = 1000;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        delay = 500;
      }

      setTimeout(type, delay);
    };
    setTimeout(type, 1000);
  }

  // Hamburger Menu
  hamburger.addEventListener("click", () => {
    nav.classList.toggle("show");
  });
});
