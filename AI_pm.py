import os
from openai import OpenAI

# Initialisation du client
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def obtenir_reponse_ia(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="grok-2-mini",  # Utilisation du modèle Grok
            messages=[
                {
                    "role": "system",
                    "content": "Vous êtes un assistant IA utile et amical."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur: {str(e)}"

# Exemple d'utilisation
if __name__ == "__main__":
    reponse = obtenir_reponse_ia("Bonjour, comment vas-tu?")
    print(reponse)