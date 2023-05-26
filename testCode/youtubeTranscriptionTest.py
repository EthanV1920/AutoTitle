import openai
import configparser

config = configparser.ConfigParser()
config.read('testCode/config.ini')

openai.api_key = config['KEYS']['OPENAI_API_KEY']


decorationText = "This is the transcription of a YouTube video. Based on this transcription, make a catchy title and description that is less than 140 characters Transcription: "
transcription = open("captions/captions.txt", "r").read()
promptIn = decorationText + transcription
promptIn = promptIn.replace("\n", " ")

print(promptIn)

completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": promptIn}])
reply = completion.choices[0].message.content

genText = open("GeneratedText.txt", "w+")
genText.write(reply)
genText.close()
