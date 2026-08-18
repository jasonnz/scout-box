#!/usr/bin/env python3
"""
scout-box main.py
Simulation mode for testing the predator scout camera pipeline.
"""

import time
import datetime
import os
import json
from pathlib import Path

# --- CONFIGURATION ---
LOG_DIR = "logs"
IMAGE_DIR = "images"
SIMULATION_INTERVAL = 10  # Seconds between simulated triggers

# --- SETUP DIRECTORIES ---
def setup_directories():
    """Create the folders for logs and images if they don't exist."""
    Path(LOG_DIR).mkdir(exist_ok=True)
    Path(IMAGE_DIR).mkdir(exist_ok=True)
    print(f"✅ Directories ready: {LOG_DIR}/, {IMAGE_DIR}/")

# --- LOGGING FUNCTIONS ---
def log_trigger(timestamp, source="simulation"):
    """Write a trigger event to a JSONL log file."""
    log_file = Path(LOG_DIR) / f"triggers_{datetime.datetime.now().strftime('%Y%m%d')}.log"
    
    event = {
        "timestamp": timestamp.isoformat(),
        "source": source,
        "status": "photo_saved"
    }
    
    with open(log_file, "a") as f:
        f.write(json.dumps(event) + "\n")
    
    print(f"📝 Logged: {timestamp.strftime('%H:%M:%S')} - {source}")

def generate_mock_image(timestamp):
    """Simulate saving a photo (creates a .txt placeholder instead of .jpg for testing)."""
    filename = f"capture_{timestamp.strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = Path(IMAGE_DIR) / filename
    
    # Write a dummy file to simulate the camera output
    with open(filepath, "w") as f:
        f.write(f"Simulated photo capture at {timestamp.isoformat()}\n")
        f.write("(Replace this with actual camera code when hardware arrives.)")
    
    print(f"📸 Mock image saved: {filepath}")
    return filepath

# --- MAIN LOOP ---
def main():
    print("\n🚀 Scout Box Simulator Starting...")
    print(f"⏱️  Triggering every {SIMULATION_INTERVAL} seconds.")
    print(f"📂 Logs go to: {LOG_DIR}/")
    print(f"🖼️ Images go to: {IMAGE_DIR}/")
    print("Press Ctrl+C to stop.\n")
    
    setup_directories()
    
    try:
        while True:
            now = datetime.datetime.now()
            
            # 1. Simulate a PIR trigger
            print(f"\n⚡ [TRIGGER] Sensor activated!")
            
            # 2. Take a mock photo
            generate_mock_image(now)
            
            # 3. Log the event
            log_trigger(now)
            
            # 4. Wait before next trigger
            print(f"💤 Sleeping for {SIMULATION_INTERVAL} seconds...")
            time.sleep(SIMULATION_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Scout Box stopped by user. Goodbye!")

if __name__ == "__main__":
    main()