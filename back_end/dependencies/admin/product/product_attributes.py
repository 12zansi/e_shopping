
from back_end.database.connection import cursor, connection
from fastapi import Depends
from back_end.dependencies.login import UserLogin

class AdminProductAttributes(UserLogin):
    pass