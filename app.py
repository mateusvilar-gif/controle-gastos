import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    valor = "indisponivel"
    try:
        r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL", timeout=5)
        dados = r.json()
        if "USDBRL" in dados:
            valor = dados["USDBRL"]["bid"]
        elif isinstance(dados, list) and len(dados) > 0:
            valor = dados[0].get("bid", "indisponivel")
    except Exception:
        valor = "indisponivel"
    return "<h1>Controle de Gastos</h1><p>Dolar: R$ " + str(valor) + "</p>"

if __name__ == "__main__":
    app.run()