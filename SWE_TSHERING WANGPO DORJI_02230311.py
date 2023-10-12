import subprocess
import time

def is_update_mode():
    update_status = subprocess.check_output(["softwareupdate", "--list"])
    return b'No new software available.' not in update_status

def is_connected_to_hotspot():
    wifi_info = subprocess.check_output(["networksetup", "-getairportnetwork", "en0"])
    return b'2wanlol' in wifi_info

def main():
    while True:
        if is_update_mode():
            if is_connected_to_hotspot():
                print("Connected to '2wanlol' hotspot. Pausing updates.")
                subprocess.call(["softwareupdate", "--schedule", "off"])
            else:
                print("Not connected to '2wanlol' hotspot. Resuming updates.")
                subprocess.call(["softwareupdate", "--schedule", "on"])
        time.sleep(30)

if __name__ == "__main__":
    main()

    


