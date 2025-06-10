import pandas as pd
import os

def analisar_respostas(respostas):
    pontuacoes = {
        'A': 'Afetivo',
        'B': 'Independente',
        'C': 'Controlador',
        'D': 'Desatento'
    }

    perfis = [pontuacoes.get(r, 'Desconhecido') for r in respostas]
    perfil_dominante = pd.Series(perfis).mode()[0]

    # Gravar resultado
    df = pd.DataFrame({'respostas': [respostas], 'perfil': [perfil_dominante]})
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/resultados.csv', mode='a', header=not os.path.exists('data/resultados.csv'), index=False)

    return perfil_dominante
