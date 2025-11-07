import serial
import time
import os

# Configuration
PORT = "COM6"  # Change selon ton PC (ex: COM3, COM5, etc.)
BAUDRATE = 9600
FILENAME = "E:\\Mini projet S9\\mov_o.csv"  # Chemin absolu

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    #time.sleep(2)  # Laisser l'Arduino se préparer
    ser.flush()

    print("✅ Connexion série établie. Lecture des données...")

    # Vérifier si le fichier existe déjà
    if os.path.exists(FILENAME):
        print(f"⚠️  Le fichier {FILENAME} existe déjà. Les nouvelles données seront ajoutées.")

    with open(FILENAME, "a") as file:
        print(f"✅ Fichier ouvert : {os.path.abspath(FILENAME)}")  # Affiche le chemin exact
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print(line)  # Afficher dans la console
                file.write(line + "\n")  # Écrire dans le fichier
                file.flush()  # Forcer l'écriture immédiate

except serial.SerialException as e:
    print(f"❌ Erreur de connexion au port série : {e}")
except KeyboardInterrupt:
    print("\n🔴 Arrêt du script (Ctrl + C).")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("✅ Connexion série fermée.")