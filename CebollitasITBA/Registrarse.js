function Mostrar_Contraseña() {
  let password, check;

  password = document.getElementById("Contraseña");

  check = document.getElementById("ver");

  if (check.checked == true) {
    // Si la checkbox de mostrar contraseña está activada
    password.type = "text";
  } // Si no está activada
  else {
    password.type = "password";
  }
}
