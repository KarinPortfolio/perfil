# Em logic/graficos.py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tempfile
from collections import Counter
import base64 # <-- Adicione esta importação
import os     # <-- Adicione esta importação para remover o arquivo temporário

_resultados_historico = []

def adicionar_resultado_ao_historico(perfil):
    """Adiciona um perfil ao histórico para gerar o gráfico."""
    _resultados_historico.append(perfil)

def gerar_grafico_perfis(contagem_perfis):
    """
    Gera um gráfico de barras da distribuição dos perfis,
    salva-o em um arquivo temporário, o codifica para Base64,
    e retorna a string Base64.
    """
    if not contagem_perfis:
        return None

    perfis = list(contagem_perfis.keys())
    contagens = list(contagem_perfis.values())

    plt.figure(figsize=(8, 6)) # Opcional: define um tamanho de figura
    plt.bar(perfis, contagens, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
    plt.xlabel('Perfil')
    plt.ylabel('Número de Pessoas')
    plt.title('Distribuição dos Perfis de Relacionamento')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Cria um arquivo temporário e salva o gráfico
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    caminho_imagem = temp_file.name
    plt.savefig(caminho_imagem, format='png')
    temp_file.close() # Fecha o manipulador do arquivo

    # Abre o arquivo temporário em modo binário, lê o conteúdo
    # e o codifica para Base64
    with open(caminho_imagem, "rb") as image_file:
        imagem_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    # Limpa o arquivo temporário após o uso
    os.remove(caminho_imagem)

    plt.close() # Fecha a figura Matplotlib para liberar memória

    return imagem_base64 # <-- Retorna a string Base64