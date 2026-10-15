import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = [35, 42, 48, 51, 55, 57, 60, 63, 67, 69,
        71, 74, 77, 79, 83, 86, 89, 91, 94, 98]
df = pd.DataFrame({'Marks': data})
print("Observed Data:")
print(df)
plt.figure(figsize=(8, 5))
sns.histplot(df['Marks'], bins=6, kde=False)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
sns.kdeplot(df['Marks'], fill=True)
plt.title("Density Plot of Marks")
plt.xlabel("Marks")
plt.ylabel("Density")
plt.tight_layout()
plt.show()
sns.histplot(df['Marks'], bins=6, kde=True)
plt.title("Histogram with Density Curve")
plt.xlabel("Marks")
plt.ylabel("Frequency / Density")
plt.show()