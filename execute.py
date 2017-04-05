import wave,sys,urllib
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import json

f = open(sys.argv[1]+".txt", 'r')
message = str(f.readlines()).decode('unicode_escape').encode('ascii','ignore')

text_to_speech = TextToSpeechV1(
    username='c287d648-26ab-41f8-9e16-58c9764bbe9a',
    password='4IUV2PBcqZBZ',
    x_watson_learning_opt_out=True)

print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), "static/"+sys.argv[1]+".wav"),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(message, accept='audio/wav',
                                  voice="en-US_AllisonVoice"))

print(
    json.dumps(text_to_speech.pronunciation(
        'Watson', pronunciation_format='spr'), indent=2))

print(json.dumps(text_to_speech.customizations(), indent=2))

#
# def play_sound(file):
#     chunk=1024
#     wf=wave.open(file,'rb')
#     p=pyaudio.PyAudio()
#     stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
#     data=wf.readframes(chunk)
#     while data!='':
#         stream.write(data)
#         data=wf.readframes(chunk)
#     stream.close()
#     p.terminate()
#

#res=urllib.URLopener()
#res.retrieve("https://text-to-speech-demo.mybluemix.net/api/v1/synthesize?download=true&text="+message,"static/"+sys.argv[1]+".wav")


# play_sound("transcript.wav") 

