# 🚛 Smart Fleet Management System

## 📖 Overview
This project is a complete end-to-end IIoT solution designed to simulate and monitor a fleet of commercial vehicles in real-time. It integrates **Edge Computing (Python Simulation)**, **Network Communication (MQTT)**, and **Cloud Visualization (Node-RED)** to track vehicle location, engine health, and driver behavior.

The system addresses the problem of **fleet maintenance and safety** by providing real-time telemetry and automated alerts for engine overheating events.

## 🚀 Features
* **📍 Real-Time GPS Tracking:** Simulates a fleet of trucks moving along a realistic route in Dubai (Sheikh Zayed Road/Downtown) using waypoint interpolation.
* **⚙️ Live Telemetry:** Monitors critical vehicle stats including:
    * **Speed (km/h)**
    * **Engine RPM** (Correlated to speed for realism)
    * **Engine Temperature** (Dynamic physics simulation)
* **⚠️ Automated Safety Logic:** "Edge" logic detects critical overheating (>105°C) and triggers immediate dashboard alerts.
* **☁️ Cloud Dashboard:** A centralized Node-RED dashboard featuring live maps, gauges, and historical data charts.

## 🛠️ Tech Stack (Free & Open Source)
[cite_start]This project was built using strictly free/open-source tools as per project requirements[cite: 12, 26]:
* **Device Layer:** Python 3.x (Simulation script)
* [cite_start]**Communication Layer:** MQTT (HiveMQ Public Broker / Mosquitto) [cite: 25]
* [cite_start]**Application Layer:** Node-RED & Node-RED Dashboard [cite: 25]
* **Libraries:** `paho-mqtt` (Python), `node-red-contrib-web-worldmap`

## 📦 Installation & Usage

### 1. Prerequisites
* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js & Node-RED](https://nodered.org/docs/getting-started/local)

### 2. Setup the Device Simulation
1.  Clone this repository:
    ```bash
    git clone [https://github.com/yourusername/smart-fleet-iot.git](https://github.com/yourusername/smart-fleet-iot.git)
    ```
2.  Install the required Python library:
    ```bash
    pip install paho-mqtt
    ```
3.  Run the simulation script:
    ```bash
    python fleet_sim.py
    ```

### 3. Setup the Dashboard (Node-RED)
1.  Start Node-RED:
    ```bash
    node-red
    ```
2.  Open your browser to `http://localhost:1880`.
3.  Install the required palette nodes:
    * `node-red-dashboard`
    * `node-red-contrib-web-worldmap`
4.  Import the `flows.json` file provided in this repository.
5.  Click **Deploy**.
6.  Access the dashboard at `http://localhost:1880/ui`.
