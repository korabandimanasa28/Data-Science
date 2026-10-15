import pandas as pd
import matplotlib.pyplot as plt
study_hours = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
marks = [42, 48, 53, 61, 64, 70, 75, 78, 84, 91]
df = pd.DataFrame({
    'Study_Hours': study_hours,
    'Marks': marks
})
print("Data:")
print(df)
plt.figure(figsize=(8, 5))
plt.scatter(df['Study_Hours'], df['Marks'])
plt.title("Relationship Between Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.show()
correlation = df['Study_Hours'].corr(df['Marks'])
print("\nCorrelation Coefficient:", round(correlation, 2))