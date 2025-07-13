
from datetime import datetime
import functools
import sqlite3


def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        query = kwargs.get('query') or (args[0] if args else None)
        timespamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
        if query:
            
            print(f"[{timespamp}] Executing SQL query: {query}")
        
        else:
            print(f"[{timespamp}] No SQL query found in arguments.")
        
        return func(*args,*kwargs)
    return wrapper
    

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
