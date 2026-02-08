document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("nav");
  const hamburger = document.querySelector(".hamburger");
  const navLinks = Array.from(document.querySelectorAll("nav a"));

// Automatically apply system theme
const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
document.documentElement.setAttribute("data-theme", systemPrefersDark ? "dark" : "light");

// Optional: dynamically change theme if system preference changes
window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", e => {
  document.documentElement.setAttribute("data-theme", e.matches ? "dark" : "light");
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
      "Aspiring SOC Analyst",
      "Cybersecurity Internship Candidate",
      "IT Internship Candidate",
      "Defensive Security Enthusiast",
    ];
    let wordIndex = 0, charIndex = 0, isDeleting = false;

    const type = () => {
      const word = words[wordIndex];
      typedText.textContent = isDeleting
        ? word.substring(0, charIndex--)
        : word.substring(0, charIndex++);

      let delay = isDeleting ? 60 : 120;

      if (!isDeleting && charIndex === word.length + 1) {
        isDeleting = true;
        delay = 800;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        delay = 400;
      }

      setTimeout(type, delay);
    };
    setTimeout(type, 700);
  }

  // Hamburger Menu
  function openNav() {
    nav.classList.add("show");
    hamburger.classList.add("is-active");
    hamburger.setAttribute("aria-expanded", "true");
    // focus first link for accessibility
    const firstLink = nav.querySelector('a');
    firstLink && firstLink.focus();
    document.body.style.overflow = 'hidden';
  }
  function closeNav() {
    nav.classList.remove("show");
    hamburger.classList.remove("is-active");
    hamburger.setAttribute("aria-expanded", "false");
    hamburger.focus();
    document.body.style.overflow = '';
  }
  function toggleNav() {
    const isOpen = nav.classList.contains("show");
    isOpen ? closeNav() : openNav();
  }
  hamburger.addEventListener("click", toggleNav);
  hamburger.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      toggleNav();
    }
  });

  // Close nav on link click (mobile overlay)
  navLinks.forEach(a => a.addEventListener('click', () => {
    if (nav.classList.contains('show')) closeNav();
  }));

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('show')) closeNav();
  });

  // Active link highlight based on path
  const current = location.pathname.split('/').pop() || 'index.html';
  navLinks.forEach(a => {
    const href = a.getAttribute('href');
    if (href === current) a.classList.add('active');
  });
});

// === Certificate Popup Handling ===
document.querySelectorAll('.view-cert-text').forEach(trigger => {
  trigger.addEventListener('click', function (event) {
    event.stopPropagation();
    document.querySelectorAll('.popup').forEach(p => p.classList.remove('active'));

    const targetId = this.getAttribute('data-popup');
    const popup = document.getElementById(targetId);
    if (popup) popup.classList.add('active');
  });
});

document.addEventListener('click', () => {
  document.querySelectorAll('.popup').forEach(p => p.classList.remove('active'));
});

document.querySelectorAll('.popup').forEach(popup => {
  popup.addEventListener('click', e => e.stopPropagation());
});

document.querySelectorAll('.popup .close').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.closest('.popup').classList.remove('active');
  });
});
