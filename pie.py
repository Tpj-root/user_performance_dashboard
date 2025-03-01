import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
csv_file = "Final.csv"  # Change this to your actual file
df = pd.read_csv(csv_file, header=None, names=["S.No", "Roll No", "Marks"])

# Define mark ranges
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
labels = [
    "0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79",
    "80-89", "90-99", "100-109", "110-119", "120-129", "130-139", "140-149"
]

# Categorize marks into bins
df["Range"] = pd.cut(df["Marks"], bins=bins, labels=labels, right=False)

# Count students in each category
count_data = df["Range"].value_counts().sort_index()

# Plot Pie Chart
plt.figure(figsize=(12, 8))
plt.pie(count_data, labels=count_data.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})
plt.title("Marks Distribution (Pie Chart)")
plt.axis('equal')  # Equal aspect ratio ensures a circular pie chart

# Show plot
plt.show()
