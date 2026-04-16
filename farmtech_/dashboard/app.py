
from flask import Flask, render_template_string
import random

app = Flask(__name__)

def gerar_dados():
    dados = []
    for _ in range(5):
        cultura = random.choice(["Shitake", "Hortifruti"])
        umidade = random.randint(30, 90)
        ph = round(random.uniform(5.0, 7.5), 2)
        irrigacao = "ON" if umidade < 50 else "OFF"
        dados.append((cultura, umidade, ph, irrigacao))
    return dados

HTML = '''
<h1>🌱 FarmTech Dashboard (Sem Banco)</h1>
<table border="1">
<tr><th>Cultura</th><th>Umidade</th><th>pH</th><th>Irrigação</th></tr>
{% for row in dados %}
<tr>
<td>{{row[0]}}</td>
<td>{{row[1]}}</td>
<td>{{row[2]}}</td>
<td>{{row[3]}}</td>
</tr>
{% endfor %}
</table>
'''

@app.route("/")
def home():
    dados = gerar_dados()
    return render_template_string(HTML, dados=dados)

app.run(debug=True)
