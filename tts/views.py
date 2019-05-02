from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import HttpResponse
import librosa as lr
from eval import Eval

def index(request):
    #print("index.......")
    return render(request, 'tts/index.html')

#female =1 (default)
#male=2
#여자 목소리를 디폴트로 지정하여 모델 초기화 
eval=Eval()
eval.init()

# Ajax
@csrf_exempt # 403 error 제어
def synthesize(request):
    print("view 도착")
    text = request.POST['text'].strip()
    voiceType = request.POST['voiceType'].strip()
    print(text)
    print(voiceType)
    voice_choice = 1  # default == female 
    if (voiceType == 'male') : 
        voice_choice = 2

    path_dir = '/static/audio/'
    audio_file = path_dir + eval.text(text, voice_choice)
    print(audio_file)
    audio = {"audio":audio_file}
    audio = json.dumps(audio)

    print(audio)
    return HttpResponse(audio, content_type="application/json")
