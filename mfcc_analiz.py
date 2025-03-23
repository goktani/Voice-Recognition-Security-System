import librosa
import numpy as np
import os

def mfcc_cikar(dosya):
    y, sr = librosa.load(dosya, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)

X = []
y = []

for dosya in os.listdir("temiz_veri"):
    mfcc_ozellikleri = mfcc_cikar(f"temiz_veri/{dosya}")
    X.append(mfcc_ozellikleri)
    if "admin" in dosya:
        y.append(1)
    else:
        y.append(0)

X = np.array(X)
y = np.array(y)

np.save("X.npy", X)
np.save("y.npy", y)
print("MFCC verileri kaydedildi.")
