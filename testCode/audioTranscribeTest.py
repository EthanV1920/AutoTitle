import openai
import configparser

config = configparser.ConfigParser()
config.read('testCode/config.ini')

openai.api_key = config['KEYS']['OPENAI_API_KEY']

audio_file= open("auido/Embrace God's Gifts and Impact Lives Audio Only Short.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)