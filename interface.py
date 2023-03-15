
import openai
import tkinter as tk

# Initialisez la clé API d'OpenAI
openai.api_key = "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"

# Initialisez la connexion à l'API OpenAI
model_engine = "text-davinci-003" # Choisir le modèle de GPT-3 à utiliser
prompt = "" # Initialiser la première requête
max_tokens = 60 # La quantité de tokens pour chaque réponse
temperature = 0.7 # La température pour la génération de texte

root = tk.Tk()
root.title("Net4moly")

chat_display = tk.Text(root, height=30, width=80)
input_entry = tk.Entry(root, width=80)
send_button = tk.Button(root, text="Envoyer", command=lambda: send_message())

chat_display.pack()
input_entry.pack()
send_button.pack()


def send_message():
    # Obtenir le texte de l'entrée utilisateur
    user_input = input_entry.get()

    # Envoyer la requête à l'API OpenAI
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + user_input,
        max_tokens=max_tokens,
        temperature=temperature
    )

    # Récupérer la réponse de l'API OpenAI
    message = response.choices[0].text

    # Afficher la réponse dans le widget Text
    chat_display.insert(tk.END, "User: " + user_input + "\n")
    chat_display.insert(tk.END, "Net4moly Assistant: " + message + "\n")

    # Réinitialiser l'entrée utilisateur
    input_entry.delete(0, tk.END)
root.mainloop()
