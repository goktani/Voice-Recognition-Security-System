import librosa
import numpy as np
import scipy.signal
import soundfile as sf
import os

def temizle_ve_kaydet(input_dosya, output_dosya):
    y, sr = librosa.load(input_dosya, sr=16000)
    
    # Gürültü azaltma (High-pass filter)
    y = scipy.signal.savgol_filter(y, 11, 2)

    # Ses dosyasını tekrar kaydet
    sf.write(output_dosya, y, sr)

if not os.path.exists("temiz_veri"):
    os.makedirs("temiz_veri")

for dosya in os.listdir("veri_seti"):
    temizle_ve_kaydet(f"veri_seti/{dosya}", f"temiz_veri/{dosya}")