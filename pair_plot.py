import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
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

sns.pairplot(df)
plt.suptitle('Pair Plot of Numerical Features', y=1.02)

output_dir='pair_plot'
os.makedirs(output_dir, exist_ok=True)

output_path= os.path.join(output_dir, 'pair_plot.png')
plt.savefig(output_path)
plt.close()