import wave,sys,urllib
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import json

# Open text file
f = open(sys.argv[1]+".txt", 'r')
message = str(f.readlines()).decode('unicode_escape').encode('ascii','ignore')

# Bluemix credentials
text_to_speech = TextToSpeechV1(
    username='c287d648-26ab-41f8-9e16-58c9764bbe9a',
    password='4IUV2PBcqZBZ',
    x_watson_learning_opt_out=True)

# Different voices for the text to speech
# print(json.dumps(text_to_speech.voices(), indent=2))


# Write .wav file
with open(join(dirname(__file__), "static/"+sys.argv[1]+".wav"),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(message, accept='audio/wav',
                                  voice="en-US_AllisonVoice"))


'''

Different pronunciations and speech costumizations

print(
    json.dumps(text_to_speech.pronunciation(
        'Watson', pronunciation_format='spr'), indent=2))

print(json.dumps(text_to_speech.customizations(), indent=2))
'''




