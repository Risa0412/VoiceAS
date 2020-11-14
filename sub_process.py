import random
import datetime
import time
import re
import os
import webbrowser
import subprocess
import argparse
from time import strftime
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from word_extractor import get_words_list

import speech_recognition as sr
import pyttsx3

def get_name():
    _name = ""
    if os.path.exists('name.txt'):
        file = open("name.txt","r")
        _name = file.read()
        file.close()

    return _name

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 115)
engine.setProperty('volume', 0.9)


def myCommand():
    # "listens for commands"
    r = sr.Recognizer()# Recognizerはライブラリ
    # engine.runAndWait()

    with sr.Microphone() as source:# 音(source)はマイクロフォンから取ってくる。
        r.pause_threshold = 0.5# 音を取った後、カットする。
        r.adjust_for_ambient_noise(source, duration=1)# ノイズを取り除く。
        audio = r.listen(source)# 綺麗になった音がaudioになる。

    try:
        command = r.recognize_google(audio, language='ja-JP')# このaudioはどんな言語か。

    except sr.UnknownValueError:# 音を拾ったけど言語ではないとき。
        print('....')
        command = myCommand()
    print(type(command), command)
    return command
    
def assistant(command):
    if 'そこまで' in command:
        engine.say(f'さようなら、{name}')
        engine.runAndWait()
        exit()

    elif "私の名前は" in command:
        reg_ex = re.search("私の名前は(.+)", command)
        if reg_ex:
            callname = reg_ex.group(1)
            file = open("name.txt","w+")
            file.write(callname)
            file.close()
            engine.say(f"{callname}で呼びます。")

    elif '時間' in command:
        # print(type(command), command)
        now = datetime.datetime.now()
        # aana.get_single_audio(f'現在の時間は{now.hour}時{now.minute}分です。')
        engine.say(f'現在の時間は{now.hour}時{now.minute}分です。')
        print(f'現在の時間は{now.hour}時{now.minute}分です。')
        

    elif '画像' in command:
        reg_ex = re.search('(.*)画像', command)
        url = 'https://www.google.co.jp/'
        if reg_ex:
            subsearch = reg_ex.group(1)
            url += f'search?tbm=isch&source=hp&ei=yW9cXqOsBeytmAWK06PgBg&q={subsearch}&oq={subsearch}'
            webbrowser.open(url)
            # aana.get_single_audio(f'{subsearch}画像を探しました。')
            engine.say(f'{subsearch}画像を探しました。')

    # elif 'の作り方' in command:
    elif re.match(r'\S+の\S+方', command.replace(' ', '')):
        print( get_words_list(command))
        site_name, subsearch, order = get_words_list(command)
        site_dic = {'クックパッド': 'https://cookpad.com/search/', 'youtube': 'https://www.youtube.com/results?search_query='}# key:サイト名 value:サイトURL
        url = 'https://www.google.co.jp/'
        for kwords, urls in site_dic.items():# site_dicのkey, valueをペアで取得。
            if site_name in kwords:# reg_ex[0]の含まれるkeyから命令を出す。
                url = urls# kwordsのurlsが代入される。
        if site_name:
            if 'https://www.google.co.jp/' in url:
                url += f'search?sxsrf=ALeKk01uAOvlPejHN4lH97ttu805Q_WuLw%3A1603514862906&ei=7rGTX6DxNsz7-QbG_4Bo&q=site%3A+{site_name}+{subsearch}&oq=site%3A+{site_name}+{subsearch}'
            else:
                url += f'{subsearch}'
            webbrowser.open(url)
            engine.say(f'{subsearch}の{order}を探しました。')
            # aana.get_single_audio(f'{subsearch}を探しました。')

    elif 'クックパッド' in command:
        reg_ex = re.search('クックパッド(.*)', command)
        reg_ex = re.search('で(.*)', reg_ex.group(1))
        subsearch = reg_ex.group(1)
        if subsearch:
            url = f'https://cookpad.com/search/{subsearch}'
            webbrowser.open(url)
            # aana.get_single_audio(f'{subsearch}画像を探しました。')
            engine.say(f'{subsearch}を探しました。')
    engine.runAndWait()
if __name__ == '__main__':
    while True:
        name = get_name()
        if name == '':
            engine.say('お名前はなんですか？')
        # else:
        #     engine.say(f'おはよう、{name}たん')
        #     print(f'話してください...')
        assistant(myCommand())
        

"""
2020/10/10
次回：ディクショナリの中にURLが入っていない場合。
2020/10/24
次回：DB/TEXTに前の命令を保存する
"""
