from flask import Flask, request, jsonify

app = Flask(__name__)

# Licenças válidas simuladas
licencas_validas = {
    "ABC123DEF": True,  # Substitua por chaves reais
    "XYZ789LMN": True
}

@app.route("/validar_licenca", methods=["POST"])
def validar_licenca():
    dados = request.get_json()
    licenca = dados.get("licenca")

    if not licenca:
        return jsonify({"erro": "Licença não informada."}), 400

    licenciado = licencas_validas.get(licenca, False)
    
    return jsonify({"licenciado": licenciado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
