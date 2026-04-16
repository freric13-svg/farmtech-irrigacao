#include "DHT.h"

#define DHTPIN 15
#define DHTTYPE DHT22
#define LDR_PIN 34
#define BTN_N 12
#define BTN_P 13
#define BTN_K 14
#define RELE 26

DHT dht(DHTPIN, DHTTYPE);
bool previsaoChuva = false;

void setup() {
  Serial.begin(115200);
  pinMode(BTN_N, INPUT_PULLUP);
  pinMode(BTN_P, INPUT_PULLUP);
  pinMode(BTN_K, INPUT_PULLUP);
  pinMode(RELE, OUTPUT);
  dht.begin();
}

void loop() {
  // Leitura da API via Python (Serial)
  if (Serial.available()) {
    char dado = Serial.read();
    if (dado == '1') previsaoChuva = true;
    if (dado == '0') previsaoChuva = false;
  }

  float umidade = dht.readHumidity();
  int ldrValor = analogRead(LDR_PIN);
  
  // Mapeamento didático: LDR (0-4095) para pH (0.0-14.0)
  float phSolo = map(ldrValor, 0, 4095, 0, 140) / 10.0;

  // Leitura NPK (Botão pressionado = Nível OK)
  bool nOk = !digitalRead(BTN_N);
  bool pOk = !digitalRead(BTN_P);
  bool kOk = !digitalRead(BTN_K);

  bool irrigar = false;

  // Lógica de Decisão FarmTech
  // Shitake e Hortaliças precisam de solo úmido e pH controlado (5.5 a 7.0)
  if (!previsaoChuva) {
    if (umidade < 60.0 || phSolo < 5.5 || phSolo > 7.0 || !nOk || !pOk || !kOk) {
      irrigar = true;
    }
  }

  digitalWrite(RELE, irrigar ? HIGH : LOW);

  // Monitoramento Serial
  Serial.print("Umidade: "); Serial.print(umidade);
  Serial.print("% | pH: "); Serial.print(phSolo);
  Serial.print(" | NPK: "); Serial.print(nOk && pOk && kOk ? "OK" : "FALTA");
  Serial.println(irrigar ? " | STATUS: IRRIGANDO" : " | STATUS: AGUARDANDO");

  delay(2000);
}
