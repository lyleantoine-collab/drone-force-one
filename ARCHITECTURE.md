# Architecture Overview 

## 1. Deployment Flow 

- Backpack opens → drones launch in sequence (thermal lead, relay, scouts).
- Role assigned at boot via hull QR; AI confirms availability.
- Thermal scout scans 120° cone, streams heat-map tiles immediately.
- Relay climbs to 50 m, locks sat uplink, bridges to truck/base (The Hive).
- From the Hive: med-delivery drones launch

## 2. Communication Mesh 

- Drone-to-drone: LoRaWAN 915 MHz, 10 km LOS.
- Commands: MAVLink/UDP, Kyber-encrypted, key rotate per flight.
- Dynamic roles-if signal drops, any drone becomes repeater.
- Truck broadcasts simple directives: expand 500 m → scouts spiral.

## 3. Data Pipeline 

- Capture → compress (MJPEG tiles).
- Tag → edge YOLO-lite: human, vehicle, hotspot (<2 s).
- Push → truck triage dashboard; auto-queue med-pods or evac.

Modular: swap ArduPilot → PX4 by changing firmware path. 
> [Scouts x7] [F-350 Truck]

Pull requests welcome.
