var designationRadios = document.querySelectorAll('input[name="designation"]');

for (var i = 0; i < designationRadios.length; i++) {
  designationRadios[i].addEventListener("click", function () {
    if (this.value === "Admin") {
      document.querySelector(".staff").style.display = "none";
      document.querySelector(".student").style.display = "none";
      document.querySelector(".lib_user").style.display = "none";
      document.querySelector(".card_id").style.display = "none";
      document.querySelector("#staff_id").required = false;
      document.querySelector("#matric_no").required = false;
      document.querySelector("#library_user_1").required = false;
      document.querySelector("#library_user_2").required = false;
      document.querySelector("#library_id").required = false;
      document.getElementById("library_user_1").checked = false;
      document.getElementById("library_user_2").checked = false;
    } 
  });
}
