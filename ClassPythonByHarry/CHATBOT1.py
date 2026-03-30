# from openai import OpenAI

# key1=""


# messages=[]

# client=OpenAI(
#     api_key=key1,
#               )



# def completion(message):
#     global messages
#     messages.append(
#         {
#             "role":"user",
#             "content":message
#         }
#     )
#     chat_complition=client.chat.completions.create(messages=messages,model="gpt-4o")

#     message={
#         "role":"assistant",
#         "content":chat_complition.choices[0].message.content
#     }
#     messages.append(message)
#     print(f"Jarvis {message['content']}")

# if __name__=="__main__":
#     print(f"Jarvis: Hi I am Jarvis, How may I help you\n")
#     while True:
#         user_question=input()
#         print(f"User : {user_question}")
#         completion(user_question)






