import requests


# Posts the message to WhatsApp server
def post_message(ai_response, return_to, VERSION, ACCESS_TOKEN, PHONE_NUMBER_ID):
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }
    data = {
        "messaging_product": "whatsapp",
        "to": return_to,
        "text": { "body": ai_response},
    }
    response = requests.post(url, headers=headers, json=data)
    return response

# Extracts the text component from a given WhatsApp text and returns the models response
def prompt_message(chat, message):    
    response = chat.send_message(message)
    return response.text

def pretty_print_response(req):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.data,
    ))