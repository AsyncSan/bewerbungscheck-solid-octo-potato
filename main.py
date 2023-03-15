import os
import openai
import gradio


# Set environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

messages = [{"role": "system", "content": "Du bist ein Experte für Bewerbungen. Nutzer senden dir ihre Bewerbungen zu und du kritisierst die Bewerbungsschreiben. Schreib was gut an der Bewerbung ist und was noch Verbesserungspotential aufweist. Schreibe in der \"Du-Form\" und schreibe so lang und ausführlich wie nötig um dem Bewerber alle nötigen Tipps zu geben. Erkläre welche Änderungen der Bewerber vornehmen kann und erkläre das Warum. Antworte nur im Kontext der Bewerbungen und bleib in deiner Rolle. Nachfolgend ein Bewerbungsschreiben zum kritisieren:"}]

def CustomChatGPT(Deine_Bewerbung):
    messages.append({"role": "user", "content": Deine_Bewerbung})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Set up Gradio app
gradio.Interface(
    fn=CustomChatGPT,
    inputs = "text",
    outputs = gradio.components.Textbox(label="Resultat"),
    title = "Homeofficecentral - Bewerbungschecker",
    description="<center>Füge deine Bewerbung ein und erhalte direkt konstruktive Kritik und Verbesserungsvorschläge!</br></br>Wir speichern keine Daten zu deiner Bewerbung. Privacy ist uns wichtig und wir wollen nicht in Datenschutzrichtlinien ertrinken</center>",
    article="<h2>Willkommen bei der Bewerbungs-App!</h2> <p>Diese App wurde von der Webseite Homeofficecentral.de erstellt, um Ihnen zu helfen, Ihre Bewerbung zu verbessern. Sie können Ihre Bewerbung in das Textfeld unten einfügen und erhalten innerhalb kurzer Zeit eine Antwort mit Kritik und Verbesserungsvorschlägen. Ihre Daten werden nicht gespeichert oder weitergegeben.</p> <p>Die App analysiert Ihre Bewerbung auf Aspekte wie Rechtschreibung, Grammatik, Stil, Struktur, Inhalt und Anpassung an die Stellenanzeige. Sie erhalten eine Bewertung für jeden Aspekt sowie konkrete Tipps, wie Sie Ihre Bewerbung optimieren können.</p> <p>Um die App zu nutzen, folgen Sie diesen Schritten:</p> <ol> <li>Kopieren Sie Ihre Bewerbung in das Textfeld unten.</li> <li>Klicken Sie auf den orangenen Button “Bewerten”.</li> <li>Warten Sie einige Sekunden, bis die App Ihre Bewerbung analysiert hat.</li> <li>Lesen Sie die Ergebnisse und nehmen Sie die empfohlenen Änderungen vor.</li> </ol> <p>Viel Erfolg bei Ihrer Bewerbung!</p>"
    ).launch(server_name="0.0.0.0")