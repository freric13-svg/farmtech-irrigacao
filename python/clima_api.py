import requests
import serial
import time

# Configurações
API_KEY = "SUA_API_KEY_AQUI"
CIDADE = "Sao Paulo"
PORTA_SERIAL = "COM3" # Ajuste conforme seu PC (ex: /dev/ttyUSB0 no Linux)

try:
    ser = serial.Serial(PORTA_SERIAL, 115200)
    time.sleep(2) # Aguarda conexão estabilizar

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&lang=pt_br"
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
