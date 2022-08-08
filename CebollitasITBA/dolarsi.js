async function getDolarData() {
  const response = await fetch(
    "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
  );
  const date = new Date();
  const data = await response.json();
  const dolarOficial = data[0]["casa"];
  const dolarBlue = data[1]["casa"];
  const dolarCont = data[3]["casa"];
  const dolarBolsa = data[4]["casa"];
  const dolarTurista = data[6]["casa"];
  const dolarPromedio = data[7]["casa"];

  // DOLAR OFICIAL

  const doc = document.getElementById("doc");
  const dov = document.getElementById("dov");
  const vardo = document.getElementById("vardo");
  const actdo = document.getElementById("actdo");

  doc.innerHTML += dolarOficial["compra"];
  dov.innerHTML += dolarOficial["venta"];
  vardo.innerHTML += dolarOficial["variacion"] + "%";
  actdo.innerHTML +=
    date.getDate() +
    "/" +
    date.getMonth() +
    "/" +
    date.getFullYear() +
    "  " +
    date.getHours() +
    ":" +
    date.getMinutes() +
    "HS";

  // DOLAR BLUE

  const dbc = document.getElementById("dbc");
  const dbv = document.getElementById("dbv");
  const vardb = document.getElementById("vardb");
  const actdb = document.getElementById("actdb");

  dbc.innerHTML += dolarBlue["compra"];
  dbv.innerHTML += dolarBlue["venta"];
  vardb.innerHTML += dolarBlue["variacion"] + "%";
  actdb.innerHTML +=
    date.getDate() +
    "/" +
    date.getMonth() +
    "/" +
    date.getFullYear() +
    "  " +
    date.getHours() +
    ":" +
    date.getMinutes() +
    "HS";

  // DOLAR LIQUI

  const refdl = document.getElementById("refdl");
  const vardl = document.getElementById("vardl");
  const actdl = document.getElementById("actdl");

  refdl.innerHTML += dolarCont["venta"];
  vardl.innerHTML += dolarCont["variacion"] + "%";
  actdl.innerHTML +=
    date.getDate() +
    "/" +
    date.getMonth() +
    "/" +
    date.getFullYear() +
    "  " +
    date.getHours() +
    ":" +
    date.getMinutes() +
    "HS";

  // DOLAR BOLSA

  const refdbol = document.getElementById("refdbol");
  const vardbol = document.getElementById("vardbol");
  const actdbol = document.getElementById("actdbol");

  refdbol.innerHTML += dolarBolsa["compra"];
  vardbol.innerHTML += dolarBolsa["variacion"];
  actdbol.innerHTML +=
    date.getDate() +
    "/" +
    date.getMonth() +
    "/" +
    date.getFullYear() +
    "  " +
    date.getHours() +
    ":" +
    date.getMinutes() +
    "HS";

  // DOLAR TURISTA

  const dtv = document.getElementById("dtv");
  const vardt = document.getElementById("vardt");
  const actdt = document.getElementById("actdt");

  dtv.innerHTML += dolarTurista["venta"];
  vardt.innerHTML += dolarTurista["variacion"];
  actdt.innerHTML +=
    date.getDate() +
    "/" +
    date.getMonth() +
    "/" +
    date.getFullYear() +
    "  " +
    date.getHours() +
    ":" +
    date.getMinutes() +
    "HS";

  // DOLAR  PROMEDIO

  const dpc = document.getElementById("dpc");
  const dpv = document.getElementById("dpv");
  const vardp = document.getElementById("vardp");
  const actdp = document.getElementById("actdp");

  dpc.innerHTML += dolarPromedio["compra"];
  dpv.innerHTML += dolarPromedio["venta"];
  vardp.innerHTML += dolarOficial["variacion"];
  actdp.innerHTML +=
    date.getDate() +
    "/" +
    date.getMonth() +
    "/" +
    date.getFullYear() +
    "  " +
    date.getHours() +
    ":" +
    date.getMinutes() +
    "HS";
}

getDolarData();
