from openai import OpenAI

from dotenv import load_dotenv
import os
import time

load_dotenv()

def query_ai(messages,model="gpt-3.5-turbo"):
    client = OpenAI(
        api_key = os.getenv('OPENAI_API_KEY'),
        base_url = os.getenv('OPENAI_BASE_URL') or "https://api.openai.com/v1"
    )
    for i in range(8): # retry 3 times
        #print(messages)
        print("waiting AI response....")
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model,
                )
        except Exception as e:
            print("An unexpected error occurred: ", e)
            time.sleep(1)
            continue
        #print(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content