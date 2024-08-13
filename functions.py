import pandas as pd
import numpy as np

def count(df):
    count = 0
    for _ in df:
        count += 1
    return count

def mean(df):
    df = pd.to_numeric(df, errors='coerce')
    total_sum = 0
    for i in df:
        total_sum += i
    return total_sum / count(df)

def std(df):
    df = pd.to_numeric(df, errors='coerce')
    mean_value = mean(df)
    sum_squared = 0
    for i in df:
        if not pd.isnull(i): 
            sum_squared += (i - mean_value) ** 2
    return np.sqrt(sum_squared / count(df))

def min(df):
    df = pd.to_numeric(df, errors='coerce')
    min_value = df[0]
    for i in df:
        if i < min_value:
            min_value = i
    return min_value

def max(df):
    df = pd.to_numeric(df, errors='coerce')
    max_value = df.iloc[0]
    for i in df:
        if i > max_value:
            max_value = i
    return max_value

def percentile(df, p):
    df = pd.to_numeric(df, errors='coerce')
    df = sorted(df)
    index = (p / 100) * (count(df) - 1)
    if index.is_integer():
        return df[int(index)]
    else:
        lower = df[int(index)]
        upper = df[int(index) + 1]
        return lower + (upper - lower) * (int(index) % 1)
    
def sum(df):
    if np.isscalar(df):
        return df
    df = pd.to_numeric(df, errors='coerce')
    total_sum = 0
    for i in df:
        total_sum += i
    return total_sum
