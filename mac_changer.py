import subprocess

# subprocess.call("ifconfig", shell=True)
subprocess.call("ipconfig", shell=True)

# cambiar mac
subprocess.call("ipconfig eth0 down", shell=True)
subprocess.call("ipconfig eth0 hw ether 00:11:22:33:44:66", shell=True)

subprocess.call("ipconfig eth0 up", shell=True)