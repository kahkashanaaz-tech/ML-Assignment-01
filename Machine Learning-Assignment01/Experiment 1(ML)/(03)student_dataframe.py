import pandas as pd

# Create a DataFrame
data = {
    "Student Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [72, 85, 68, 91, 88],
    "Attendance": [88, 92, 76, 95, 81]
}

df = pd.DataFrame(data)

# Display the complete DataFrame
print("Complete Student Records:")
print(df)

# Filter students who scored above 80 marks
filtered_df = df[df["Marks"] > 80]

# Display filtered records
print("\nStudents who scored above 80 marks:")
print(filtered_df)