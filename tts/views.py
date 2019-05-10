from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import HttpResponse
import librosa as lr
from eval import Eval
from django.core.serializers import serialize
from . models import Maratron


def index(request):
    print("index.......")
    return render(request, 'tts/index.html')

#여자 목소리를 디폴트로 지정하여 모델 초기화 
eval=Eval()
eval.init()

# Ajax
# textToSpeech
@csrf_exempt # 403 error 제어
def synthesize(request):
    print("view 도착")
    # text = request.POST['text'].strip()
    text = request.POST.get('text',False)
    # voiceType = request.POST['voiceType'].strip()
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

    path_dir = '/static/audio/'
    audio_file = path_dir + eval.text(text, voice_choice)
    print(audio_file)
    audio = {"audio":audio_file}
    audio = json.dumps(audio)

    print(audio)
    return HttpResponse(audio, content_type="application/json")

# audioStore
def audioStore(request):
    href = request.GET['href']
    # print(href)
    choice = href[-1]
    # print(choice)
    
    # index를 기준으로 데이터 받아오기
    data = Maratron.objects.get(index = choice)
    print("data는 ", data)
    
    serialize_data = serialize('json', [data, ])
    print("serialize는 ", serialize_data)
    serialize_data = serialize_data.strip('[]')
    print("strip은  ", serialize_data)
    # serialize_data = json.loads(serialize_data)
    # fields_data = serialize_data["fields"]
    # print("fields는   ", fields_data)

    return HttpResponse(json.dumps(serialize_data), 'application/json')
   