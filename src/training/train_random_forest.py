from src.loader.data_loader import *
from src.model.random_forest import *
from sklearn.feature_extraction.text import *
from sklearn.feature_selection import *
import pickle

# train_loader = DataLoader()

# train_loader.__load_data__(get_path(constant.ROOT_DIR + "/Dataset/train"))

# test_loader = DataLoader()

# test_loader.__load_data__(get_path(constant.ROOT_DIR + "/Dataset/test"))

# feature_extractor = TfidfVectorizer(ngram_range=(1, 2))
# feature_train = feature_extractor.fit_transform(train_loader.data_text)
# feature_test = feature_extractor.transform(test_loader.data_text)

# print(feature_train.shape)

# X_train = feature_train
# y_train = train_loader.data_class
# X_test = feature_test
# y_test = test_loader.data_class

# with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/X_train.pkl"), "wb") as f:
#   pickle.dump(X_train, f)
# with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/y_train.pkl"), "wb") as f:
#   pickle.dump(y_train, f)

# with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/X_test.pkl"), "wb") as f:
#   pickle.dump(X_test, f)
# with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/y_test.pkl"), "wb") as f:
#   pickle.dump(y_test, f)

# with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/feature_extractor.pkl"), "wb") as f:
#   pickle.dump(feature_extractor, f)

  
with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/X_train.pkl"), "rb") as f:
  X_train = pickle.load(f)
with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/y_train.pkl"), "rb") as f:
  y_train = pickle.load(f)

with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/X_test.pkl"), "rb") as f:
  X_test = pickle.load(f)
with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/y_test.pkl"), "rb") as f:
  y_test = pickle.load(f)

feature_selector = SelectKBest(chi2, k=25000)
X_train = feature_selector.fit_transform(X_train, y_train)
X_test = feature_selector.transform(X_test)

with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/feature_selector.pkl"), "wb") as f:
  pickle.dump(feature_selector, f)

train_app = Random_Forest()
train_app.fit(X_train, y_train)
print(train_app.evaluate(X_test, y_test))
with open(get_path(constant.ROOT_DIR + "/save_model/random_forest.pkl"), "wb") as f:
  pickle.dump(train_app.model, f)
train_app.get_confusion_matrix(X_test, y_test)