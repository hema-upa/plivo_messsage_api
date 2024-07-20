
def map_customer_data(customer_csv_rows):
    mapped_data = []
    headers = customer_csv_rows[0]

    for row in customer_csv_rows[1:]:
        row_dict = dict()
        for i in range(len(headers)):
            row_dict[headers[i]] = row[i]
        mapped_data.append(row_dict)
    return mapped_data
