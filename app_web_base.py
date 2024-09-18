import gradio

# defines response message and format
def respond(history, new_message):
    print(history)
    return history + [[new_message, 'Message Recieved!']]

# using the bot
with gradio.Blocks() as my_bot:
    chatbot = gradio.Chatbot()
    user_input = gradio.Text()

    user_input.submit(respond, [chatbot, user_input], chatbot)
    
my_bot.launch()