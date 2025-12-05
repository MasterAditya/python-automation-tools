import pandas as pd

excel_file = "input.xlsx"
df = pd.read_excel(excel_file)

# Example cleaning: drop empty columns, fill NaNs
df.dropna(axis=1, how="all", inplace=True)
df.fillna("", inplace=True)

df.to_excel("cleaned.xlsx", index=False)
print("Excel cleaned and saved as cleaned.xlsx")
