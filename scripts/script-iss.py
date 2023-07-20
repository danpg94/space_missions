import time
import urllib.request
import json

try:
    while True:
        req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
        response = urllib.request.urlopen(req)

        data = json.loads(response.read())

        # Extraer la información de la posición de la EEI
        timestamp = data['timestamp']
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']

        # Imprimir la información de la posición en tiempo real
        print(f"Timestamp: {timestamp}")
        print(f"Latitud: {latitude}")
        print(f"Longitud: {longitude}\n")

        time.sleep(1)

except Exception as e:
    print("Error al recuperar los datos:", e)
