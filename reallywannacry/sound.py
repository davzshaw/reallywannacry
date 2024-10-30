import sounddevice as sd
from scipy.io.wavfile import write

# Parámetros de grabación
duracion = 10  # Duración de la grabación en segundos
frecuencia_muestreo = 44100  # Frecuencia de muestreo en Hz

print("Grabando...")

# Graba el audio desde el micrófono
audio = sd.rec(int(duracion * frecuencia_muestreo), samplerate=frecuencia_muestreo, channels=2)
sd.wait()  # Espera a que termie la grabación

# Guarda el archivo de audio
nombre_archivo = "grabacion.wav"
write(nombre_archivo, frecuencia_muestreo, audio)

print(f"Grabación guardada en {nombre_archivo}")
