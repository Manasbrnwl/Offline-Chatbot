from vosk import Model,KaldiRecognizer
import pyaudio

model = Model(r"Chatbot\\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model,44100)

mic = pyaudio.PyAudio()
stream = mic.open(rate=44100,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=1024)
stream.start_stream()

def listen():
    print("Listening.....")
    while True:
        data = stream.read(1024)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            Text = text[14:-3]
            print(f"You said : {Text}")
            
            if len(Text)>0:
                return Text
# print(listen())