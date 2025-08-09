document
  .getElementById("registrationForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent actual form submission for demo

    const formElements = event.target.elements;
    const feedback = document.getElementById("formFeedback");

    feedback.innerHTML = ""; // Clear previous messages

    let valid = true;

    for (let element of formElements) {
      if (element.type !== "submit" && element.required && !element.value) {
        element.classList.add("is-invalid");
        feedback.innerHTML += `<p class="text-danger">The ${element.previousElementSibling.textContent} field is required.</p>`;
        valid = false;
      } else {
        element.classList.remove("is-invalid");
        element.classList.add("is-valid");
      }
    }

    if (valid) {
      feedback.innerHTML =
        '<p class="text-success">Registration successful!</p>';
    }
  });

document.addEventListener("DOMContentLoaded", function () {
  const pwdFields = document.querySelectorAll("input[type='password']");
  pwdFields.forEach((field) => {
    const toggleBtn = document.createElement("small");
    toggleBtn.innerText = "Show";
    toggleBtn.style.cursor = "pointer";
    toggleBtn.classList.add("ms-2", "text-primary");
    field.parentElement.appendChild(toggleBtn);

    toggleBtn.addEventListener("click", function () {
      if (field.type === "password") {
        field.type = "text";
        this.innerText = "Hide";
      } else {
        field.type = "password";
        this.innerText = "Show";
      }
    });
  });
});
