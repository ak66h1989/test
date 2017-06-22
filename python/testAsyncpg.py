import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user='postgres', password='d03724008',
                                 database='tse', host='127.0.0.1')
    values = await conn.fetch('''SELECT * FROM mytable''')
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())