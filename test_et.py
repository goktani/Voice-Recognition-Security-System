import pyaudio
import wave
import librosa
import numpy as np
import tensorflow as tf

# Modeli yükle
model = tf.keras.models.load_model("ses_tanima_modeli.h5")

# Ses kaydetme ayarları
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # 16kHz örnekleme hızı
CHUNK = 1024
RECORD_SECONDS = 3
OUTPUT_FILENAME = "test_sesi.wav"

def ses_kaydet():
    """Mikrofondan 3 saniyelik ses kaydeder ve test_sesi.wav olarak kaydeder."""
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

    print("🎤 Konuşmaya başla! (3 saniye boyunca)")
    frames = []
    
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("✅ Kayıt tamamlandı!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def test_et(dosya):
    """Ses dosyasını yükler, MFCC özelliklerini çıkarır ve modeli kullanarak tahmin yapar."""
    y, sr = librosa.load(dosya, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc = np.mean(mfcc, axis=1).reshape(1, -1)  # Model girişine uygun hale getir
    
    tahmin = model.predict(mfcc)

    if tahmin >= 0.3:
        print("✅ Admin sesi tanındı, kutu açılıyor!")
    else:
        print("❌ Yetkisiz kişi, erişim engellendi!")

# 1️⃣ Önce sesi kaydet
ses_kaydet()

# 2️⃣ Ardından kaydedilen sesi test et
test_et(OUTPUT_FILENAME)
