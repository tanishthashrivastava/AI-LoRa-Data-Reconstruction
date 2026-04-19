#  AI-Based LoRa Data Reconstruction System

##  Overview
LoRa (Long Range) communication systems often suffer from packet loss and fragmented telemetry data, especially in remote or low-signal environments. This project focuses on reconstructing missing GPS coordinates using machine learning techniques to ensure continuous and reliable tracking.

---

##  Problem Statement
In real-world LoRa networks, transmitted data packets may be incomplete due to signal interference, resulting in missing latitude and longitude values. This leads to broken tracking paths and loss of situational awareness.

---

##  Solution
This project implements an AI-based reconstruction system that:
- Detects fragmented telemetry data
- Predicts missing GPS coordinates using machine learning
- Restores continuous movement paths
- Visualizes reconstructed data on an interactive map

---

##  Approach

### 1. Data Simulation
- Created a realistic LoRa dataset with:
  - Missing values (NULL)
  - Fragmented packets
  - Duplicate entries
  - Multiple devices

### 2. Data Cleaning
- Removed duplicate records
- Identified missing latitude & longitude values
- Applied forward-fill and backward-fill techniques

### 3. ML-Based Reconstruction
- Trained **Random Forest Regression models**
- Features used:
  - Speed
  - Direction
  - Signal Strength
- Predicted missing GPS coordinates

### 4. Visualization
- Plotted device movement using **Folium map**
- Highlighted:
  - 🟢 Normal Data
  - 🔴 Reconstructed Data
  - 🔵 Movement Path

### 5. Interactive UI
- Built using **Streamlit**
- Allows users to:
  - Upload LoRa dataset
  - Reconstruct missing data
  - Visualize results instantly
  - Download processed data

---

##  Live Demo
 https://ai-lora-data-reconstruction-7kjpnyx2xtr4kzrhg7yhjd.streamlit.app

---

##  Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn (Random Forest)
- Folium (Map Visualization)
- Streamlit (UI)

---

##  Key Insights
- Missing GPS data can be accurately reconstructed using movement patterns
- Signal strength plays a critical role in data fragmentation
- ML-based reconstruction ensures continuity in tracking systems
- Visualization helps identify reconstructed vs original data clearly

---

##  Visualization

- 🟢 Green → Original data  
- 🔴 Red → Reconstructed data  
- 🔵 Blue → Movement path  

(Add your map screenshot here)

---

##  Limitations
- Uses synthetic dataset instead of real LoRa hardware data
- Prediction accuracy depends on data quality and patterns

---

##  Future Scope
- Implement Kalman Filter for advanced smoothing
- Integrate real-time LoRa gateway data
- Deploy full-scale monitoring dashboard
- Add anomaly detection for unusual movement

---

##  How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/AI-LoRa-Data-Reconstruction.git
cd AI-LoRa-Data-Reconstruction
pip install -r requirements.txt
python -m streamlit run app/lora_app.py
