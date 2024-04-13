# Imports
from flask import Flask, request, make_response
import google.generativeai as genai
from dotenv import load_dotenv, dotenv_values
from message_handling import post_message, prompt_message, pretty_print_response
import os
import logging


# Configurations from the .env file
config = dotenv_values(".env")
ACCESS_TOKEN = config["FB_DEV_ACCESS_TOKEN"]
PHONE_NUMBER_ID = config["PHONE_NUMBER_ID"]
VERSION = config["VERSION"]
API_KEY = config["GOOGLE_API_KEY"]
NGROK_PORT = config["NGROK_PORT"]

# Flask app will catch requests from META API
app = Flask (__name__, template_folder='template')
@app.route("/", methods=["POST"])
def webhooks():
    if request.method == "POST":
        data = eval(request.data)
        message = data["text"]["body"]
        print("User Message: ",message[:30])
        #print(pretty_print_response(request))
        model_response = prompt_message(chat, message)
        return_number = data["to"]
        print("Model Message: " +model_response[:30] + "...")
        reply = post_message(model_response, return_number, VERSION, ACCESS_TOKEN, PHONE_NUMBER_ID)
        #print("Sent response status: "+ (str)(reply.status_code))
        response = make_response("<h1>Success</h1>")
        response.status_code = 200
        return "Success", 200
    else:
        response = make_response("<h1>Success</h1>")
        response.status_code = 400
        return "Bad Request", 400



    
if __name__ == "__main__":
    # Model configuration:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('models/gemini-1.0-pro-latest')

    # Initialize chat with Gemini
    chat = model.start_chat() 

    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=NGROK_PORT)