# 🌱 FarmTech Solutions - Sistema de Irrigação Inteligente (Versão Sem Banco)

## 📌 Descrição
Projeto completo de agricultura digital utilizando ESP32, Python e dashboard web.

## ⚙️ Componentes
- ESP32 (Wokwi)
- DHT22 (umidade)
- LDR (pH)
- Botões (NPK)
- Relé (irrigação)

## 🧠 Lógica
Irrigação ativada quando:
- Umidade < 50%
- pH fora de 5.5 a 7.0
- NPK incompleto
- Sem previsão de chuva

## 🖥️ Dashboard
Aplicação Flask que simula dados em tempo real (sem uso de banco de dados).

## 🤖 Automação
Script que gera dados simulados no terminal.

## 🚀 Execução

### Dashboard
```bash
cd dashboard
python app.py
```

### Automação
```bash
python automation.py
```

## 📹 Vídeo
Adicionar link aqui

## 👨‍💻 Projeto acadêmico FIAP
