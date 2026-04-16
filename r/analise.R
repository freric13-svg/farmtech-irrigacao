# FarmTech Solutions - Análise de Decisão
# Simulando dados coletados de sensores de Horticultura e Shitake

dados_umidade <- c(58, 62, 45, 50, 48, 55, 60) # Amostras de umidade (%)

media_umidade <- mean(dados_umidade)
desvio_padrao <- sd(dados_umidade)

cat("--- RELATÓRIO DE ANÁLISE FARMTECH ---\n")
cat("Média de Umidade observada:", round(media_umidade, 2), "%\n")
cat("Variabilidade (Desvio Padrão):", round(desvio_padrao, 2), "%\n")

# Recomendação estratégica
if (media_umidade < 55) {
  cat("ALERTA: Solo abaixo da média ideal para Horticultura. Aumentar frequência de irrigação.\n")
} else {
  cat("STATUS: Níveis de umidade estáveis para o cultivo.\n")
}
