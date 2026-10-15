import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print("First Five Records:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal_width"], label="Sepal Width")
plt.plot(df.index, df["petal_width"], label="Petal Width")
plt.xlabel("Flower Index")
plt.ylabel("Width")
plt.title("Sepal Width and Petal Width")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="sepal_width",
    y="petal_width",
    hue="species"
)
plt.title("Sepal Width vs Petal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.show()
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="sepal_width",
    hue="species",
    kde=True
)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="species",
    y="sepal_width"
)
plt.title("Sepal Width by Species")
plt.xlabel("Flower Species")
plt.ylabel("Sepal Width")
plt.show()
sns.pairplot(
    df,
    hue="species"
)
plt.show()