import aiosqlite
from datetime import datetime
from discord.ext import tasks, commands


class Reminder(commands.Cog):

    def __init__(self, db_file, bot):
            self.db_file = db_file
            self.bot = bot
            self.printer.start()
            
            self.debug = False #set this to true to remove the negative time restricion

    def cog_unload(self):
        self.printer.cancel()

    async def get_all_reminders(self, uid):
        try:
            db = await aiosqlite.connect(self.db_file)
            cursor = await db.execute(f'SELECT * FROM \'reminders\' WHERE uid IS {uid}')
            result = await cursor.fetchall()
            await cursor.close()
            await db.commit()
            await db.close()

            # if > 1 entry in result return the result to be processed in remindercheck
            if len(result) > 0:
                builder_str = ""
                for reminder in result:
                    builder_str += f"⦁ \"{reminder[1]}\" at {reminder[2]}\n"
                return builder_str
            return "You have no reminders set."
        except Exception as e:
            return f"An error occoured when retrieving your data: {e}"


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
                    user = await self.bot.fetch_user(int(reminder[0]))
                    await user.send(f"<@{str(reminder[0])}>, Your reminder due for {reminder[2]}:\n\"{reminder[1]}\"")
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
            await db.execute(f"INSERT INTO {table_name} VALUES(?,?,?)", (uid, message, str(time_obj)))
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
