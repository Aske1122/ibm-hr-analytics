import pandas as pd

# Indlæs data
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv", sep=';')

# Hvor stort er datasættet?
print("=== DATASÆT STØRRELSE ===")
print(f"Rækker: {df.shape[0]}, Kolonner: {df.shape[1]}")

# Se de første rækker
print("\n=== DE FØRSTE 5 RÆKKER ===")
print(df.head())

# Hvilke kolonner har vi?
print("\n=== KOLONNER OG DATATYPER ===")
print(df.dtypes)

# Er der manglende værdier?
print("\n=== MANGLENDE VÆRDIER ===")
print(df.isnull().sum())

# Hvad er attrition-fordelingen?
print("\n=== ATTRITION FORDELING ===")
print(df["Attrition"].value_counts())
print(df["Attrition"].value_counts(normalize=True).round(2))