import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Veriyi yükle
X = np.load("X.npy")
y = np.load("y.npy")

# Ensure labels are floats in the range [0, 1]
y = y.astype(np.float32)

# Eğitim ve test verisi olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Sigmoid for binary classification
])

# Modeli derle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğit
history = model.fit(X_train, y_train, epochs=50, batch_size=8, validation_data=(X_test, y_test))

# Modeli kaydet
model.save("ses_tanima_modeli.h5")
print("Model eğitildi ve kaydedildi.")