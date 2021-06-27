from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('C:/Users/Shivani Singh/AppData/Local/Programs/Python/Python37/gp1/SnisBotLearn/'):
        convData = open('C:/Users/Shivani Singh/AppData/Local/Programs/Python/Python37/gp1/SnisBotLearn/' + file,'r').readlines()
        trainer=ListTrainer(chatbot)
        trainer.train(convData)
setup()
