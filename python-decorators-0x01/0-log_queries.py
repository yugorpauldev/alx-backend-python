
from datetime import datetime
import functools


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
    
