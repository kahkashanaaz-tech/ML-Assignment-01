import numpy as np

# Create a NumPy array containing internal marks of 10 students
marks = np.array([72, 85, 68, 91, 77, 88, 65, 95, 80, 74])

# Calculate statistical values
mean = np.mean(marks)
median = np.median(marks)
std = np.std(marks)
maximum = np.max(marks)
minimum = np.min(marks)

# Print results
print("Internal Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
print("Maximum:", maximum)
print("Minimum:", minimum)




