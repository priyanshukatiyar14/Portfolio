document.addEventListener("DOMContentLoaded", () => {
  const typingElement = document.querySelector(".typing");
  const words = [
    "Python Development",
    "Java Development",
    "Full Stack Development",
  ];
  let wordIndex = 0;
  let letterIndex = 0;
  let currentWord = words[wordIndex];
  let isDeleting = false;
  let typingSpeed = 200;
  let deletingSpeed = 100;

  function type() {
    typingElement.textContent = currentWord.slice(0, letterIndex);
    if (!isDeleting && letterIndex < currentWord.length) {
      letterIndex++;
      setTimeout(type, typingSpeed);
    } else if (isDeleting && letterIndex > 0) {
      letterIndex--;
      setTimeout(type, deletingSpeed);
    } else if (!isDeleting && letterIndex === currentWord.length) {
      isDeleting = true;
      setTimeout(type, 1000);
    } else if (isDeleting && letterIndex === 0) {
      isDeleting = false;
      wordIndex++;
      if (wordIndex === words.length) {
        wordIndex = 0;
      }
      currentWord = words[wordIndex];
      setTimeout(type, 500);
    }
  }

  type();

  // Menu toggle
  const menuIcon = document.querySelector(".menu-icon");
  const menuItems = document.querySelector(".menu-items");

  menuIcon.addEventListener("click", () => {
    menuItems.classList.toggle("active");
  });
});
