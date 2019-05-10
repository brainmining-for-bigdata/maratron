# maratron DB 생성 방법  
```mysql> create database maratron;
생성된 DB 확인
mysql> show databases;
Project Terminal
```
## default table, tts App 내 DB 모델 생성 및 반영
```(encore) C:\Users\user\Documents\maratron>python manage.py migrate
반영 여부 확인
(encore) C:\Users\user\Documents\maratron>python manage.py showmigrations tts
superUser 계정 생성
(encore) C:\Users\user\Documents\maratron>python manage.py createsuperuser
서버 구동하여 admin 페이지 정상 접속 여부 확인
(encore) C:\Users\user\Documents\maratron>python manage.py runserver
```
http://127.0.0.1:8000/admin/


# Team Project 
Text2Speech를 구현한 Django Project
Model : tacotron 사용

### Reference
* https://github.com/keithito/tacotron  
* https://github.com/carpedm20/multi-speaker-tacotron-tensorflow

### Dataset
* 영어 UK (남자) 
https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/   
* 영어 (여자) 
https://keithito.com/LJ-Speech-Dataset/
* 영어 남자
https://librivox.org/a-history-of-california-the-spanish-period-by-charles-edward-chapman/
* 한국어 여자
https://www.kaggle.com/bryanpark/korean-single-speaker-speech-dataset

### 

### Preprocess the data
python preprocess.py --dataset ljspeech

### Train a model
python train.py

### Monitor with Tensorboard
tensorboard --logdir ~/tacotron/logs-tacotron

### Evaluate 
python eval.py --checkpoint ~/tacotron/logs-tacotron/model.ckpt-185000

### Run a server
python manage.py runserver
