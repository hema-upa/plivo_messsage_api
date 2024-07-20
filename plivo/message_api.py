import plivo

def send_message(from_number, destination_number, text):
    try:
        client = plivo.RestClient('<auth_id>','<auth_token>')
        response = client.messages.create(
            src=from_number,
            dst=destination_number,
            text=text,
            url='<domain>',
        )
        return response["message_uuid"]
    except Exception as e:
        print("Error calling send_message api", e)
        raise e

def get_message(message_uuid):
    try:
        client = plivo.RestClient(auth_id="<auth_id>", auth_token="auth_token")
        return client.messages.get(message_uuid=message_uuid)
    except Exception as e:
        print("Error calling get_message api", e)
        raise e
