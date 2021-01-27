# pip 업그레이드하기 =>  /usr/bin/python3 -m pip install --upgrade pip
#  구글 번역 API 다운로드 하기 => pip3 install google_trans_new
# requests 패키지도 필요함
# 구글 번역 라이브러리는 Python >=3.6 에서 동작함

import os
from google_trans_new import google_translator # 문제가 좀 있음


filename = 'title.txt' # 유튜브 영상에서 다운받은 자막파일 이름
src_lang = 'ko'
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
  line = f.readline()
  translate_text = translator.translate(line,lang_src=src_lang, lang_tgt=tgt_lang)  
  print(translate_text)

  # 변경된 lines 배열을 다시 파일에 쓰기
  f = open(filename, "a" , encoding='UTF8')
  f.write('\n'+translate_text+ '('+ lang_codes[tgt_lang] +')' + '\n')
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