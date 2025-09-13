import requests
from django.http import JsonResponse
from django.conf import settings

# Envoi d'un message WhatsApp
def send_whatsapp_message():
    # token = "EAAQcQV5uSMMBPesGB75plrCqY7IkRiMAogZBH0TNGFNi6vA1sfjkBpRUbchCTXCJfF0ZBbZCVxfZA66kcifGT8NFc18W89hPXkmTPS05CFTNIMPzOiRoZB04keuGxbkqQpOvVAZBAWMUDASoPJisSQfvOvWEiCzrI3dImcoWs4AyFx6Njej3IV9oZBZAK7euLysYjYZCefAq6ZAeW5DcVPMqNstcLfZCWzAWkZCLMhZCJv3f9xQZDZD"
    token = "EAAQcQV5uSMMBPb4QJZBZBTma0IOnqM1nM1d8nevDfdY5qnIFqob0B16lIZCMHpk46VDwcHGXxXZA9Xn2ivDno94Oa5dm5XIpZAudUeMA4qy3rLgqVBwTE2J1Bt1E1quCzrHrpqy0Qs1i9nTdxtVQlYZBJEOGjyMtVHqLUtbWKwdR3JptwVjDVEZCvOhNwWCYEjLbn1wJbe3FcpTTaSsZB9ABqbeRPZBnHJ5QWzXp7mq06nwZDZD"
    url = "https://graph.facebook.com/v22.0/814154635108152/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        # "to": "25769393905",  # Numéro de herve
        "to": "25776973103",  # Numéro de lionel
        "type": "text",
        "text": {"body": "Salut, ceci est un test depuis Django 🚀"}
    }

    response = requests.post(url, headers=headers, json=data)
    return JsonResponse(response.json())

print(send_whatsapp_message())
