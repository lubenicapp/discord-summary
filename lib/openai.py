from openai import OpenAI
from decouple import config

client = OpenAI()

MODEL = "gpt-3.5-turbo"
BASE_MESSAGES = [
    {"role": "system", "content": "Je t'envoie les extraits d'une conversation discord. Tu dois résumer les sujets qui ont été abordés et quelles sont les positions de chacun"},
    {"role": "system", "content": "Tu dois présenter le résumé comme un procès verbal"},
    {"role": "system", "content": "Tu ne dois envoyer quele résumé, pas de phrase d'introduction ou autre"},
    {"role": "system", "content": "Tu dois associer a chaque participant un adjectif pour le décrire, par example : Jean a été le plus drôle"},
]


def tldr(content):
    messages = BASE_MESSAGES
    prompt = {"role": "user", "content": content}

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[*messages, prompt]
    )

    return completion.choices[0].message.content
