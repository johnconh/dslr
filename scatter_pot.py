import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

try:
    filesys = sys.argv[1]
except IndexError:
    print('No file provided')
    sys.exit(1)

try:
    df = pd.read_csv(filesys)
except FileNotFoundError:
    print('File not found')
    sys.exit(1)

df = df.select_dtypes(include=[np.number]) #Seleccionar columnas numericas

#Crear una matriz de correlacion
correlation_matrix = df.corr()

#Encontrar el par de caracteristicas co la correlacion mas alta(absoluta)
corr_pairs = correlation_matrix.unstack()
corr_pairs = corr_pairs[corr_pairs < 0.95] #Excluir la correlacion perfecta
most_similar = corr_pairs.idxmax()#Par de correlacion mas alta

feature1, feature2 = most_similar

plt.figure(figsize=(10, 6))
plt.scatter(df[feature1], df[feature2], alpha=0.6)
plt.title(f'Scatter Plot of {feature1} vs {feature2}')
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.grid(True)

output_dir = 'scatter_plots'
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, 'most_similar_features_scatter.png')
plt.savefig(output_path)
plt.close()