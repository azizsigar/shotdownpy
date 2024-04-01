import platform
import subprocess

def shutdown_computer():
    system = platform.system()
    if system == "Windows":
        # Windows için shutdown komutunu kullan
        subprocess.run(["shutdown", "/s", "/t", "1"])
    elif system == "Linux":
        # Linux için shutdown komutunu kullan
        subprocess.run(["sudo", "shutdown", "-h", "now"])
    else:
        print("Bu işletim sistemi desteklenmiyor.")

if __name__ == "__main__":
    shutdown_computer()
