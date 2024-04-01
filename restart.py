import platform
import subprocess

def restart_computer():
    system = platform.system()
    if system == "Windows":
        # Windows için yeniden başlatma komutunu kullan
        subprocess.run(["shutdown", "/r", "/t", "1"])
    elif system == "Linux":
        # Linux için yeniden başlatma komutunu kullan
        subprocess.run(["sudo", "shutdown", "-r", "now"])
    else:
        print("Bu işletim sistemi desteklenmiyor.")

if __name__ == "__main__":
    restart_computer()
