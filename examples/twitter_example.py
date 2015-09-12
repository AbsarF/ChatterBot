from chatterbot import ChatBot


chatbot = ChatBot("ChatterBot",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
    io_adapter="chatterbot.adapters.io.TwitterAdapter",
    database="../database.db",
    consumer_key="xxx",
    consumer_secret="xxx"
)

'''
Respond to mentions on twitter.
The bot will follow the user who mentioned it and
favorite the post in which the mention was made.
'''

user_input = "Type something to begin..."

print(user_input)

while True:
    try:
        user_input = chatbot.get_input()

        bot_input = chatbot.get_response(user_input)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break

