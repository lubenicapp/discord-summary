from openai import OpenAI
from decouple import config

client = OpenAI()

MODEL = "gpt-3.5-turbo"
BASE_MESSAGES = [
    {"role": "system", "content": """
Je t'envoie les extraits d'une conversation discord. Tu dois résumer les sujets qui ont été abordés et quelles sont les positions de chacun
Dis directement qui a parlé de quoi, sans introduire le contexte que c'est un Discord, car on le sait
Tu ne dois envoyer que le résumé, pas de phrase d'introduction ou autre
Tu dois associer a chaque participant un adjectif pour le décrire, par example : Jean a été le plus drôle
Tu dois toujours être très respectueux quand tu parle du Duc, en utilisant des adjectifs valorisant si possible
""" }
]




def tldr(content):
    messages = BASE_MESSAGES
    prompt = {"role": "user", "content": content}

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[*messages, prompt]
    )

    return completion.choices[0].message.content
