import constant
from path import *
from pyvi import ViTokenizer

class NormText:
    def __init__(self):
        with open(get_path(constant.ROOT_DIR + '/Dictionary/specialchar.txt'), 'r', encoding='utf-8') as r:
            self.list_char_cant_read = r.read().split()
        with open(get_path(constant.ROOT_DIR + '/Dictionary/stopwords.txt'), 'r', encoding='utf-8') as r:
            self.stop_words = r.read().split()
        self.stop_words = [ViTokenizer.tokenize(word) for word in self.stop_words]
        self.replace_list = {
            'òa': 'oà', 'óa': 'oá', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'òe': 'oè', 'óe': 'oé','ỏe': 'oẻ',
            'õe': 'oẽ', 'ọe': 'oẹ', 'ùy': 'uỳ', 'úy': 'uý', 'ủy': 'uỷ', 'ũy': 'uỹ','ụy': 'uỵ', 'uả': 'ủa',
            'ả': 'ả', 'ố': 'ố', 'u´': 'ố','ỗ': 'ỗ', 'ồ': 'ồ', 'ổ': 'ổ', 'ấ': 'ấ', 'ẫ': 'ẫ', 'ẩ': 'ẩ',
            'ầ': 'ầ', 'ỏ': 'ỏ', 'ề': 'ề','ễ': 'ễ', 'ắ': 'ắ', 'ủ': 'ủ', 'ế': 'ế', 'ở': 'ở', 'ỉ': 'ỉ',
            'ẻ': 'ẻ','aˋ': 'à', 'iˋ': 'ì', 'ă´': 'ắ','ử': 'ử', 'e˜': 'ẽ', 'y˜': 'ỹ', 'a´': 'á'
        }

    def norm(self, sentence):
        sentence = ' '.join(sentence.split())
        sentence = self.clean_unicode_encode_word(sentence)
        sentence = self.convert_to_lower(sentence)
        sentence = self.remove_special_chars(sentence)
        sentence = self.norm_type_accents(sentence)
        sentence = ViTokenizer.tokenize(sentence)
        return ' '.join(sentence.split())

    def convert_to_lower(self, text):
        return text.lower()
    
    def remove_special_chars(self, text):
        for i in self.list_char_cant_read:
            text = text.replace(i, " ")
        return text
    
    def remove_stop_words(self, text):
        for word in self.stop_words:
            if word in text.split():
                text = text.replace(word, " ")
        return text

    def norm_type_accents(self, sentence):
        for k, v in self.replace_list.items():
            sentence = sentence.replace(k, v)
        return sentence

    def clean_unicode_encode_word(self, text):
        enc_word = str(text).encode("unicode_escape")
        clean_enc_word = self.compound_unicode(enc_word)
        return clean_enc_word.decode("unicode_escape")

    def compound_unicode(self, unicode_str):
        unicode_str = unicode_str.replace(b"e\\u0309", b"\\u1EBB")  # ẻ
        unicode_str = unicode_str.replace(b"e\\u0301", b"\\u00E9")  # é
        unicode_str = unicode_str.replace(b"e\\u0300", b"\\u00E8")  # è
        unicode_str = unicode_str.replace(b"e\\u0323", b"\\u1EB9")  # ẹ
        unicode_str = unicode_str.replace(b"e\\u0303", b"\\u1EBD")  # ẽ
        unicode_str = unicode_str.replace(b"\\xea\\u0309", b"\\u1EC3")  # ể
        unicode_str = unicode_str.replace(b"\\xea\\u0301", b"\\u1EBF")  # ế
        unicode_str = unicode_str.replace(b"\\xea\\u0300", b"\\u1EC1")  # ề
        unicode_str = unicode_str.replace(b"\\xea\\u0323", b"\\u1EC7")  # ệ
        unicode_str = unicode_str.replace(b"\\xea\\u0303", b"\\u1EC5")  # ễ
        unicode_str = unicode_str.replace(b"y\\u0309", b"\\u1EF7")  # ỷ
        unicode_str = unicode_str.replace(b"y\\u0301", b"\\u00FD")  # ý
        unicode_str = unicode_str.replace(b"y\\u0300", b"\\u1EF3")  # ỳ
        unicode_str = unicode_str.replace(b"y\\u0323", b"\\u1EF5")  # ỵ
        unicode_str = unicode_str.replace(b"y\\u0303", b"\\u1EF9")  # ỹ
        unicode_str = unicode_str.replace(b"u\\u0309", b"\\u1EE7")  # ủ
        unicode_str = unicode_str.replace(b"u\\u0301", b"\\u00FA")  # ú
        unicode_str = unicode_str.replace(b"u\\u0300", b"\\u00F9")  # ù
        unicode_str = unicode_str.replace(b"u\\u0323", b"\\u1EE5")  # ụ
        unicode_str = unicode_str.replace(b"u\\u0303", b"\\u0169")  # ũ
        unicode_str = unicode_str.replace(b"\\u01b0\\u0309", b"\\u1EED")  # ử
        unicode_str = unicode_str.replace(b"\\u01b0\\u0301", b"\\u1EE9")  # ứ
        unicode_str = unicode_str.replace(b"\\u01b0\\u0300", b"\\u1EEB")  # ừ
        unicode_str = unicode_str.replace(b"\\u01b0\\u0323", b"\\u1EF1")  # ự
        unicode_str = unicode_str.replace(b"\\u01b0\\u0303", b"\\u1EEF")  # ữ
        unicode_str = unicode_str.replace(b"i\\u0309", b"\\u1EC9")  # ỉ
        unicode_str = unicode_str.replace(b"i\\u0301", b"\\u00ED")  # í
        unicode_str = unicode_str.replace(b"i\\u0300", b"\\u00EC")  # ì
        unicode_str = unicode_str.replace(b"i\\u0323", b"\\u1ECB")  # ị
        unicode_str = unicode_str.replace(b"i\\u0303", b"\\u0129")  # ĩ
        unicode_str = unicode_str.replace(b"o\\u0309", b"\\u1ECF")  # ỏ
        unicode_str = unicode_str.replace(b"o\\u0301", b"\\u00F3")  # ó
        unicode_str = unicode_str.replace(b"o\\u0300", b"\\u00F2")  # ò
        unicode_str = unicode_str.replace(b"o\\u0323", b"\\u1ECD")  # ọ
        unicode_str = unicode_str.replace(b"o\\u0303", b"\\u00F5")  # õ
        unicode_str = unicode_str.replace(b"\\u01a1\\u0309", b"\\u1EDF")  # ở
        unicode_str = unicode_str.replace(b"\\u01a1\\u0301", b"\\u1EDB")  # ớ
        unicode_str = unicode_str.replace(b"\\u01a1\\u0300", b"\\u1EDD")  # ờ
        unicode_str = unicode_str.replace(b"\\u01a1\\u0323", b"\\u1EE3")  # ợ
        unicode_str = unicode_str.replace(b"\\u01a1\\u0303", b"\\u1EE1")  # ỡ
        unicode_str = unicode_str.replace(b"\\xf4\\u0309", b"\\u1ED5")  # ổ
        unicode_str = unicode_str.replace(b"\\xf4\\u0301", b"\\u1ED1")  # ố
        unicode_str = unicode_str.replace(b"\\xf4\\u0300", b"\\u1ED3")  # ồ
        unicode_str = unicode_str.replace(b"\\xf4\\u0323", b"\\u1ED9")  # ộ
        unicode_str = unicode_str.replace(b"\\xf4\\u0303", b"\\u1ED7")  # ỗ
        unicode_str = unicode_str.replace(b"a\\u0309", b"\\u1EA3")  # ả
        unicode_str = unicode_str.replace(b"a\\u0301", b"\\u00E1")  # á
        unicode_str = unicode_str.replace(b"a\\u0300", b"\\u00E0")  # à
        unicode_str = unicode_str.replace(b"a\\u0323", b"\\u1EA1")  # ạ
        unicode_str = unicode_str.replace(b"a\\u0303", b"\\u00E3")  # ã
        unicode_str = unicode_str.replace(b"\\u0103\\u0309", b"\\u1EB3")  # ẳ
        unicode_str = unicode_str.replace(b"\\u0103\\u0301", b"\\u1EAF")  # ắ
        unicode_str = unicode_str.replace(b"\\u0103\\u0300", b"\\u1EB1")  # ằ
        unicode_str = unicode_str.replace(b"\\u0103\\u0323", b"\\u1EB7")  # ặ
        unicode_str = unicode_str.replace(b"\\u0103\\u0303", b"\\u1EB5")  # ẵ
        unicode_str = unicode_str.replace(b"\\xe2\\u0309", b"\\u1EA9")  # ẩ
        unicode_str = unicode_str.replace(b"\\xe2\\u0301", b"\\u1EA5")  # ấ
        unicode_str = unicode_str.replace(b"\\xe2\\u0300", b"\\u1EA7")  # ầ
        unicode_str = unicode_str.replace(b"\\xe2\\u0323", b"\\u1EAD")  # ậ
        unicode_str = unicode_str.replace(b"\\xe2\\u0303", b"\\u1EAB")  # ẫ
        unicode_str = unicode_str.replace(b"\\u202d", b"")
        unicode_str = unicode_str.replace(b"\\u202c", b"")
        return unicode_str
