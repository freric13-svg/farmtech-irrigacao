# 🌱 FarmTech Solutions - Fase 2: Irrigação Inteligente

## 📌 Sobre o Projeto
Esta é a continuação do sistema de gestão agrícola voltado para o cultivo de **Shitake** e **Horticultura**. Nesta fase, implementamos um protótipo de **Irrigação Inteligente** utilizando o microcontrolador ESP32.

## 🎯 Regras de Negócio
O sistema ativa a irrigação automaticamente quando:
1.  **Umidade do solo** for inferior a 60%.
2.  **pH do solo** estiver fora da faixa ideal (5.5 a 7.0), simulado pelo LDR.
3.  **Nutrientes NPK** estiverem insuficientes (simulados por botões).
4.  **Previsão do Tempo:** A irrigação é bloqueada se a API do OpenWeather detectar chuva.

## 🛠️ Componentes e Conexões (Wokwi)
- **DHT22:** Medidor de umidade e temperatura.
- **LDR:** Simulador de sensor de pH.
- **Botões (3x):** Representam os níveis de Nitrogênio (N), Fósforo (P) e Potássio (K).
- **Relé:** Atuador que ligaria a bomba de água.

## 📁 Organização do Repositório
- `/src`: Código fonte `.ino` para o ESP32.
- `/python`: Script de integração com API climática.
- `/r`: Análise estatística dos dados de solo.
- `/docs`: Diagramas e imagens do circuito.

## 🚀 Como Executar
1. Carregue o código do `src` no simulador Wokwi.
2. Execute o script Python para enviar os dados climáticos reais via Serial.
3. Utilize o script R para analisar as médias de umidade da plantação.

## 📸 Circuito do Projeto (Wokwi)
Abaixo está a representação visual da montagem do hardware simulado:

![Circuito FarmTech](./docs/circuito_farmtech.png)

## 🛠️ Instruções de Execução
1. Carregue o código da pasta `/src` no Wokwi.
2. Certifique-se de que os pinos seguem o arquivo `diagram.json`.
3. Para integração com a API, utilize o script em `/python`.
