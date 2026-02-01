import os
from cryptography.fernet import Fernet
import csv
from datetime import datetime

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Target directory
target_dir = os.path.expanduser("~/ransomware_sim")

# CSV lof file
log_file = os.path.join(target_dir, "ransom_log.csv")

# Initialize CSV
with open(log_file, mode='w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["File Name", "File Size (bytes)", "Timestamp"])

# Encrypt files and log data
for filename in os.listdir(target_dir):
	filepath = os.path.join(target_dir, filename)

	# Skip the log file and already encrypted files
	if filename == "ransom_log.csv" or filename.endswith("encrypted"):
	    continue

	# Read original data
	with open(filepath, 'rb') as f:
	    data = f.read()

	# Encrypt data
	encrypted_data = cipher.encrypt(data)

	# Save encrypted file
	with open(filepath + ".encrypted", 'wb') as f:
	    f.write(encrypted_data)

	# Log details
	file_size = os.path.getsize(filepath)
	timestamp = datetime.now().isoformat()

	with open(log_file, mode= 'a', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow([filename, file_size, timestamp])

print ("Encryption simulation complete. Log created.")

