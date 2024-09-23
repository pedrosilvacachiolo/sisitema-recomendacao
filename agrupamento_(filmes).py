# -*- coding: utf-8 -*-
"""agrupamento (filmes)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HbN1N8_OZuOxFXa1c_4FblKmuxRXj6j6
"""

# importando as biblioyecas necessarias
import numpy as np
from sklearn.cluster import KMeans
# matriz simples
# 6 usuarios e 4 filmes
movie_ratings = np.array([
    [1,0,0,1],  # usuario 1: assitiu aos filmes 1 e 4
    [1,1,0,0],  # usuario 2: assitiu aos filmes 1 e 2
    [0,1,1,0],  # usuario 3: assitiu aos filmes 2 e 3
    [0,0,1,1],  # usuario 4: assitiu aos filmes 3 e 4
    [1,0,1,0],  # usuario 5: assitiu aos filmes 1 e 3
    [0,1,0,1],  # usuario 6: assitiu aos filmes 2 e 4

])

# treinando o modelo
num_clusters = 2

# inicializando o modelo
Kmeans = KMeans(n_clusters=num_clusters,
                random_state=0,n_init=10)

# treinando o modelo
Kmeans.fit(movie_ratings)

#classificando os usuarisos
grupos_indice = Kmeans.predict(movie_ratings)

# exibir dados
print("usuario pertence ao seguinte grupo:")
for i, cluster in enumerate(grupos_indice):
  print(f"usuario {i+1} pertence ao grupo {cluster+1}")

print("\nFilmes assistidos:")
for i in range(len(movie_ratings)):
  assistidos = np.where(movie_ratings[i] == 1)[0] +1
  print(f"Usuario {i+1} assistiu aos filmes:{assistidos}")

# funçao que recomenda filmes
def recomendar_filmes (filmes, filmes_assistidos, grupos_indice):

  filmes = np.array(filmes)

  # encontrar o grupo do usuario com base em seu vetor de filmes
  usuario_id = len(filmes_assistidos)
  grupo_usuarios = Kmeans.predict([filmes])[0]


  usuarios_no_mesmo_grupo = [i for i in range(len(grupos_indice))
  if grupos_indice[i] == grupo_usuarios]


  filmes_recomendados = set()
  for usuario in usuarios_no_mesmo_grupo:
    filmes_assistidos_usuario = np.where(filmes_assistidos[usuario] == 1)[0]
    filmes_recomendados.update(filmes_assistidos_usuario)

  #remover filmes que o usuario ja assistiu
  filmes_recomendados = filmes_recomendados - set(np.where(filmes == 1)[0])

  #ajustar os indice dos filmes recomendados
  filmes_recomendados = [filme + 1 for filme in filmes_recomendados]

  return sorted(filmes_recomendados)

# exemplo de uso da funcao recomendar_filmes
filmes_assistidos_usuario = [1,0,1,0] #vetor de filmes
#asistidos (por exmplo ,assitiu aos filmes 1 e 3)
filmes_recomendados = recomendar_filmes(filmes_assistidos_usuario, movie_ratings ,grupos_indice)

print(f"\nFilmes recomendados:{filmes_recomendados}")