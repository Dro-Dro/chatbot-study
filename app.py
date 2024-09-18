from openai import OpenAI

client = OpenAI(
    api_key = 'KEY'
)

messages=[]

# user input
user_input = input('Enter your prompt: ')

# create prompt
messages.append({'role': 'user', 'content': user_input})

# send the api call
response = client.chat.completions.create(messages = messages, model = "gpt-3.5-turbo")

# display response in console
print(response.choices[0].message.content)