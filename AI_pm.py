import os
from openai import OpenAI

# Initialisation de l'assistant Product Manager
def create_assistant_PM(writing_demand: str):
    client = OpenAI(
        api_key=os.getenv("XAI_API_KEY"),
        base_url="https://api.x.ai/v1"
    )

    system_message = f"""you're a senior Product Manager, create a complete user story for the following writing demand: {writing_demand}"""

def generate_reponse_ia(client, system_message, prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="grok-2-mini",  # Utilisation du modèle Grok
            messages=[
                {
                    "role": "system",
                    "content": system_message
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
    My_user_story = """Your user story"""

    # create assistant Product Manager
    client, system_message = create_assistant_PM(My_user_story)
    # generate a response with assistant
    prompt = f"""Write a user story for the following writing demand: {My_user_story}"""
    reponse = generate_reponse_ia(client, system_message, prompt)

    print(reponse)
