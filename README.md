# 🌱 FarmTech Solutions - Projeto de Irrigação Inteligente

## 📌 Objetivo
Simular um sistema de irrigação inteligente utilizando ESP32 e sensores simulados no Wokwi.

## 🔧 Sensores utilizados

- Botões → Simulam NPK
- LDR → Simula pH do solo
- DHT22 → Simula umidade do solo
- Relé → Simula bomba de irrigação

## 🧠 Lógica do Sistema

A irrigação é ativada quando:
- Umidade abaixo de 50%
- pH fora da faixa ideal (5.5 a 7.0)
- NPK incompleto

## 📁 Estrutura

- src/esp32_irrigacao.ino
- python/clima_api.py
- README.md

## 🚀 Como executar

1. Rodar código no Wokwi
2. Testar sensores
3. Executar script Python para clima

## 📹 Vídeo
Inserir link aqui

## 👨‍💻 Autor
Projeto acadêmico FIAP - FarmTech Solutions
