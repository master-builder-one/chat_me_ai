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
1. Obtain your Google Gemini API Key from [here](https://aistudio.google.com/app/apikey) and add it to your `.env` file.
2. Get your Meta Developer WhatsApp API key after creating a META developer account and adding WhatsApp as a product. Create one [here](https://developers.facebook.com/). Add your Temporary Access token to `FB_DEV_ACCESS_TOKEN` in your `.env` file. Retrieve your Phone number ID from Meta developer's dashboard and include it in your `.env` file.
3. In the API Setup section of your Meta Developer Dashboard, add the phone number you wish to use the application with.
4. Configure ngrok using the [provided guide](https://ngrok.com/docs/getting-started/?os=windows). Remember to save the port number you use in your `.env` file. For now, the `run.py` does not support step 5 - Skip it.
5. Follow [this guide](https://developers.facebook.com/docs/whatsapp/sample-app-endpoints) to configure webhooks with Glitch for your WhatsApp account. Utilize the `server.js` file provided in the repository. Replace the URL in line 32 of `server.js` with your ngrok domain.
6. Ensure you've installed the required dependencies as indicated above. Run the application using `run.py` and send a message to the provided number.

NOTE: Do not use quotes in your .env files

Example:
1. Run the application: `python run.py`
2. Send a message to the number given to you by Meta API.


Inspired by Dave Ebbelbar's YouTube Guide: https://www.youtube.com/watch?v=3YPeh-3AFmM