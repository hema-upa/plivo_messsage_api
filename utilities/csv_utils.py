from constants import CSV_SEPARATOR
import csv

def create_csv_file(file_path, headers):
    header = CSV_SEPARATOR.join(headers)
    with open(file_path, "w") as csv_file:
        csv_file.write(header)
        csv_file.write("\n")
    print(f"CSV file created: {file_path} with headers: {header}.")

def add_data_to_csv(file_path, csv_data):
    with open(file_path, "a") as csv_file:
        for csv_row_data in csv_data:
            csv_file.write(CSV_SEPARATOR.join(csv_row_data) + "\n")

def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)
