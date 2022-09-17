from back_end.Models.favorite_list import FavoriteList
from back_end.database.connection import cursor, connection
from fastapi import Depends
from back_end.dependencies.login import UserLogin,token_auth_scheme

