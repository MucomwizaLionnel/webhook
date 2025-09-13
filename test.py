import requests

# token = "EAAQcQV5uSMMBPTY0xRbfq0lYjJiffhG6qgvSGaPYWBY1FFo2vqqs3UyJKqgl98ezZBKTr8Di18yxpJPu70btrvuCJoSnwKhdsoL1xFJDSIx3ryBgrITI1WxCQUEveJaihgl6joeC2RxcL3NpMZApOyEYRe1DwmflXlwNcRACnl2ZACreAgVidnRJcLFYrgWvgkYheXo8nqdRSbc0qwPTfcuZAnZAYEYhe9UiiKm9GwQZDZD"


def send_whatsapp_template_message():
    token = "EAAQcQV5uSMMBPTY0xRbfq0lYjJiffhG6qgvSGaPYWBY1FFo2vqqs3UyJKqgl98ezZBKTr8Di18yxpJPu70btrvuCJoSnwKhdsoL1xFJDSIx3ryBgrITI1WxCQUEveJaihgl6joeC2RxcL3NpMZApOyEYRe1DwmflXlwNcRACnl2ZACreAgVidnRJcLFYrgWvgkYheXo8nqdRSbc0qwPTfcuZAnZAYEYhe9UiiKm9GwQZDZD"
    url = "https://graph.facebook.com/v22.0/814154635108152/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": "257769393905",
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

print(send_whatsapp_template_message())
