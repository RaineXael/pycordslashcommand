from cryptography.fernet import Fernet
import aiosqlite

class Reminder():
    
    def __init__(self):
        try:
            with open("./reminder_key", "rb") as binary_file:
                self.key = binary_file.read()             
            self.fernet = Fernet()
        except:
            print('There\'s a problem initializing the fernet key. Was reminder_key created?')

    async def insert_reminder(self, table_name, uid,message,time):
            #returns true or false wether success or fail
            try:
                db = await aiosqlite.connect(self.db_file)
                
                await db.execute(f"INSERT INTO {table_name} VALUES(?,?,?)",(uid,message,time))
                await db.commit()
                await db.close()
                return True
            except Exception as e:
                print(e)
                return False