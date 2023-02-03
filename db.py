import aiosqlite

class SQL_Manager():
    async def __init__(self):
        self.db = await aiosqlite.connect("./example.db")
    
    async def select(self, table_name, where_statement):
        #should check for any improper vaues
        print("skeleton method as of now")
        
    async def insert(self, table_name, value_inputs):
        #should check for any improper vaues
        print("skeleton method as of now")
    
    async def close_database(self):
        await self.db.close()
