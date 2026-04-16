import requests
import serial
import time

# Configurações
API_KEY = "b296a63c88636674760e7c1b5aa57ea3"
CIDADE = "Sao Paulo"
PORTA_SERIAL = "COM3" # Ajuste conforme seu PC (ex: /dev/ttyUSB0 no Linux)

try:
    ser = serial.Serial(PORTA_SERIAL, 115200)
    time.sleep(2) # Aguarda conexão estabilizar

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&appid=b296a63c88636674760e7c1b5aa57ea3&units=metric"
    resposta = requests.get(url).json()

    if "weather" in resposta:
        clima = resposta["weather"][0]["main"].lower()
        print(f"Clima atual em {CIDADE}: {clima}")

        if "rain" in clima or "drizzle" in clima:
            ser.write(b'1') # Avisa ESP32 que vai chover
            print("Sinal enviado: Chuva detectada. Irrigação suspensa.")
        else:
            ser.write(b'0') # Sem chuva
            print("Sinal enviado: Sem chuva. ESP32 assume controle.")
    
    ser.close()
except Exception as e:
    print(f"Erro: {e}")
