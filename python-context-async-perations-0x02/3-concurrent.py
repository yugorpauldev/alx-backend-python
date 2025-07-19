import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('example.db') as conn:
        cursor = await conn.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        await cursor.close()
        return results

async def async_fetch_older_users():
    async with aiosqlite.connect('example.db') as conn:
        cursor = await conn.execute("SELECT * FROM users WHERE age > ?", (40,))
        results = await cursor.fetchall()
        await cursor.close()
        return results

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return users, older_users

# Run the concurrent fetch
if __name__ == "__main__":
    results = asyncio.run(fetch_concurrently())
    print("All users:", results[0])
    print("Users older than 40:", results[1])