from cryptography.fernet import Fernet
import aiosqlite
from datetime import datetime
class Reminder():
    
    def __init__(self, db_file):
        try:
            with open("./reminder_key", "rb") as binary_file:
                self.key = binary_file.read()             
            self.fernet = Fernet(self.key)
            self.db_file = db_file
        except:
            print('There\'s a problem initializing the fernet key. Was reminder_key created?')

    async def insert_reminder(self, table_name, uid,message):
                #returns true or false wether success or fail
                try:
                    db = await aiosqlite.connect(self.db_file)
                    
                    await db.execute(f"INSERT INTO {table_name} VALUES(?,?,?)",(uid,self.fernet.encrypt(bytes(message,'UTF-8')),str(datetime.today().strftime('%Y-%m-%d'))))
                    await db.commit()
                    await db.close()
                    return True
                except Exception as e:
                    print(e)
                    return False

    async def on_add_reminder(self, uid, message):
        #fired when the reminder command is fired off
        #check inputs then do the below
        await self.insert_reminder('reminders',uid,message)
    
    
    