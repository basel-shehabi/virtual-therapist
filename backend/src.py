import openai
import gradio
import os
import logging

from dotenv import load_dotenv

load_dotenv() # Load environment variables
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p') # Fancy logging

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is not None:
    logging.info('Retrieved API Key successfully!') # Used to test whether or not we retrieved the API key successfully

messages = [{"role": "system", "content": "You are a trained and qualified psychiatrist"}]

def CustomChatGPT(feelings):
    messages.append({"role": "user", "content": feelings})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Old code using gradio goes below, will work on uplifting to fastAPI.
'''
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Virtual Therapist")
demo.launch(share=True)
'''