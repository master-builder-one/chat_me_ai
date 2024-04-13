# chat_me_ai

Chat with Google Gemini in WhatsApp

## Requirements
1. Meta Developer account
2. Google AI Studio API key 
2. ngrok
3. Python version >= 3.9 

## Installation
1. Clone this repository: `git clone https://github.com/kaizoku-x/chat_me.git`
2. Install required packages: `pip install -r requirements.txt`

## Usage
1. Get your Google Gemini API Key here: https://aistudio.google.com/app/apikey. Add it to your .env file
2. Get you Meta Developer Whatsapp API key after you have created a META developer account and added WhatsApp as a product. Create one here: https://developers.facebook.com/ . Add your Temporary Access token to FB_DEV_ACCESS_TOKEN in your .env file. Get your Phone number ID and add it to your .env file.
3. Under API Setup add the phone number you would like to add to use your application with.
4. Configure ngrok with the following guide: https://ngrok.com/docs/getting-started/?os=windows. Make sure the port number into your .env file. For now the run.py does not support, step 5 -Skip it.
5. Follow this guide to configure webhooks with Glitch on your WhatsApp account: https://developers.facebook.com/docs/whatsapp/sample-app-endpoints. Use the server.js file given in the repository. Replace url in server.js line 32 with your ngrok domain.
6. Make sure to install requirements as indicated above. Run the application "run.py", and send a message to the given number

NOTE: Do not use quotes in your .env files

Example:
1. Run the application: `python run.py`
2. Send a message to the number given to you by Meta API.


Inspired by Dave Ebbelbar's YouTube Guide: https://www.youtube.com/watch?v=3YPeh-3AFmM