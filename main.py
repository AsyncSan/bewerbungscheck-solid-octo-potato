import os
import openai
import gradio
import gunicorn

# Set environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Set up Gradio app
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Bewerbungschecker", server_name="0.0.0.0")

demo.launch(share=True)

