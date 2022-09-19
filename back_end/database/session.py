from .connection2 import session_local

async def start_session():
    try:
       db = session_local()
       yield db
    finally:
       db.close()
