from cryptography.fernet import Fernet
import aiosqlite
from datetime import datetime
from discord.ext import tasks, commands
# the messages here are encrypted so i don't see people's private messages
# when doing things in the database


class Reminder(commands.Cog):

    def __init__(self, db_file, bot):
        try:
            with open("./reminder_key", "rb") as binary_file:
                self.key = binary_file.read()
            self.fernet = Fernet(self.key)
            self.db_file = db_file
            self.bot = bot
            self.printer.start()
            
            self.debug = False #set this to true to remove the negative time restricion
        except:
            print(
                'There\'s a problem initializing the fernet key. Was reminder_key created?')

    def cog_unload(self):
        self.printer.cancel()

    async def on_check_messages(self):
        try:
            db = await aiosqlite.connect(self.db_file)
            cursor = await db.execute(f'SELECT * FROM \'reminders\' WHERE datetime(time) < datetime(\'{str(datetime.now())}\');')
            result = await cursor.fetchall()
            await cursor.close()
            await db.commit()
            await db.close()

            # if > 1 entry in result return the result to be processed in remindercheck
            if len(result) > 0:
                return result
            return None
        except Exception as e:
            print(f"exception in db checking due messages: {e}")
            return None

    async def release_messages(self, result: list):
        # send dms to the poeple
        db = await aiosqlite.connect(self.db_file)
        try:
            for reminder in result:
                
                    message = self.fernet.decrypt(str(reminder[1], 'UTF-8')).decode('UTF-8')
                    print(str(message))
                    user = await self.bot.fetch_user(int(reminder[0]))
                    await user.send(f"<@{str(reminder[0])}>, Your reminder due for {reminder[2]}:\n\"{str(message)}\"")
                    # also erase entry from db                    
                    await db.execute(f"DELETE FROM reminders WHERE uid = ? AND message = ? and time = ?", (reminder[0], reminder[1], reminder[2]))
                    await db.commit()                    
        except Exception as e:
            print(f"Exception occoured during removal of fulfilled request: {e}")
        finally:
            await db.close()        
            

    @tasks.loop(seconds=15.0)
    async def printer(self):
        message_check = await self.on_check_messages()
        if message_check != None:
            await self.release_messages(message_check)

    async def insert_reminder(self, table_name, uid, message, time_obj):
        # returns true or false wether success or fail
        try:
            db = await aiosqlite.connect(self.db_file)
            await db.execute(f"INSERT INTO {table_name} VALUES(?,?,?)", (uid, self.fernet.encrypt(bytes(message, 'UTF-8')), str(time_obj)))
            await db.commit()
            await db.close()
            return True
        except Exception as e:
            print(e)
            return False

    def validate_time(self, year, month, day, hour, minute):

        # input date
        date_string = f'{year}-{month}-{day}-{hour}-{minute}'
        # giving the date format
        date_format = '%Y-%m-%d-%H-%M'
        # formatting the date using strptime() function
        dateObject = datetime.strptime(date_string, date_format)
        if dateObject <= datetime.today() and not self.debug:
            raise IndexError()  # technically out of bounds for time
        return dateObject

    async def on_add_reminder(self, uid, message, year, month, day, hour, minute):
        # fired when the reminder command is fired off
        # check inputs then do the below
        try:
            time_obj = self.validate_time(year, month, day, hour, minute)
            await self.insert_reminder('reminders', uid, message, time_obj)
            return f'Reminder: \"{message}\" added for {time_obj}'
        except ValueError:
            return "Invalid format! Please check your numbers."
        except IndexError:
            return 'The time you entered was in the past. Please enter a future time and date.'
