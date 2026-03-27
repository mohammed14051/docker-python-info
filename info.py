import os
import socket
import datetime

print("=== SYSTEM INFO ===")
print("Time:", datetime.datetime.now())
print("Hostname:", socket.gethostname())
print("Current Files:", os.listdir())

try:
    print("User:", os.getlogin())
except:
    print("User: Not available in container")
