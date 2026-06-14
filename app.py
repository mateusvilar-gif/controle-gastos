import requests
from flask import Flask, render_template, request, redirect
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

@app.route("/")
def home():
    valor = "indisponivel"
    try:
        r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL", timeout=10)
        dados = r.json()
        if "USDBRL" in dados:
            valor = dados["USDBRL"]["bid"]
    except Exception:
        valor = "indisponivel"

    gastos = supabase.table("gastos").select("*").execute().data
    return render_template("index.html", valor=valor, gastos=gastos)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    descricao = request.form.get("descricao")
    valor_gasto = request.form.get("valor")
    categoria = request.form.get("categoria")
    supabase.table("gastos").insert({
        "descricao": descricao,
        "valor": valor_gasto,
        "categoria": categoria
    }).execute()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)