  from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():...

@app.route("/<int:numero1>/<int:numero2>/<string:sinal>")
def calculadora(numero1, numero2, sinal):...
    return f"Calculadora: {numero1} {sinal} {numero2}"
