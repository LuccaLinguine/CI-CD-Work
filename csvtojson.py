import csv, json

csv_file = "profiles1.csv"
json_file = "data.json"

# Read CSV
with open(csv_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Warn for empty file
if not data:
    print("Empty CSV file")

# Convert to JSON (with indent for readability)
with open(json_file, mode="w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)