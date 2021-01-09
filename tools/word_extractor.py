# -*- coding: utf-8 -*-
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
from janome.tokenizer import Tokenizer


# word_kindに結合したい単語の種類（名詞、動詞など）をペアで('名詞','動詞')の形で入れる。
# word_kindに応じて文章から抜き出した単語動詞を結合して一つの単語にする。
def word_assembler(word_part_of_speech, token, result_list, word_kind):
    if word_kind[0] in word_part_of_speech[0] and word_kind[1] in token.part_of_speech:
        try:
            past_index = result_list.index(word_part_of_speech[1])
            result_list[past_index] = f"{word_part_of_speech[1]}{token.surface}"
            result_list.pop(past_index + 1)
        except:
            pass


def get_words_list(sentence):
    """
    文中の名詞を抽出する。
    :param sentence: string
    :return: list of string
    """
    result_list = []

    char_filters = [UnicodeNormalizeCharFilter(),
                    RegexReplaceCharFilter('<.*?>', '')]

    token_filters = [POSKeepFilter(['名詞', '動詞', '助動詞']), LowerCaseFilter(), ExtractAttributeFilter('surface')]# 名詞のみを抽出。

    a = Analyzer(char_filters=char_filters, token_filters=token_filters)

    sentence = sentence.replace('.', '')
    for token in a.analyze(sentence):
        result_list.append(token)

    stop_words = ["あそこ","あっ","あの","あのかた","あの人","あり","あります","ある","あれ","い","いう","います","いる","う","うち","え","お","および","おり","おります","か","かつて","から","が","き","ここ","こちら","こと","この","これ","これら","さ","さらに","し","しかし","する","ず","せ","せる","そこ","そして","その","その他","その後","それ","それぞれ","それで","た","ただし","たち","ため","たり","だ","だっ","だれ","つ","て","で","でき","できる","です","では","でも","と","という","といった","とき","ところ","として","とともに","とも","と共に","どこ","どの","な","ない","なお","なかっ","ながら","なく","なっ","など","なに","なら","なり","なる","なん","に","において","における","について","にて","によって","により","による","に対して","に対する","に関する","の","ので","のみ","は","ば","へ","ほか","ほとんど","ほど","ます","また","または","まで","も","もの","ものの","や","よう","より","ら","られ","られる","れ","れる","を","ん","何","及び","彼","彼女","我々","特に","私","私達","貴方","貴方方"]
    for word in stop_words: 
        if word in result_list:
            result_list.remove(word)
        # sentence = sentence.replace(word, '')
    t = Tokenizer()

    # create the ist of tuple
    word_part_of_speech = [('', '')]
    word_kinds = [('名詞', '名詞'), ('動詞', '助動詞')]# word_assembler()で引数になる単語の種類のリストを作成する。
    # iterate over the tokenize sentence and search for 2 'meishi' who would be following each other
    for token in t.tokenize(sentence):
        for word_kind in word_kinds:# word_kindsの要素数だけword_assemler()を実行する。
            word_assembler(word_part_of_speech, token, result_list, word_kind)# 単語の結合
        word_part_of_speech = (token.part_of_speech, token.surface)# word_kindsの条件で結合された単語を含むリスト

    return result_list




# usage--このファイルの使い方--
"""
USAGE

s = 'youtubeでカメラの作り方'
words_list = get_words_list(s)
words_list = ["youtube", "カメラ", "作り方"]

"""
# s = 'クックパッドでカメラの作り方'
# get_words_list(s)

if __name__ == '__main__':
    s = 'youtubeでカメラの作りたい'
    words_list = get_words_list(s)
    print(words_list)
    s = 'クックパッドでパスタの作り方'
    words_list = get_words_list(s)
    print(words_list)
    