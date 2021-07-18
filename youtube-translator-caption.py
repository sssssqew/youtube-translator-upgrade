# pip 업그레이드하기 =>  /usr/bin/python3 -m pip install --upgrade pip
#  구글 번역 API 다운로드 하기 => pip3 install google_trans_new
# requests 패키지도 필요함
# 구글 번역 라이브러리는 Python >=3.6 에서 동작함

# 주의사항 : 캡션을 달때는 무조건 한줄로 작성하기 => 아니면 캡션 다운로드한 다음에 한줄로 변경하기

# 파이썬 버전을 업그레이드하면 google_trans_new 를 인식 못할수 있음 => 커맨드창에서 파이썬 버전을 변경해줘야함 py -3.91 youtube-translator-caption.py
# 파이썬 3.9.1에서는 모듈을 인식하지만 3.9.6에서는 인식하지 못함

# json.decoder.JSONDecodeError: Extra data 
# C:\Users\이성용\AppData\Local\Programs\Python\Python39\Lib\site-packages\google_trans_new 폴더 내에 google_trans_new.py 151 행 코드 변경하기
# (decoded_line + ']') 를 decoded_line 으로 변경하기

import os
from google_trans_new import google_translator # 문제가 좀 있음

# directory_to_save_captions = '/home/sylee/dev/utility/youtube-translator/captions/' # 자막을 저장할 폴더 위치 => PC마다 변경해줘야 함
directory_to_save_captions = 'C:\youtube-translator\\captions\\'

# 자막 파일들을 담을 폴더 생성하기
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
createFolder(directory_to_save_captions)


filename = 'captions.srt' # 유튜브 영상에서 다운받은 자막파일 이름
src_lang = 'en'
tgt_lang_array = ['en', 'zh-cn', 'zh-tw', 'hi', 'ru',
                             'ja', 'de', 'th', 'id', 'ms', 'vi', 'tl',
                             'fi', 'fr', 'pl',  'pt', 'es', 'tr', 'it',
                             'uk', 'da', 'no', 'nl', 'sv', 'he'
                             ]

lang_codes = {
    'en' : '영어',
    'zh-cn': '중국어(간체)',
    'zh-tw' : '중국어(번체)',
    'hi' :  '힌디어',
    'ru': '러시아어',
    'ja' : 	'일본어',
    'de': '독일어',
    'th': '태국어',
    'id' : '인도네시아어',
    'ms': '말레이어',
    'vi' : '베트남어',
    'tl' : '필리핀어',
    'fi' : '핀란드어',
    'fr': '프랑스어',
    'pl': '폴란드어',
    'pt': '포르투칼어',
    'es': '스페인어',
    'tr': '터키어',
    'it': '이탈리아어',
    'uk': '우크라이나어',
    'da' : 	'덴마크어',
    'no': '노르웨이어',
    'nl': '네덜란드어',
    'sv': '스웨던어',
    'he': '히브리어'
}

translator = google_translator()  

def translate_and_save_into_file(filename, tgt_lang):
  #  파일 전체 읽어서 lines 배열에 저장하기
  f = open(filename, "r" , encoding='UTF8')
  lines = f.readlines()

  # 라인마다 순회하면서 한글이 있는 줄만 번역한 다음 lines 배열에 업데이트하기
  for i, line in enumerate(lines):
    if (i-2) % 4 == 0: 
      # print(lines[i])
      translate_text = translator.translate(lines[i],lang_src=src_lang, lang_tgt=tgt_lang)  
      print(translate_text)
      lines[i] = translate_text + "\n" # 원래 다운로드한 자막파일에 자막마다 한줄 띄워쓰기가 있어서 반드시 "\n"  있어야 함

  # 변경된 lines 배열을 다시 파일에 쓰기
  f = open("{}captions_{}.srt".format(directory_to_save_captions, lang_codes[tgt_lang]), "w", encoding='UTF8')
  f.writelines(lines)
  f.close()

# 번역할 언어 갯수만큼 순회하면서 번역하고 파일 저장함
for i in range(len(tgt_lang_array)):
  translate_and_save_into_file(filename, tgt_lang_array[i])
  print("---------------------------------------------------------------")



# google trans new 코드 ########################
############### 변경할 언어 코드 ################
# 영어 : en
# 중국어(간체): zh-cn
# 중국어(번체) : zh-tw
# 힌디어 :  hi
# 러시아어: ru
# 일본어 : 	ja
# 독일어: de
# 태국어: th
# 인도네시아어 : id
# 말레이어: ms
# 베트남어 : vi
# 필리핀어 : tl
# 핀란드어 : fi
# 프랑스어: fr
# 폴란드어: pl
# 포르투칼어: pt
# 스페인어: es
# 터키어: tr
# 이탈리아어: it
# 우크라이나어: uk
# 덴마크어 : 	da
# 노르웨이어: no
# 네덜란드어: nl
# 스웨던어: sv
# 히브리어: he
############################################