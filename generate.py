import csv
import random

# Generate 100 rows of sample data
data = [['Column A', 'Column B', 'Column C']]  # Headers
for i in range(100):
    row = [random.randint(1, 100) for _ in range(3)]  # Generating random data for 3 columns
    data.append(row)

# Write data to a CSV file
with open('sample_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Sample data has been generated and saved as 'sample_data.csv'")
