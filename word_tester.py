# -*- coding: utf-8 -*-
from gensim import corpora, models, similarities
from janome.tokenizer import Tokenizer
import numpy as np
import re
import json
from pprint import pprint
from tools.word_extractor import get_words_list
from tools.importer_saver import from_txt


class word:
    def __init__(self):
        self.t = Tokenizer()
        self.routine()

    # db/db.txtからjsonデータを取得し、ディクショナリ化する。
    def get_data(self):
        data = from_txt('./db', 'db.txt')
        data = json.loads(data)
        self.text_db['cookpad_search'] = data['food_name'] + data['ingredients']

    def get_db(self):# もっと簡単なものに。
        self.text_db = {'cookpad':'パスタを作りたい.パスタを食べたい.お腹が空いた.おいしいものが食べたい.今日のご飯何にしよう.料理を作りたい.弁当を作りたい.ピザを作りたい.ハンバーグを作りたい.辛い物が食べたい.甘いものが食べたい.塩分を取りたい.デザートを食べたい.簡単に作れるランチを知りたい.簡単なディナーを知りたい.お勧めの料理を知りたい.卵を使った料理を知りたい',
                        'youtube':'動画を観たい.youtube を使いたい.ドラマを観たい.面白い映像を観たい.映画を観たい.音楽が聞きたい.怖い動画を見たい.急上昇1位の動画を見たい.犬の動画を見たい.猫の動画を見たい.お勧めの動画.急上昇中の動画を教えてほしい.簡単に作れるご飯の動画が見たい.眠れる動画を見たい.面接の動画.簡単な料理の動画を見たい.美味しい料理の動画を見たい.コロナについて知りたい',
                        'study':'CCNAの勉強頑張ります.学校の勉強の仕方を知りたい.仕事で活躍する知識を身に付けたい.資格の勉強をする.基本情報試験の勉強を頑張る.音楽の勉強をしたい.免許を取りたい.英語を学びたい.ネットワークの知識を身に付けたい.セキュリティについて学びたい.アンドロイドアプリを作りたい.pythonを身に付けたい.Linuxの勉強をしたい.課題を終わらせたい'}   #listのlist

    def get_tokenized_db(self):
        self.texts = []# t.tokenize(text)の結果はlist
        self.theme = []
        for theme, text in self.text_db.items():
            self.texts.append(get_words_list(text))
            self.theme.append(theme)

    def get_dictionary(self):
        self.dictionary = corpora.Dictionary(self.texts)

    def get_feature_count(self):# tokenに何回ループしたかをカウントする。
        self.feature_cnt = len(self.dictionary.token2id)

    def get_corpus(self):# ベクトルを作る。
        self.corpus = [self.dictionary.doc2bow(text) for text in self.texts]

    def create_tfidf(self):
        self.tfidf = models.TfidfModel(self.corpus)

    def get_index(self):
        self.index =  similarities.SparseMatrixSimilarity(self.tfidf[self.corpus], num_features = self.feature_cnt)

    def get_keyword_vector(self, user_input):
        self.kw_vector = self.dictionary.doc2bow([token.surface for token in self.t.tokenize(user_input)])

    def get_similarity(self):
        return self.index[self.tfidf[self.kw_vector]]

    def routine(self):
        self.get_db()
        self.get_data()
        self.get_tokenized_db()
        self.get_dictionary()
        self.get_feature_count()
        self.get_corpus()
        self.create_tfidf()
        self.get_index()


if __name__ == '__main__':
    wd = word()

    def test():
        user_list_input = ['弁当を作りたい','料理を作りたい','音楽の動画が見たい','数学の勉強をする','怖い動画を見たい','料理の動画を見たい','料理の勉強をしたい',
        '面白い動画を見たい','料理の動画を見て勉強したい','数学の勉強をしたい','音楽の勉強がしたい','基本情報試験の動画を見る','基本情報試験の勉強をする','簡単に作れるご飯の動画を見たい','急上昇の動画','簡単に作れる料理の動画',
        'お勧めの動画','料理の勉強をした','デザートを食べたい','アプリを作成したい','英語を勉強したい','卵料理を作りたい','カルボナーラを食べたい','お腹がすいた','カレーの材料','お勧めの国を教えて','コロナについて知りたい',
        '子供が美味しく食べられる料理を知りたい','お年寄りでも食べれる料理','子供に勉強をさせる方法','安く済ませられる料理','クリスマス料理を知りたい','牛肉を使った料理','野菜がいっぱい取れる料理を知りたい','コロナ新規感染者',
        '作り置き出来る料理を知りたい','一人暮らし用の鍋がほしい','一人用サイズのすき焼きのグ材の量を知りたい','3日で約1000円に抑えられる1人暮らしの料理を知りたい','一人暮らし向けの料理を知りたい','近場のスーパーを教えてほしい',
        '安売りしているスーパーを知りたい','お勧めの小説','お勧めの漫画','面白い番組を知りたい','キューピー三分クッキングの動画を見たい','深い眠りにつく方法','HAL大阪に入学して学びたい','タイピングの練習をしたい','wordの使い方を知りたい',
        'Execlの表計算の勉強をしたい','勉強に適した環境を作りたい','睡眠不足を解消したい','おせちの具材を教えてほしい','おせちをアレンジしたい','1人用サイズのおせちの材料','キャベツの切り方を教えてほしい','1人で勉強する方法','子供が美味しく野菜を食べられる方法',
        '玉ねぎの皮のめくり方','500円以内で食べられる料理を教えてほしい','お勧めの音楽動画を知りたい','centOS7の使い方を知りたい','TwitterBOTを作りたい','自分のwebサイトを作成したい','参考になるwebサイトのデザインを教えてほしい']
        for user_input in user_list_input[:10]:
            wd.get_keyword_vector(user_input)
            similarity = wd.get_similarity()
            theme = {'cookpad': [], 'youtube': [], 'study': [], 'cookpad_search': []}
            # print(user_input)
            # print(wd.theme[np.argmax(similarity)])
            for i in range(len(similarity)):
                if 'を' in user_input:
                    current_user_input_keyword = [re.findall(r'(\S+)を', user_input)[0], user_input]
                else:
                    current_user_input_keyword = user_input

            print('----')
            for i in range(len(similarity)):
                print(f'{wd.theme[i]}:{similarity[i]}')

                if current_user_input_keyword not in theme[wd.theme[np.argmax(similarity)]]:
                    theme[wd.theme[np.argmax(similarity)]].append(current_user_input_keyword)
                
                    if wd.theme[np.argmax(similarity)] == 'cookpad':
                        print('question')
                        print(current_user_input_keyword)
                    elif wd.theme[np.argmax(similarity)] == 'cookpad_search':
                        print('search')
                        # user_inputから、探せるもの、質問が必要、もう一つ処理が必要に分ける
                        print(current_user_input_keyword)

                        """ 探せるもの """
                        """ 弁当 デザート 卵料理 牛肉 """

                        """ 質問が必要 """
                        """ 料理 お腹がすいた """
                        # どんな料理が作りたいか、何を食べたいか
                        # 探せるものに行く

                        """ もう一つ処理が必要 リストが必要"""
                        """ 子供が美味しく食べられる料理 お年寄りでも食べれる料理 安く済ませられる料理 作り置き出来る料理 一人暮らし用の鍋 1人用サイズのおせちの材料 子供が美味しく野菜 """
                        # 子供、お年寄り、作り置き、一人暮らし、一人用、お父さん、お母さん、恋人、彼氏、彼女、友達、子供、安い、高い
                        """ カレーの材料 クリスマス料理 野菜がいっぱい取れる料理 """
                        # バレンタインなど、特別な日に合わせた料理、食材名、カテゴリー名、商品名（どこでも使うリスト）
    test()
        # print()
        # pprint(theme)

"""https://www.moranbong.co.jp/recipe/?base_c=41&contents_type=47
anc_arrow"""
