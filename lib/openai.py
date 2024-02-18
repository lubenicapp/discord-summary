from openai import OpenAI
from decouple import config

client = OpenAI()

MODEL = "gpt-3.5-turbo"
BASE_MESSAGES = [
    {"role": "system", "content": """
Je t'envoie les extraits d'une conversation discord. Tu dois résumer les sujets qui ont été abordés et quelles sont les positions de chacun
Dis directement qui a parlé de quoi, sans introduire le contexte que c'est un Discord, car on le sait
Tu ne dois envoyer que le résumé, pas de phrase d'introduction ou autre. Rentre dnas les détails. écris plusieurs paragraphes
n'ai pas peur de faire 20 lignes ou plus.
"""}
]




def tldr(content):
    messages = BASE_MESSAGES
    prompt = {"role": "user", "content": content}

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[*messages, prompt]
    )

    return completion.choices[0].message.content
