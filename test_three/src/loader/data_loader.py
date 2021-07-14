import glob
import constant
import os
from path import *
from src.data_preprocessing.norm_text import *
from tqdm import tqdm

class DataLoader:

    def __init__(self):
        self.data_text = []
        self.data_class = []
        self.norm_app = NormText()

    def read_text(self, text_file):
        with open(text_file, "r", encoding="utf-16") as f:
            lines = f.readlines()
            lines = " ".join(lines)
            lines = self.norm_app.norm(lines)
        return lines

    def __load_data__(self, data_path=None, text_format="txt"):
        for folder_path in glob.glob(get_path(data_path + "/*")):
            for file_path in tqdm(glob.glob(get_path(folder_path + "/*." + text_format))):
                self.data_text.append(self.read_text(file_path))
                self.data_class.append(constant.classes[os.path.basename(folder_path)])
