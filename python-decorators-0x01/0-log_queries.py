import sqlite3
import functools


def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        if query:
            
            print(f"[LOG] Executing SQL query: {query}")
        
        else:
            print(f"[LOG] No SQL query found in arguments.")
        
        return func(*args,*kwargs)
    return wrapper
    
