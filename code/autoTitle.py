import openai
import configparser

config = configparser.ConfigParser()
config.read('/Users/ethanvosburg/Downloads/AutoTitle/code/config.ini')

openai.api_key = config['KEYS']['OPENAI_API_KEY']

audio_file= open("/Users/ethanvosburg/Downloads/AutoTitle/auido/Embrace God's Gifts and Impact Lives Audio Only.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)