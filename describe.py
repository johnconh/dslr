import pandas as pd
import numpy as np
import sys
from functions import count, mean, std, min, max, percentile, sum

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
    
for column in df.columns:
    '''
        Eliminar las columnas que no sean numéricas
    '''
    try:
        df[column] = pd.to_numeric(df[column])
    except ValueError:
        df = df.drop(column, axis=1)

for column in df.columns:
    '''
        Reemplazar los valores nulos por la media de la columna
    '''
    mean_value = sum(x for x in df[column] if x == x) / count(df[column])
    df[column] = df[column].apply(lambda x: mean_value if pd.isnull(x) else x)

stats = pd.DataFrame()

for column in df.columns:
    series = df[column].tolist()
    stats[column] = [
        count(series), 
        mean(series), 
        std(series), 
        min(series), 
        percentile(series, 25), 
        percentile(series, 50), 
        percentile(series, 75),
        max(series)
    ]

stats.index = ['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']

print(stats)
