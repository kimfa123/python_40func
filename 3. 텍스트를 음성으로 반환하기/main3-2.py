from gtts       import gTTS
from playsound  import playsound
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")

#음성변환으로 생성되는 .mp3 파일을 파이썬에서 바로 실행하는 코드를 만들어 봅니다. 