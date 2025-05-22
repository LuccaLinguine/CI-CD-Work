import pandas

def csv_to_json(csv_file):
    df = pandas.read_csv(csv_file)
    df.to_json("profiles1.json", orient="records", force_ascii=False, lines=True)

if __name__ == '__main__':
    csv_to_json("profiles1.csv",)