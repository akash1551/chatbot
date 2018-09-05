from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

while True:
    message = input('You: ')
    if message.strip() != 'Bye':
        # Get a response to an input statement
        reply = chatbot.get_response(message)
        print('Chatbot: ', reply)
    else:
        # Get a response to an input statement
        reply = chatbot.get_response(message)
        print('Chatbot: Bye')
        break
