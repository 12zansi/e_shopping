from sqlalchemy import Column,Integer,ForeignKey
from back_end.database.connection2 import Base


class TBFavorite(Base):
    __tablename__ = 'favorites'
    id =  Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
