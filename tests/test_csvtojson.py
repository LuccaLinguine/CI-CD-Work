import pandas
import unittest
import os

df = pandas.read_csv("profiles1.csv")

#Takes csv file path as input, returns the csv converted to json
def csv_to_json(csv_file):
    df = pandas.read_csv(csv_file)
    df.to_json("data.json", orient= "records", indent = 4, force_ascii = False)

csv_to_json("profiles1.csv")

jsondf = pandas.read_json("data.json")

class TestPipeline(unittest.TestCase):

    def test_file_exist(self):
        self.assertTrue(os.path.isfile("profiles1.csv"))

    def test_amt_col(self):
        self.assertEqual(len(df.columns),12, f"Columns != 12, {len(df.columns)} exist.")

    def test_amt_row(self):
        self.assertGreaterEqual(len(df), 900, f"Less than 900 rows in the csv, there is only {len(df)}")

    def test_json_exists(self):
        self.assertTrue(os.path.isfile("data.json"),"data.json does not exist")

    def test_json_rows(self):
        self.assertGreaterEqual(len(jsondf), 900, f"less than 900 rows in the json, there is only {len(jsondf)}")

    def test_json_properties(self):
        required_properties = [
            "Givenname", "Surname", "Streetaddress", "City", "Zipcode",
            "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"
        ]
        for prop in required_properties:
            with self.subTest(property=prop):

                self.assertIn(prop, jsondf.columns, f"{prop} is missing")

                self.assertTrue(jsondf[prop].notna().all() and (jsondf[prop] != '').all(), f"{prop} is empty or contains null values")

if __name__ == '__main__':
    unittest.main()
