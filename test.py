from db import SQL_Manager
import asyncio

async def test_program():
    
    sql = await SQL_Manager('./example.db')
    print(await sql.select_all('table1','*'))
    await sql.close_database()
    
asyncio.run(test_program())