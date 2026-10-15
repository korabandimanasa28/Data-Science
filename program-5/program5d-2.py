import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Department': [
        'CSE', 'CSE', 'CSE', 'CSE', 'CSE',
        'ECE', 'ECE', 'ECE', 'ECE', 'ECE',
        'EEE', 'EEE', 'EEE', 'EEE', 'EEE'
    ],
    'Marks': [
        82, 76, 91, 85, 89,
        68, 74, 79, 83, 71,
        62, 70, 75, 81, 86
    ]
}
df = pd.DataFrame(data)
print("Data:")
print(df)
plt.figure(figsize=(8, 5))
sns.boxplot(
    x='Department',
    y='Marks',
    data=df
)
plt.title("Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()