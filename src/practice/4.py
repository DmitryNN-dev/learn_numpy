import numpy as np
import librosa

# Загрузка аудио файла
audio_file = "audio.mp3"
y, sr = librosa.load(audio_file)

# Преобразование аудио в массив numpy
audio_array = y

# Вывод информации о массиве
print(audio_array.shape)
print(audio_array)