import pandas as pd

df = pd.DataFrame({
    'Department': ['CSE', 'CSE', 'ECE', 'ECE'],
    'Marks': [80, 90, 70, 85]
})

grouped = df.groupby('Department')

print("Mean and Standard Deviation:")
print(grouped['Marks'].agg(['mean', 'std']))