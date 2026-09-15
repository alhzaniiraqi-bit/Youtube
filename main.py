import requests
import time

FIREBASE_URL = "https://music-17150-default-rtdb.firebaseio.com/server_time.json"

def auto_update_time():
    while True:
        try:
            response = requests.put(FIREBASE_URL, json={".sv": "timestamp"}, timeout=10)
            print(f"Updated successfully: {response.status_code}")
        except Exception as e:
            print(f"Error updating time: {e}")
            
        # الانتظار لمدة 30 دقيقة (1800 ثانية)
        time.sleep(1800)

if __name__ == "__main__":
    auto_update_time()
