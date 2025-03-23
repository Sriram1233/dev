document.getElementById("regi").addEventListener("submit", function (e) {
  e.preventDefault();
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phn").value.trim();
  const passwor = document.getElementById("psd").value.trim();
  const cpasswor = document.getElementById("cpsd").value.trim();

  if (name === "") {
    alert("name is required");
    return;
  }

  if (email === "") {
    alert("email must");
    return;
  }

//   const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//   if (!emailRegex.test(email)) {
//     alert("Please enter a valid email.");
//     return;
//   }

  const phoneRegex = /^[0-9]{10}$/;
  if (!phoneRegex.test(phone)) {
    alert("Please enter a valid 10-digit phone number.");
    return;
  }

  if (passwor.length < 6) {
    alert("Password must be at least 6 characters.");
    return;
  }

  if (passwor !== cpasswor) {
    alert("Passwords do not match.");
    return;
  }

  document.getElementById("gender").addEventListener("change", function () {
    if (this.value) {
      alert("You selected: " + this.value);
    } else {
      alert("Please select a gender.");
    }
  });

  alert('register success');
});
