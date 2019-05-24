from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import HttpResponse
import librosa as lr
from eval import Eval
from django.core.serializers import serialize
from .models import Maratron
import base64
from ttsProject.settings import MEDIA_URL


def index(request):
    audiobook_list = Maratron.objects.all()
    print("index페이지")
    print(audiobook_list)
    return render(request, 'tts/index.html',{"audiobook_list":audiobook_list})

#여자 영어 목소리를 디폴트로 지정하여 모델 초기화 
eval=Eval()

# Ajax
# textToSpeech
@csrf_exempt # 403 error 제어
def synthesize(request):
    print("view 도착")
    text = request.POST.get('text',False)
    voiceType = request.POST.get('voiceType')
    print(text)
    print(voiceType)
    voice_choice = 1  # default == en_female 

    if (voiceType == 'en_female') : 
        voice_choice = 1
    elif (voiceType == 'en_male') : 
        voice_choice = 2
    else :
        voice_choice = 3
   
    '''
    path_dir = '/static/audio/'
    audio_file = path_dir + eval.text(text, voice_choice)
    print(audio_file)
    audio = {"audio":audio_file}
    '''
    audio = eval.text(text, voice_choice)
    audio = base64.b64encode(audio)
    return HttpResponse(audio, content_type="audio/wav")

# audioStore
def audioStore(request):
    choice = request.GET['id']
    print("choice는 ", choice)
    
    # id를 기준으로 데이터 받아오기
    entry = Maratron.objects.get(id = choice)
    data = entry.dic()
    print("data는 ", data)
    data['contents'] = MEDIA_URL +  data['contents']
    print(data['contents'])
    data['audio'] = MEDIA_URL +  data['audio']
    data['thumnail'] = MEDIA_URL +  data['thumnail']
    print("수정된 data는 ", data)
 
    return HttpResponse(json.dumps(data), 'application/json')