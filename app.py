import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    valor = dados["USDBRL"]["bid"]
    return f"<h1>Controle de Gastos</h1><p>Cotacao do dolar hoje: R$ {valor}</p>"

if __name__ == '__main__':
    app.run()
