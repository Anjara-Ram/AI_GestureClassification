# Gesture Classification with Arduino & TensorFlow

Real-time gesture recognition using Arduino IMU data and TensorFlow Lite.

## 📁 Files

- **`Collect_data_from_IMU.ino`** - Arduino code to collect IMU sensor data
- **`enregistre_imu.py`** - Python script to receive and save data from Arduino
- **`a_char.csv`, `c_char.csv`** - Collected gesture datasets
- **`arduino_tinyml_workshop.ipynb`** - Jupyter notebook for model training and TensorFlow Lite conversion

## 🚀 Quick Start

1. **Collect Data**: Upload `Collect_data_from_IMU.ino` to Arduino and run `enregistre_imu.py`
2. **Train Model**: Use the Jupyter notebook to train your TensorFlow model
3. **Deploy**: Convert to TensorFlow Lite and deploy back to Arduino

## 🎯 Gestures
- `a_char` - Gesture A
- `c_char` - Gesture C
- `m_char` - Gesture M
