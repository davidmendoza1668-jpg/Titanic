import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_excel("drive/MyDrive/titanic-analisis/data/Titanic-Dataset.xlsx")

print(df.head(5))
print("-----------------------------------")
print(df.info())
print("-----------------------------------")
print(df.isnull().sum())
print("-----------------------------------")
print(df.shape)

df["Age"] = df["Age"].fillna(df["Age"].mean())

df = df.drop("Cabin", axis=1)

df["Survived"].value_counts()