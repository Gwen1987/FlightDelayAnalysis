import pandas as pd


df = pd.read_csv('full_dataframe.csv', low_memory=False)


print(df['Origin'].value_counts(), df['Dest'].value_counts())