import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
csv_file = "Final.csv"  # Change this to your actual file
df = pd.read_csv(csv_file, header=None, names=["S.No", "Roll No", "Marks"])

# Define extended ranges
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
labels = [
    "0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79",
    "80-89", "90-99", "100-109", "110-119", "120-129", "130-139", "140-149"
]

# Categorize marks into bins
df["Range"] = pd.cut(df["Marks"], bins=bins, labels=labels, right=False)

# Count number of students in each category
count_data = df["Range"].value_counts().sort_index()

# Print statistics
print(f"Total Users: {len(df)}\n")
for label, count in count_data.items():
    print(f"People with marks in range {label}: {count}")

# Plot the distribution
plt.figure(figsize=(12, 6))
plt.bar(count_data.index, count_data.values, color='skyblue')
plt.xlabel("Marks Range")
plt.ylabel("Number of Candidates")
plt.title("""TEACHERS RECRUITMENT BOARD
DIRECT RECRUITMENT FOR THE POST OF BLOCK EDUCATIONAL OFFICER – 2019-2020
TO 2020-2022
(Directorate of Elementary Education)""")

plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.xticks(rotation=45)
plt.show()



