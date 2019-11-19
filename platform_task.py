import platform
import subprocess

if __name__ == "__main__":
    if all(a in platform.platform() for a in ["debian", "arm"]):
        subprocess.call(["sed", "-i", "/pandas/d", "requirements.txt"])
