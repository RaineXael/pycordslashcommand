import aiosqlite

class SQL_Manager():
    def __init__(self, db_file):
        self.db_file = db_file
        
    async def select(self, name, values='*', where_statement=""):
        #returns a list of the selected elements
        db = await aiosqlite.connect(self.db_file)
        where_string = ""
        if where_statement != "":
            where_string = f"WHERE {where_statement}"
        print(f'SELECT {values} FROM {name} {where_string};')
        cursor = await db.execute(f'SELECT {values} FROM {name} {where_string};')
        result = await cursor.fetchall()
        await cursor.close()
        await db.close()
        return str(result)
        
    async def insert(self, table_name, value_inputs):
        #returns true or false wether success or fail
        try:
            db = await aiosqlite.connect(self.db_file)
            print("input: " + f"INSERT INTO {table_name} VALUES({value_inputs})")
            await db.execute(f"INSERT INTO {table_name} VALUES({value_inputs})")
            await db.commit()
            await db.close()
            return True
        except Exception as e:
            print(e)
            return False
            
    
