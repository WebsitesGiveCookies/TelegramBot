from requests import post

def webhook():
    chat_ID = "7113566967"
    message = "O"
    url = "https://api.telegram.org/bot7113566967:AAHrW_vKr-_mVM0U--5rFg9MdBEqINSTnfk/sendMessage"
    answer = {
        "chat_id": chat_ID,
        "text": message,
    }
    response = post(url, json=answer)
    print(response.text)
webhook()
