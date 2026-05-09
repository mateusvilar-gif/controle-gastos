import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL", timeout=5)
        valor = r.json()["USDBRL"]["bid"]
    except:
        valor = "indisponivel"
    return "<h1>Controle de Gastos</h1><p>Dolar: R$ " + str(valor) + "</p>"

if __name__ == "__main__":
    app.run()