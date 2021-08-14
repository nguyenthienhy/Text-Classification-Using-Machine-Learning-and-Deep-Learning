import pickle
from path import *
from src.data_preprocessing.norm_text import *
import constant

norm_app = NormText()

with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/feature_extractor.pkl"), "rb") as f:
  feature_extractor = pickle.load(f)

with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/feature_selector.pkl"), "rb") as f:
  feature_selector = pickle.load(f)

with open(get_path(constant.ROOT_DIR + "/save_model/random_forest.pkl"), "rb") as f:
  model = pickle.load(f)

def predict_category():
    f = open(get_path(constant.ROOT_DIR + "/Test_files/test.txt"), "r", encoding="utf-8")
    lines = f.readlines()
    new_lines = ""
    for line in lines:
        new_lines += new_lines + " " + norm_app.norm(line)
    pred = model.predict(feature_selector.transform(feature_extractor.transform([new_lines])))
    print("Chủ đề của đoạn văn: " + constant.target_names[pred[0]])

predict_category()