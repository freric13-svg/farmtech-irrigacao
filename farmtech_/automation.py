
import random

for i in range(5):
    cultura = random.choice(["Shitake", "Hortifruti"])
    umidade = random.randint(30, 90)
    ph = round(random.uniform(5.0, 7.5), 2)
    irrigacao = "ON" if umidade < 50 else "OFF"

    print(f"Cultura: {cultura}")
    print(f"Umidade: {umidade}")
    print(f"pH: {ph}")
    print(f"Irrigação: {irrigacao}")
    print("-" * 30)
