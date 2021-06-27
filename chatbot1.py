from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.logic import LogicAdapter

def get_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold' : 0.50
        }
    ]
    )
    
    trainer=ListTrainer(bot)
    while True:
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if(usrText.strip() == 'Bye' or usrText.strip() == 'bye'  or usrText.strip() ==  'BYE' or usrText.strip() == 'BYe' or usrText.strip() == 'bYe') :
            return('Bye')
            break
