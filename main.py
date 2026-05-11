from dotenv import load_dotenv
from openai import OpenAI
import json
import system_prompt


load_dotenv()

client = OpenAI()


try:
    with open("history.json", "r") as f:
        message_history = json.load(f)
except (FileNotFoundError, json.JSONDecodeError, IndexError):
    message_history = [
        {"role": "system", "content": system_prompt.SYSTEM_INPUT},
    ]


def toggle(toggle):
    if toggle == "Off":
        message_history[2]["content"] = system_prompt.FAST
    else:
        message_history[2]["content"] = system_prompt.SYSTEM_INPUT


def get_reply(user_message):
    message_history.append({"role": "user", "content": user_message})

    response = client.responses.create(
        model="gpt-5-mini",
        tools=[{"type": "web_search"}],
        input=message_history
    )

    message_history.append({"role": "assistant", "content": response.output_text})

    with open("history.json", "w") as f:
        json.dump(message_history, f, indent=2)
    
    return (response.output_text)
    



    

   


    

   

