import csv
import json
import unittest

class TestPass(unittest.TestCase):
    def test_csv_column_count(self):
        with open('profiles1.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            assert len(headers) == 12

    def test_csv_row_count(self):
        with open('profiles1.csv', encoding='utf-8') as f:
            reader = list(csv.reader(f))
            assert len(reader) - 1 > 900

    def test_json_row_count(self):
        with open('profiles1.json', encoding='utf-8') as f:
            data = json.load(f)
            assert len(data) > 900

    def test_json_keys(self):
        with open('profiles1.json', encoding='utf-8') as f:
            data = json.load(f)
            expected_keys = expected_keys = {
    "Givenname", "Surname", "Streetaddress", "City", "Zipcode",
    "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
    "Telephone", "Birthday", "ConsentToContact"
}
            for entry in data:
                assert expected_keys.issubset(entry.keys())
