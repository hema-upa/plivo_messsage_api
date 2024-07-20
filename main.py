from utilities.csv_utils import create_csv_file, add_data_to_csv, read_csv_file
from constants import CSV_NAME, RESULT_FILE_NAME
from data.customer_data import CUSTOME_DATA_HEADERS, CUSTOMER_DATA
from utilities.customer_data_mapper import map_customer_data
from plivo.message_api import send_message, get_message
import json


def create_csv():
    create_csv_file(CSV_NAME, CUSTOME_DATA_HEADERS)
    add_data_to_csv(CSV_NAME, CUSTOMER_DATA)

def send_messages(customer_ids):
    csv_rows = read_csv_file(CSV_NAME)
    mapped_data = map_customer_data(csv_rows)
    id_to_customer_data = {
        data["ID"]: data
        for data in mapped_data
    }

    message_responses = []
    for id in customer_ids:
        sms_message = f"{id_to_customer_data[id]['Message']},src={id_to_customer_data[id]['SourceNumber']},dst={id_to_customer_data[id]['DestinationNumber']}"
        src_number = id_to_customer_data[id]["SourceNumber"]
        dst_number = id_to_customer_data[id]["DestinationNumber"]
        msg_uuid = send_message(src_number, dst_number, sms_message)
        msg_details = get_message(msg_uuid)
        message_responses.append({
            id: {
                "src_number": src_number,
                "dst_number": dst_number,
                "msg_text": sms_message,
                "msg_details": msg_details
            }
        })
    
    return message_responses


def main():
    # Create CSV file with data
    create_csv()

    # Accept customer ID as input now
    customer_ids_input = input()
    customer_ids = customer_ids_input.split(",")

    # send messages
    message_responses = send_messages(customer_ids)

    # write results
    with open(RESULT_FILE_NAME, 'w') as result_file:
        json.dump(message_responses, result_file, indent=4)

if __name__ == "__main__":
    main()
