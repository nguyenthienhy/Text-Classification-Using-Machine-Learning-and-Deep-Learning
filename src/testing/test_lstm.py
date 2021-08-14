from silence_tensorflow import silence_tensorflow
silence_tensorflow()
from src.model.bilstm import *
from src.data_preprocessing.norm_text import *
from src.utils.plot_metric import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import confusion_matrix, classification_report
import pickle
import constant
import numpy as np
from path import *
from tensorflow.keras.optimizers import *

norm_app = NormText()

# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/X_train.pkl"), "rb") as f:
#   X_train = pickle.load(f)
# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/y_train.pkl"), "rb") as f:
#   y_train = pickle.load(f)

# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/X_test.pkl"), "rb") as f:
#   X_test = pickle.load(f)
# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/y_test.pkl"), "rb") as f:
#   y_test = pickle.load(f)

with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/svd.pkl"), "rb") as f:
  svd = pickle.load(f)

with open(get_path(constant.ROOT_DIR + "/Data_feature/RANDOM_FOREST/feature_extractor.pkl"), "rb") as f:
  feature_extractor = pickle.load(f)

model = BiLSTM((300,))
opt = Adam(learning_rate=0.001)
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=opt,
    metrics=['accuracy'],
)
model.load_weights(get_path(constant.ROOT_DIR + '/save_model/lstm.h5'))
# model.evaluate(X_test, y_test)

# y_pred = []
# for i, sample in enumerate(X_test):
#     sample = np.expand_dims(sample, axis=0).astype(np.float32)
#     pred = model.predict(sample)
#     label = np.argmax(pred)
#     y_pred.append(label)

# print(classification_report(y_test, y_pred, target_names=constant.target_names))
# cm = confusion_matrix(y_test, y_pred)
# plot_confusion_matrix(cm, target_names=constant.target_names)

def predict_category():
    f = open(get_path(constant.ROOT_DIR + "/Test_files/test.txt"), "r", encoding="utf-8")
    lines = f.readlines()
    new_lines = ""
    for line in lines:
        new_lines += new_lines + " " + norm_app.norm(line)
    sample = svd.transform(feature_extractor.transform([new_lines]))
    pred = model.predict(sample)
    print("Chủ đề của đoạn văn: " + constant.target_names[np.argmax(pred)])
    print("Độ tin cậy: " + str(np.max(pred)))

predict_category()