
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from rapidfuzz import process, fuzz

app = Flask(__name__)
CORS(app)

# Carregar CSV e garantir que os nomes das colunas estão corretos
df = pd.read_csv("C:\\Users\\Usuario\\Desktop\\Importante\\projetos\\Desafio Intuitive Care\\data\\Relatorio_cadop.csv", delimiter=";", encoding="utf-8")  # Definindo delimitador correto caso seja ";"
df.columns = df.columns.str.strip()  # Removendo espaços extras

@app.route("/buscar", methods=["GET"])
def buscar_operadora():
    termo = request.args.get("q", "").strip()
    
    if not termo:
        return jsonify({"error": "Termo de busca não informado"}), 400

    # Buscar na coluna correta
    resultados = process.extract(termo, df["Razao_Social"], scorer=fuzz.WRatio, limit=5)
    
    operadoras_encontradas = []
    seen = set()

    for nome, score, index in resultados:
        if score > 50 and nome not in seen:
            seen.add(nome)
            
            print(f"Index encontrado: {index}")
            print(f"Razao_Social encontrada: {df.iloc[index]['Razao_Social']}")
            print(f"CNPJ encontrado: {df.iloc[index]['CNPJ']}")
            
            operadoras_encontradas.append({
                "Razao_Social": str(df.iloc[index]["Razao_Social"]),
                "Nome_Fantasia": str(df.iloc[index]["Nome_Fantasia"]),
                "Modalidade": str(df.iloc[index]["Modalidade"]),
                "Logradouro": str(df.iloc[index]["Logradouro"]),
                "Numero": str(df.iloc[index]["Numero"]),
                "Bairro": str(df.iloc[index]["Bairro"]),
                "Cidade": str(df.iloc[index]["Cidade"]),
                "DDD": str(df.iloc[index]["DDD"]),
                "Telefone": str(df.iloc[index]["Telefone"]),
                "Endereco_eletronico": str(df.iloc[index]["Endereco_eletronico"]),
            })

    return jsonify(operadoras_encontradas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
