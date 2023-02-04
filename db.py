import aiosqlite

class SQL_Manager():
    def __init__(self, db_file):
        self.db = aiosqlite.connect(db_file)
        print (self.db)
    
    async def select_one(self, name, values, where_statement=""):
        #returns a list of the selected elements
        where_string = ""
        if where_statement != "":
            where_string = f"WHERE {where_statement}"
        cursor = await self.db.execute(f'SELECT {values} FROM {name} {where_string};')
        result = await cursor.fetchone()
        cursor.close()
        return result
    
    async def select_all(self, name, values, where_statement=""):
        #returns a list of the selected elements
        where_string = ""
        if where_statement != "":
            where_string = f"WHERE {where_statement}"
        cursor = await self.db.execute(f'SELECT {values} FROM {name} {where_string};')
        result = await cursor.fetchall()
        cursor.close()
        return result
        
    async def insert(self, table_name, value_inputs):
        #inserts values into the db
        print("skeleton method as of now")
    
    async def close_database(self):
        await self.db.close()
