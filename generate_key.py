#Not a script that has to do with a bot, this just spits out a key to put in the .env
from cryptography.fernet import Fernet
print(Fernet.generate_key())