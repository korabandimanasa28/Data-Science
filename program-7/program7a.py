import pandas as pd

df = pd.DataFrame({
    'Category': ['Fruit', 'Fruit', 'Vegetable', 'Vegetable'],
    'Data': [15, 25, 30, 45]
})

grouped = df.groupby('Category')

print("Total Data by Category:")
print(grouped['Data'].sum())