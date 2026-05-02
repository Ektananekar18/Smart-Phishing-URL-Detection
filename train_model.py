import pandas as pd

print("Training Started")

# dataset load
data = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully")
print(data.head())