import pyttsx3

engine = pyttsx3.init()# ライブラリを使うためにvariableをinit()。ここにオブジェクトが入る。
voices = engine.getProperty('voices')# どんなwindowsのvoiceを使うか決める。

# windowsにどんなvoiceがあるか調べる。
def get_voice_list():
    for voice in voices:
        print("Voice: %s" % voice.name)
        print(" - ID: %s" % voice.id)
        print(" - Languages: %s" % voice.languages)
        print("\n")

engine.setProperty("voice", voices[0].id)# windowsのvoiceの選択。setProperty(ライブラリのパラメータ名, 選択したパラメータのID)
engine.setProperty('rate', 50)# voiceのスピード。数が大きいと速い。
engine.setProperty('volume', 0.9)# voiceの大きさ。なくてもよい。
engine.say(f'の天気は。最高温度は24と最低温度は23です。')# voiceが何を言うか。
engine.runAndWait()