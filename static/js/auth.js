//password functionaliy
function togglePasswordVisibility() {
  var passwordField = document.getElementById("id_password");
  var eyeIcon = document.getElementById("eyeIcon");
  if (passwordField.type === "password") {
    passwordField.type = "text";
    eyeIcon.classList.remove("bi-eye");
    eyeIcon.classList.add("bi-eye-slash");
  } else {
    passwordField.type = "password";
    eyeIcon.classList.remove("bi-eye-slash");
    eyeIcon.classList.add("bi-eye");
  }
}

function togglePasswordVisibility1() {
  var passwordField = document.getElementById("id_password2");
  var eyeIcon = document.getElementById("eyeIcon1");
  if (passwordField.type === "password") {
    passwordField.type = "text";
    eyeIcon.classList.remove("bi-eye");
    eyeIcon.classList.add("bi-eye-slash");
  } else {
    passwordField.type = "password";
    eyeIcon.classList.remove("bi-eye-slash");
    eyeIcon.classList.add("bi-eye");
  }
}
//signup functionality
const staff = document.querySelector(".staff");
const student = document.querySelector(".student");
const lib_user = document.querySelector(".lib_user");
const card_id = document.querySelector(".card_id");
var a = document.querySelector("#designation_1");
var b = document.querySelector("#designation_2");
var c = document.querySelector("#library_user_1");
var d = document.querySelector("#library_user_2");
a.addEventListener("click", function () {
  if (staff.style.display === "none") {
    staff.style.display = "block";
    student.style.display = "none";
    lib_user.style.display = "none";
    card_id.style.display = "none";
    document.getElementById("staff_id").required = true;
    document.getElementById("matric_no").required = false;
    document.getElementById("library_user_1").required = false;
    document.getElementById("library_user_2").required = false;
    document.getElementById("library_user_1").checked = false;
    document.getElementById("library_user_2").checked = false;
    document.getElementById("matric_no").value = "";
    document.querySelector(".password").style.display = "flex";
  }
});

b.addEventListener("click", function () {
  if (student.style.display === "none") {
    student.style.display = "block";
    staff.style.display = "none";
    lib_user.style.display = "flex";
    document.getElementById("staff_id").required = false;
    document.getElementById("matric_no").required = true;
    document.getElementById("library_user_1").required = true;
    document.getElementById("library_user_2").required = true;
    document.getElementById("staff_id").value = "";
    document.querySelector(".password").style.display = "flex";
  }
});
c.addEventListener("click", function () {
  if (card_id.style.display === "none") {
    card_id.style.display = "block";
    document.getElementById("library_id").required = true;
  }
});
d.addEventListener("click", function () {
  if (card_id.style.display === "block") {
    card_id.style.display = "none";
    document.getElementById("library_id").required = false;
    document.getElementById("library_id").value = "";
  }
});
window.onload = function () {
  document.querySelectorAll("input[type=radio]").forEach(function (radio) {
    radio.checked = false;
  });
  document.getElementById("staff_id").value = "";
  document.getElementById("library_id").value = "";
  document.getElementById("matric_no").value = "";
};
//password validation
const passwordInput = document.getElementById("id_password");

passwordInput.addEventListener("input", () => {
  const password = passwordInput.value;
  const passwordRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[a-zA-Z\d@#$%^&+=]{8,}$/;
  const isValidPassword = passwordRegex.test(password);

  if (isValidPassword) {
    passwordInput.classList.remove("is-invalid");
    passwordInput.classList.add("is-valid");
  } else {
    passwordInput.classList.remove("is-valid");
    passwordInput.classList.add("is-invalid");
  }
});
const passwoordInput = document.getElementById("id_password");
const confirmPasswordInput = document.getElementById("id_password2");
const errorText = document.getElementById("error-text");

confirmPasswordInput.addEventListener("input", () => {
  const password = passwoordInput.value;
  const confirmPassword = confirmPasswordInput.value;

  if (password !== confirmPassword) {
    errorText.innerText = "Passwords do not match";
    confirmPasswordInput.classList.add("is-invalid");
  } else {
    errorText.innerText = "";
    confirmPasswordInput.classList.remove("is-invalid");
    confirmPasswordInput.classList.add("is-valid");
  }
});

const uname = document.getElementById("id_username");
const unameError = document.getElementById("uname-error");
const fname = document.getElementById("id_first_name");
const fnameError = document.getElementById("fname-error");
const lname = document.getElementById("id_last_name");
const lnameError = document.getElementById("lname-error");
const regex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
const unameregex = /[!@#$%^&*()_+\=\[\]{};':"\\|,.<>\/?]/;
const regex1 = /[0-9]/;

uname.addEventListener("input", () => {
  if (unameregex.test(uname.value)) {
    unameError.style.display = "block";
  } else {
    unameError.style.display = "none";
  }
});
fname.addEventListener("input", () => {
  if (regex.test(fname.value)) {
    fnameError.style.display = "block";
  } else if (regex1.test(fname.value)) {
    fnameError.style.display = "block";
  } else {
    fnameError.style.display = "none";
  }
});
lname.addEventListener("input", () => {
  if (regex.test(lname.value)) {
    lnameError.style.display = "block";
  } else if (regex1.test(lname.value)) {
    lnameError.style.display = "block";
  } else {
    lnameError.style.display = "none";
  }
});

