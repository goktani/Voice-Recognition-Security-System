import pyaudio
import wave
import os

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # 16kHz örnekleme
CHUNK = 1024
RECORD_SECONDS = 3  # 3 saniyelik ses kaydı

if not os.path.exists("veri_seti"):
    os.makedirs("veri_seti")

def ses_kaydet(kisi, numara):
    dosya_adi = f"veri_seti/{kisi}_ses_{numara}.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

    print(f"Kayıt başlıyor: {dosya_adi} - Konuşmaya başla...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Kayıt tamamlandı.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(dosya_adi, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Admin için 30 kayıt al
for i in range(30):
    ses_kaydet("admin", i)

# Yetkisiz kişiler için 30 kayıt al
for i in range(30):
    ses_kaydet("yetkisiz", i)
