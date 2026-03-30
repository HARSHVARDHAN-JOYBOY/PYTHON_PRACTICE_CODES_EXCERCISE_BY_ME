import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)
chat=client.chats.create(model="gemini-2.0-flash")

print("Jarvis is Online !")


while True:
    user_input=input("You : ")
    if user_input.lower() in ['exit','quit',"bye","goodbye"]:
        print("thank you foe using me Have a nice day sir !")
        break
    try:
        response=chat.send_message(user_input)
        print(f"\n Jarvis : {response.text}")
        print("_"*20)

    except Exception as e:
        print(f"\njarvis : an unexpected error occured ! {e}")



