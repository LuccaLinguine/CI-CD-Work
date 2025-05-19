import unittest
import csv

class TestGeneratedCSV(unittest.TestCase):

    # Get file
    def setUp(self):
        with open('profiles1.csv', 'r') as f:
            self.reader  = list(csv.reader(f))

    # Check columns
    def test_columns(self):
        header = self.reader[0]
        self.assertEqual(len(header), 12, f"Expected 12 columns, got {len(header)}")

    # Check rows
    def test_rows(self):
        row_count = len(self.reader)
        self.assertGreater(row_count, 900, f"Expected +900 rows, got {row_count}")


if __name__ == '__main__':
    unittest.main()
