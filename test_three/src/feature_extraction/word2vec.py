import constant
import numpy as np
from path import *
from gensim.models import KeyedVectors


class Word2Vec:

    def __init__(self):
        self.model = KeyedVectors.load_word2vec_format(get_path(constant.ROOT_DIR + "/Dictionary/baomoi.model.bin"), binary=True)
        self.word_index = self.model.key_to_index

    def convert_sentence_to_word2vec(self, sentence, max_length, embedding_dim):
        feature_sentence = np.zeros((embedding_dim, max_length))
        sentence_words = sentence.split()
        for i, word in enumerate(sentence_words):
            try:
                feature_sentence[:, i] = self.model[word][0:embedding_dim]
            except KeyError as e:
                continue
            except IndexError as e:
                continue
        feature_sentence = feature_sentence.reshape((1, feature_sentence.shape[0] * feature_sentence.shape[1]))
        return feature_sentence[0]




