import csv
from datetime import datetime

FILE_NAME = "data.csv"

def add_expense(amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])


def get_total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[1])

    except FileNotFoundError:
        pass

    return total