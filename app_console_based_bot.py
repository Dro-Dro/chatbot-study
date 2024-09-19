from openai import OpenAI

# replace 'KEY' with your own OpenAI API Key!
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

while True:
    # send the api call
    response = client.chat.completions.create(messages = messages, model = "gpt-3.5-turbo")

    # display response in console
    print(response.choices[0].message.content)

    # past conversation printed
    messages.append(response.choices[0].message)

    # send prompt again to continue quiz
    messages.append(prompt)

    # user input
    user_input = input('Enter your answer: ')

    # quit chat if user types q
    if user_input == 'q':
        exit()

    # create prompt
    messages.append({'role': 'user', 'content': user_input})