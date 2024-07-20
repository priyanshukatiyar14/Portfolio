document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".project").forEach((project) => {
    project.addEventListener("click", function () {
      const url = this.getAttribute("data-url");
      if (url) {
        window.location.href = url; // Use window.location.href for redirection within the same tab
      }
    });
  });
});
