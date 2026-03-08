# Smart Fleet Monitoring System

## Project Overview
This project presents a comprehensive Internet of Things (IoT) system designed for the real-time monitoring and management of commercial vehicle fleets. The objective is to enhance vehicle safety and prevent critical mechanical failures through remote telemetry and edge computing.

The system simulates a fleet of **10 vehicles operating within Dubai**, generating dynamic metrics including:

- GPS coordinates  
- Speed  
- Engine RPM  
- Engine temperature  

It utilizes a **dual-path hybrid architecture** to provide both **low-latency local visualization** and **rate-limited cloud data persistence**.

---

# System Architecture

The project is built on a robust IoT pipeline:

### 1. Simulated Vehicle Sensors (Edge Device)
An object-oriented Python script (`main.py`) acts as the edge device, generating telemetry and evaluating local logic such as:

- Overspeeding alerts
- Engine overheating alerts

### 2. Network Protocol (MQTT)
Telemetry is packaged as **JSON** and published to a **public Mosquitto broker**:

```
test.mosquitto.org
Port: 1883
```

### 3. Local Application (Node-RED)
Node-RED subscribes to the MQTT feed to drive a **real-time web dashboard** that includes:

- Interactive fleet map
- Live vehicle health gauges

### 4. Cloud Storage (ThingSpeak)

- Historical data visualization
- Persistent cloud storage

---

# Key Features

- **Real-Time Tracking**  
  Live mapping of all **30 vehicles simultaneously**

- **Edge Alerts**  
  Immediate system flags for:
  - Overspeeding
  - High engine temperature

- **Targeted Dashboarding**  
  Clickable map interface to monitor **individual truck telemetry**

- **Cloud Archival**  
  Automated API integration with **ThingSpeak** for long-term analytics

---

# Repository Structure

```
Smart-Fleet-Tracker/
│
├── python_edge_simulator/
│   ├── main.py          # Telemetry generation script
│   └── requirements.txt      # Python dependencies
│
├── node_red_dashboard/
│   └── flows.json            # Exported Node-RED workspace
│
├── assets/
│   ├── architecture.png
│   ├── dashboard.png
└── README.md
```

---

# Prerequisites

To run this project locally, install the following:

- **Python 3.8+**
- **Node.js**
- **Node-RED**

---

# Installation

### 1. Clone the repository

```bash
git clone https://github.com/leomint28/Smart-Fleet-Tracker.git
cd Smart-Fleet-Tracker
```

### 2. Install Python dependencies

```bash
cd Smart-Fleet-Tracker
pip install -r requirements.txt
```

### 3. Set up the Node-RED Dashboard

Start Node-RED:

```bash
node-red
```

Open your browser and navigate to:

```
http://localhost:1880
```

Then:

1. Go to **Menu ≡ → Import**
2. Upload `node_red_dashboard/flows.json`
3. Click **Deploy**

---

# Usage

### Start the fleet simulator

```bash
python main.py
```

### View the real-time dashboard

```
http://localhost:1880/ui
```

### View historical cloud data

Access your configured **ThingSpeak channel** to see stored telemetry and charts.

---