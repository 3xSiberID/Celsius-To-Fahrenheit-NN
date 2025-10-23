import numpy as np
from tensorflow.keras.models import load_model

model = load_model('model_suhu.keras')
print("✅ Model berhasil dimuat dari 'model_suhu.keras'")

user_input = input("Masukkan suhu dalam Celsius (pisahkan dengan koma, contoh: 100,37,-20): ")

try:
    celsius_input = np.array([float(x.strip()) for x in user_input.split(',')])
except ValueError:
    print("❌ Input tidak valid. Pastikan hanya memasukkan angka yang dipisahkan koma.")
    exit()

predictions = model.predict(celsius_input)

print("\nPrediksi suhu:")
for c, f in zip(celsius_input, predictions):
    print(f"{c}°C -> {f[0]:.2f}°F")
