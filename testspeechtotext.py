from watson_developer_cloud import SpeechToTextV1
import json

stt = SpeechToTextV1(username="username", password="password")
audio_file = open("output.wav", "rb")
print(json.dumps(stt.recognize(audio_file, content_type="audio/wav"), indent=2))
