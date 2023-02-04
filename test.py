from db import SQL_Manager
import asyncio

async def test_program():
    
    sql = SQL_Manager('./example.db')
    print(await sql.select_all('table1','*'))
    await sql.close_database()

print(input())   
asyncio.run(test_program())