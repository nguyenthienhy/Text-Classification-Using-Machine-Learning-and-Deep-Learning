
from src.loader.data_loader import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from src.model.bilstm import *
from src.utils.plot_loss import *
from sklearn.decomposition import TruncatedSVD
import constant
import numpy as np
import pickle

with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/X_train.pkl"), "rb") as f:
  X_train = pickle.load(f)
with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/y_train.pkl"), "rb") as f:
  y_train = pickle.load(f)

with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/X_test.pkl"), "rb") as f:
  X_test = pickle.load(f)
with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/y_test.pkl"), "rb") as f:
  y_test = pickle.load(f)
with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/svd.pkl"), "rb") as f:
  svd = pickle.load(f)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# svd = TruncatedSVD(n_components=300, random_state=42)
# svd.fit(X_train)

# X_train = svd.transform(X_train)
# X_test = svd.transform(X_test)

# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/X_train.pkl"), "wb") as f:
#   pickle.dump(X_train, f)
# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/y_train.pkl"), "wb") as f:
#   pickle.dump(y_train, f)

# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/X_test.pkl"), "wb") as f:
#   pickle.dump(X_test, f)
# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/y_test.pkl"), "wb") as f:
#   pickle.dump(y_test, f)

# with open(get_path(constant.ROOT_DIR + "/Data_feature/LSTM/svd.pkl"), "wb") as f:
#   pickle.dump(svd, f)

model = BiLSTM(X_train[0].shape)

opt = Adam()
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=opt,
    metrics=['accuracy'],
)

checkpoint_cb = ModelCheckpoint(
        constant.ROOT_DIR + '/save_model/weights.{epoch:02d}-{val_loss:.2f}.h5',
        save_weights_only=True, period=1)

history = model.fit(x=X_train,
                    y=y_train,
                    batch_size=constant.BATCH_SIZE,
                    epochs=constant.NUM_EPOCHS,
                    callbacks=[checkpoint_cb],
                    validation_data=(X_test, y_test))

plot_loss_train_val(history)
