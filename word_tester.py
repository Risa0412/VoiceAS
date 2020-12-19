from gensim import corpora, models, similarities
from janome.tokenizer import Tokenizer


class word:
    def __init__(self):
        self.t = Tokenizer()
        self.routine()

    def get_db(self):# もっと簡単なものに。
        self.text_db = {'cookpad':'パスタを作りたい.パスタを食べたい.お腹が空いた.おいしいものが食べたい.今日のご飯何にしよう.料理を作りたい', 'youtube':'動画を観たい.youtube を使いたい.ドラマを観たい.面白い映像を観たい.映画を観たい', 'study':'CCNAの勉強頑張ります.学校の勉強の仕方を知りたい.仕事で活躍する知識を身に付けたい.資格の勉強をする'}# listのlist
        # self.text_dbの語群に似ているlistを作る。（後でsimilarityを計算。どれだけ文章が似ているか。）
        # self.theme_num = []
        # for n in self.text_db.keys():
        #     self.theme_num.append(n)

    def get_tokenized_db(self):
        self.texts = []# t.tokenize(text)の結果はlist
        self.theme = []
        for theme, text in self.text_db.items():
            self.texts.append([te.surface for te in self.t.tokenize(text)])
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
        self.get_tokenized_db()
        self.get_dictionary()
        self.get_feature_count()
        self.get_corpus()
        self.create_tfidf()
        self.get_index()


if __name__ == '__main__':
    wd = word()
    user_input = input('文章を入力してください\n')
    wd.get_keyword_vector(user_input)
    similarity = wd.get_similarity()
    #theme = ['cookpad', 'youtube', 'study']
    for i in range(len(similarity)):
        print(f'{wd.theme[i]}:{similarity[i]}')
