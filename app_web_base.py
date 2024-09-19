from openai import OpenAI
import gradio

client = OpenAI(
    api_key = 'KEY'
)

messages = []
prompt = {'role': 'user', 'content': 'You are a quizzer. Present the user with a multiple choice question to practice for a BLANK, they have to respond by typing a, b, c, d or e. Wait until the user responds before telling them the correct answer and listing another related question.'}
# replace BLANK with quiz subject (for some reason keeping it as BLANK prompts the AI to give geography related questions)
# provide the user with a quiz question
# 5 possible answers via mult-choice question
# answer should be correct or not
# then present another question
messages.append(prompt)

# creates a response for user input
def respond(history, new_message):
    # add the user input to the messages
    messages.append({'role': 'user', 'content': new_message})

    # send the api call
    response = client.chat.completions.create(messages = messages, model = "gpt-3.5-turbo")

    # obtain response
    assistant_message = response.choices[0].message
    messages.append(assistant_message)
    return history + [[new_message, assistant_message.content]]

# using the bot
with gradio.Blocks() as my_bot:
    chatbot = gradio.Chatbot()
    user_input = gradio.Text()
    user_input.submit(respond, [chatbot, user_input], chatbot)
    
my_bot.launch()