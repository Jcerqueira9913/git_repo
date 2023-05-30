import numpy as np
import json

matriz = np.array([[2, 0, 0],
                   [0, 2, 0],
                   [0, 0, 2]])

vetores = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])

vetores_transformados = np.dot(matriz, vetores.T).T

dados = {
  'matriz': matriz.tolist(),
  'vetores': vetores.tolist(),
  'vetores_transformados': vetores_transformados.tolist()
}

# Salvar os dados em um arquivo JSON
with open('transformacão_linear.json', 'w') as arquivo:
    json.dump(dados, arquivo)
