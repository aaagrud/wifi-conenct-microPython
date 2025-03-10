import network
import time

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print(wlan.scan())  
    
    
    if not wlan.isconnected():
        print(f"Connecting to {ssid}...")
        wlan.connect(ssid, password)

        timeout = 10  # Maximum number of attempts
        while not wlan.isconnected() and timeout > 0:
            print("Trying to connect...")
            time.sleep(2)
            timeout -= 1  # Reduce timeout counter
        
        if wlan.isconnected():
            print(f"\nConnected to {ssid}")
            print("Network Config:", wlan.ifconfig())
        else:
            print("\nFailed to connect! Please check SSID, password, and hotspot settings.")

# Replace with your mobile hotspot credentials
connect_to_wifi('Redmi Note 11 Pro+ 5G', 'cabin8artemis+')
