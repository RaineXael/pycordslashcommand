
from discord.ext import tasks, commands
import aiosqlite
from datetime import datetime
from cryptography.fernet import Fernet
class ReminderCheck(commands.Cog):
    def __init__(self, db_file, bot):
        self.printer.start()
        self.bot = bot
        self.db_file = db_file
        
        
        with open("./reminder_key", "rb") as binary_file:
                self.key = binary_file.read()
        self.fernet = Fernet(self.key)

    def cog_unload(self):
        self.printer.cancel()

    async def on_check_messages(self):
        try:
            db = await aiosqlite.connect(self.db_file)
            cursor = await db.execute(f'SELECT * FROM \'reminders\' WHERE date(time) < \'{str(datetime.now())}\';')
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
        for reminder in result:
            print(reminder[1])
            message = self.fernet.decrypt(str(reminder[1],'UTF-8'))
            user = await self.bot.fetch_user(int(reminder[0]))
            await user.send(f"<@{str(reminder[0])}>, Your reminder due for {message}: \'{reminder[1]}\'")
            # also erase entry from db

    @tasks.loop(seconds=30.0)
    async def printer(self):
        message_check = await self.on_check_messages()
        if message_check != None:
            await self.release_messages(message_check)
