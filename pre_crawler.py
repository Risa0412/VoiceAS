# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import quote


# URLに対して、呼び出し、URLに漢字・カタカナが含まれている場合の呼び出し、レスポンスの読み込みと、読み込みHTMLをUTF-8でのデコードを行う。
# 結果はデコードされたURLと、URLのページ
class WebCrawler:
    # agent＝どんなブラウザを使って実行するか
    def __init__(self, url, agent='Mozilla/5.0', decoder='utf-8', parser='html.parser'):
        self.url = url
        # urlの呼び出し
        self.request = Request(self.url, headers={'User-Agent': agent})
        try:
            # URLの読み込み
            self.response = urlopen(self.request).read()
        except UnicodeEncodeError:
            # 漢字・カタカナのときの処理
            tmp_url = url.split('/')  # get url and split
            begin = '/'.join(tmp_url[:-1])  # join url until the last part
            end = quote(tmp_url[-1])  # quote the kanji part
            self.url = begin + '/' + end  # reform url
            self.response = urlopen(self.url).read()

        # BeautifulSoup()はUTF-8でデコード。parserはHTML型。
        self.soup = BeautifulSoup(self.response.decode(decoder), parser)
    
    # BeautifulSoupのsetter
    def get_soup(self):
        return self.soup
