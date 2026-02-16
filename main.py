import json
import time
import random
import math
import paho.mqtt.client as mqtt  

BROKER_ADDRESS = "test.mosquitto.org" 
BROKER_PORT = 8080
MQTT_TOPIC = "ecte474/fleet/telemetry" # Topic

FLEET_SIZE = 3
SIMULATION_SPEED = 0.00015 

# Route - loop around a block in Downtown Dubai
ROUTE_WAYPOINTS = [
    (25.1972, 55.2744),
    (25.1985, 55.2720),
    (25.2000, 55.2750),
    (25.1990, 55.2780),
    (25.1972, 55.2744)
]

# --- MQTT SETUP ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker! (Code: {rc})")
    else:
        print(f"Failed to connect, return code {rc}")

# Force usage of the older API version to match your callback function
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, transport="websockets")
client.on_connect = on_connect

print(f"Connecting to broker: {BROKER_ADDRESS}...")
client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
client.loop_start() # Starts a background thread to handle network traffic

# --- TRUCK CLASS ---
class Truck:
    def __init__(self, truck_id, start_index):
        self.id = truck_id
        self.current_waypoint_idx = start_index
        self.lat = ROUTE_WAYPOINTS[start_index][0]
        self.lon = ROUTE_WAYPOINTS[start_index][1]
        self.speed = 0
        self.rpm = 800
        self.temp = 85.0

    def move(self):
        # 1. Target Management
        target_idx = (self.current_waypoint_idx + 1) % len(ROUTE_WAYPOINTS)
        target_lat, target_lon = ROUTE_WAYPOINTS[target_idx]

        # 2. Vector Math
        d_lat = target_lat - self.lat
        d_lon = target_lon - self.lon
        distance = math.sqrt(d_lat**2 + d_lon**2)

        # 3. Movement Logic
        if distance < SIMULATION_SPEED:
            self.lat = target_lat
            self.lon = target_lon
            self.current_waypoint_idx = target_idx
            self.speed = random.randint(20, 30) # Slow down for corner
        else:
            self.lat += (d_lat / distance) * SIMULATION_SPEED
            self.lon += (d_lon / distance) * SIMULATION_SPEED
            if self.speed < 90:
                self.speed += random.uniform(0, 3) # Accelerate

        # 4. Physics Correlation
        target_rpm = 800 + (self.speed * 32)
        self.rpm = int(target_rpm + random.uniform(-50, 50))
        
        # Temp logic: Overheat if RPM is high for too long
        if self.rpm > 3000:
            self.temp += 0.2
        elif self.rpm < 1500:
            self.temp -= 0.1
        self.temp = max(80.0, min(self.temp, 115.0))

    def generate_payload(self):
        return {
            "device_id": self.id,
            "timestamp": time.time(),
            "location": {
                "lat": round(self.lat, 6),
                "lon": round(self.lon, 6)
            },
            "telemetry": {
                "speed_kmh": int(self.speed),
                "rpm": self.rpm,
                "engine_temp_c": round(self.temp, 1)
            }
        }

# --- MAIN LOOP ---
trucks = [Truck(f"Truck_0{i+1}", i % len(ROUTE_WAYPOINTS)) for i in range(FLEET_SIZE)]

try:
    while True:
        for truck in trucks:
            truck.move()
            payload = truck.generate_payload()
            json_payload = json.dumps(payload)
            
            # PUBLISH TO BROKER
            client.publish(MQTT_TOPIC, json_payload)
            print(f"Published: {json_payload}")
            
        time.sleep(2) # Update every 2 seconds

except KeyboardInterrupt:
    print("\nDisconnecting...")
    client.loop_stop()
    client.disconnect()