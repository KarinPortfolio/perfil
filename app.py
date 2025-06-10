from flask import Flask, render_template, request
from collections import Counter
from logic.graficos import gerar_grafico_perfis

app = Flask(__name__)

resultados_quiz_historico = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    respostas = {q: request.form[q] for q in request.form}

    contadores = Counter()
    for resposta in respostas.values():
        if resposta == 'A':
            contadores['Afetivo'] += 1
        elif resposta == 'B':
            contadores['Independente'] += 1
        elif resposta == 'C':
            contadores['Controlador'] += 1
        elif resposta == 'D':
            contadores['Desatento'] += 1

    if contadores:
        perfil_dominante = contadores.most_common(1)[0][0]
    else:
        perfil_dominante = "Não foi possível determinar"

    resultados_quiz_historico.append(perfil_dominante)

    # --- NOVO TRECHO: Gerar o gráfico e passar para o template ---
    contagem_perfis = Counter(resultados_quiz_historico)
    imagem_grafico_base64 = gerar_grafico_perfis(dict(contagem_perfis))

    return render_template('resultado.html',
                           perfil=perfil_dominante,
                           grafico_base64=imagem_grafico_base64) # Passe a string Base64 aqui
if __name__ == '__main__':
    app.run(debug=True)