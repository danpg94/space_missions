import { BASE_URL } from "./setup.js";
//Obtenemos las referencias del html de nuestros componentes/etiquetas
const statusSpan = document.querySelector("#message");
const timestampSpan = document.querySelector("#timestamp");
const latitudeSpan = document.querySelector("#latitude");
const longitudeSpan = document.querySelector("#longitude");

//Funcion que permite hacer una petición GET a la url de la iss
const fetchCurrentPosition = async () => {
  try {
    //Primero establecemos el estado de la interfaz al default
    setDefaultStatus();
    //Hacemos la peticion GET
    let response = await fetch(`${BASE_URL}/iss-now.json`);
    /**
     * Mediante destructuracion obtenemos la propiedad iss_position de la respuesta de la petición
     * Y las demás propiedades las guardamos en la variable "resto"
     */
    let { iss_position, ...resto } = await response.json();
    //Ejecutamos la función setUpdateStatus para actualizar el estado de la interfaz
    setUpdatedStatus({ ...iss_position, ...resto });
    //Ejecutamos init, que permite inicializar el ciclo de peticiones
    init();
  } catch (error) {
    console.log(error);
    //aqui se podría agregar un mensaje de error
    //ej: alert("Algo ha salido mal obteniendo la información de la api")
  }
};

/**
 * Esta funcion permite establecer el estado de "carga"/"default" mientras la petición se realiza
 */
function setDefaultStatus() {
  statusSpan.innerText = "Pending...";
  timestampSpan.innerText = "waiting...";
  latitudeSpan.innerText = "waiting...";
  longitudeSpan.innerText = "waiting...";
}

/**
 *
 * Esta funcion permite actualizar el estado de la interfaz
 */
function setUpdatedStatus({ message, timestamp, latitude, longitude }) {
  console.log(message);
  //innerText es la propiedad que permite modificar el texto de un elemento html mediante js
  statusSpan.innerText = message;
  timestampSpan.innerText = timestamp;
  latitudeSpan.innerText = latitude;
  longitudeSpan.innerText = longitude;
}

//Función que hace una petición cada 5 segundos a la api de la iss
function init() {
  setTimeout(() => fetchCurrentPosition(), 5000);
}

//Ejecutamos el script
fetchCurrentPosition();
