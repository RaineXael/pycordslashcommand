#run this file to make a new reminder_key file for use with reminder.py
#keep this key secret and don't run this script again because you'll overwrite
#the key and lose all your data
from cryptography.fernet import Fernet
with open("./reminder_key", "wb") as binary_file:
    binary_file.write(Fernet.generate_key())

    
