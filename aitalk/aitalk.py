#coding: utf-8
import requests
#みやびちゃん
#speaker = 'miyabi_west'
#あかねちゃん
speaker = 'akane_west'

speak_text = 'こんばんは'
text = "<voice name=\"" + speaker + "\">" + speak_text + "</voice>"

data = {
    "username": '',
    "password": '',
    "ext": 'aac',
    "text": text,
    "speaker_name": speaker,
    "range": 1.8
    }
r = requests.post('http://webapi.aitalk.jp/webapi/v2/ttsget.php', params=data)

dataPath = "./aitalk.m4a"
f = open(dataPath, 'wb')
f.write(r.content)
f.close()
