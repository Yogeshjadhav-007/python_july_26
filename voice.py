from gtts import gTTS
import os
text=input("Enter text:")
tts=gTTS(text=text,lang="en")
tts.save("voice.mp3")
os.startfile("voice.mp3") 