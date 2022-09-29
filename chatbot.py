from chatterbot import ChatBot
import offlineSpeechRecognition as off
# from chatterbot.trainers import ChatterBotCorpusTrainer
import Speak as sp

chatbot = ChatBot('Thermo')
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")     

def respone():
    query = off.listen()
        
    if 'exit' in query:
        sp.speak('it was nice to talk to you!')
        print('Bot said : it was nice to talk to you!')
    else:
        Query = chatbot.get_response(query)
        sp.speak(Query)
        print(f"Bot said : {Query}")
            
        # if len(Query)>0:
        #     return Query      

respone()