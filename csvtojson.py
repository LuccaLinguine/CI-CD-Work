import pandas as pd

def csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records', indent=4, force_ascii=False)

if __name__ == "__main__":
    csv_to_json('profiles1.csv', 'profiles1.json')
