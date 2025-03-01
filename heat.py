import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data from CSV
csv_file = "Final.csv"  # Change this to your actual file
df = pd.read_csv(csv_file, header=None, names=["S.No", "Roll No", "Marks"])

# Reshape marks into a square or rectangular grid for heatmap
num_students = len(df)
grid_size = int(np.ceil(np.sqrt(num_students)))  # Make a square grid

# Fill grid with marks, padding with NaN if needed
marks_array = np.full((grid_size, grid_size), np.nan)
marks_array.flat[:num_students] = df["Marks"].values

# Plot heatmap
plt.figure(figsize=(10, 8))
plt.imshow(marks_array, cmap="hot", aspect="auto", interpolation="nearest")
plt.colorbar(label="Marks")

# Remove axis labels
plt.xticks([])
plt.yticks([])
plt.title("Student Marks Heatmap")

# Show plot
plt.show()
