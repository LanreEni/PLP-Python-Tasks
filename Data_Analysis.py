
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # Load the Iris dataset directly from seaborn
    df = sns.load_dataset('iris')
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: File not found. Please check the dataset path.")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display the first few rows
print("🔹 First five rows of the dataset:")
print(df.head())

# Display info about data types and structure
print("\n🔹 Dataset Information:")
print(df.info())

# Check for missing values
print("\n🔹 Missing Values per Column:")
print(df.isnull().sum())

# Clean the dataset (if any missing values exist)
df = df.fillna(df.mean(numeric_only=True))
print("\n✅ Missing values handled successfully (if any).")

# ======================================================
# TASK 2: BASIC DATA ANALYSIS
# ======================================================

# Compute basic statistics
print("\n🔹 Basic Statistics:")
print(df.describe())

# Perform grouping: mean petal length per species
grouped = df.groupby('species')['petal_length'].mean()
print("\n🔹 Average Petal Length per Species:")
print(grouped)

# Observations / Patterns
print("""
🔹 Observations:
- Setosa species have the smallest petal length.
- Versicolor species have moderate petal length.
- Virginica species have the largest petal length.
""")

# ======================================================
# TASK 3: DATA VISUALIZATION
# ======================================================

sns.set_style("whitegrid")  # For better aesthetics

# --- 1️⃣ Line Chart ---
# Since the dataset has no time column, we use index to simulate one
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['sepal_length'], label='Sepal Length', color='green')
plt.title('Line Chart: Sepal Length Trend Over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# --- 2️⃣ Bar Chart ---
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal_length', data=df, palette='viridis')
plt.title('Bar Chart: Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# --- 3️⃣ Histogram ---
plt.figure(figsize=(8, 5))
plt.hist(df['sepal_width'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram: Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# --- 4️⃣ Scatter Plot ---
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, palette='Set2')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

print("\n✅ All tasks completed successfully!")
