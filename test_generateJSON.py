import unittest
import csv
import json

class TestGenerateJson(unittest.TestCase):

    # Set up variables
    def setUp(self):

        # Get expected properties from CSV file
        with open("profiles1.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            self.expected_keys = next(reader) # Get only CSV header

        # Load JSON file
        with open("data.json", "r", encoding="utf-8") as f:
            self.json_data = json.load(f)

    # Check headers
    def test_headers(self):
        # Check if the JSON data has the same headers as the CSV file
        self.assertEqual(set(self.json_data[0].keys()), set(self.expected_keys), "JSON keys do not match CSV headers")

    # Check rows
    def test_rows(self):
        self.assertGreaterEqual(len(self.json_data), 900, "JSON data has less than 900 rows")

if __name__ == "__main__":
    unittest.main()