function validateForm() {
  // Get the value of the input field using their ID
  let f = document.getElementById("fname").value;
  // If f is empty
  let text1;
  if (f == "") {
    text1 = "First Name cannot be empty";
  } else {
    text1 = "";
  }

  let l = document.getElementById("lname").value;
  let text2;
  if (l == "") {
    text2 = "Last Name cannot be empty";
  } else {
    text2 = "";
  }

  let e = document.getElementById("email").value;
  let text3;
  if (e == "") {
    text3 = "Looks like this is not an email";
  } else {
    text3 = "";
  }

  let p = document.getElementById("pword").value;
  let text4;
  let text5;
  if (p == "") {
    text4 = "Password cannot be empty";
    text5 = "email@example/com";
  } else {
    text4 = "";
    text5 = "";
  }

  document.getElementById("v-fname").innerHTML = text1;
  document.getElementById("v-lname").innerHTML = text2;
  document.getElementById("v-email").innerHTML = text3;
  document.getElementById("v-pword").innerHTML = text4;
  document.getElementsByName("email")[0].placeholder = text5;
}
