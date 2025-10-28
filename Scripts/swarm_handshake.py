# swarm_handshake.py
# Minimal prototype with simulated battery monitoring and retry logic.
import time
import random

BATTERY_THRESHOLD = 20  # %

def check_battery(my_id):
    battery_level = random.randint(10, 100)  # Simulate real voltage reading
    print(f"Drone-{my_id} battery: {battery_level}%")
    return battery_level

def send_with_retry(my_id, max_retries=2):
    if check_battery(my_id) < BATTERY_THRESHOLD:
        print(f"Drone-{my_id} returning to Hive - low battery")
        return None

    for attempt in range(max_retries + 1):
        msg = f"hello from drone-{my_id}"
        if random.random() < 0.2:  # 20% simulated packet loss
            print(f"Drone-{my_id}: packet lost on attempt {attempt + 1}")
            time.sleep(0.5)
            continue
        print(f"Drone-{my_id}: {msg}")
        return msg
    print(f"Drone-{my_id} gave up after {max_retries} retries")
    return None

def drone_listen(my_id):
    print(f"Drone-{my_id} listening...")
    # Simulate receiving a message
    return "hello from other-drone"

print("=== Drone Swarm Handshake Demo ===\n")

for turn in range(2):
    sender = 1 if turn == 0 else 2
    listener = 2 if turn == 0 else 1

    message = send_with_retry(sender)
    if not message:
        print("Skipped due to loss or low battery\n")
        continue

    time.sleep(0.3)
    received = drone_listen(listener)
    print(f"{received} acknowledged\n")

print("Handshake complete. Add LoRa + Kyber in Phase 2.")
