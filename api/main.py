from flask import Flask, request
from requests import post

app = Flask(__name__)


@app.route("/")
def index():
    return "website is alive"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    chat_ID =  data["message"]["chat"]["id"]
    message = data["message"]["text"]
    url = "https://api.telegram.org/bot7113566967:AAHrW_vKr-_mVM0U--5rFg9MdBEqINSTnfk/sendMessage"
    answer = {
        "chat_id": chat_ID,
        "text": message,
    }
    response = post(url, json=answer)
    return response 


# app.run()

@app.get("/send-reminder")
def send_reminder():
    
    answer = {
        "chat_id": -4161947339,
        "text": "monkey",
    }
    response = post(url="https://api.telegram.org/bot7113566967:AAHrW_vKr-_mVM0U--5rFg9MdBEqINSTnfk/sendMessage", json=answer)
    return response.json()
