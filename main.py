import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
  question = input("\033[34mQuelle est la question?\n\033[31m")
  print('\033[0m' + question + '\n')
  if question.lower() == "exit":
    print("\033[31mGOODBYE!\033[0m")
    break
  
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": "You are an assistant, answer the given question."
    }, {
      "role": "user",
      "content": question
    }])
  #print(completion)
  print('\033[33m' + completion['choices'][0]['message']['content'] + '\n')
  print('\033[32m' + completion.choices[0].message.content + '\n')