from sqlalchemy import Column,Integer,String, ForeignKey
from back_end.database.connection2 import Base

class TBProductImages(Base):
     __tablename__ = 'product_images'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }
     id = Column(Integer, primary_key = True, index = True)
     name = Column(String(100))
     product_id = Column(Integer, ForeignKey("products.id"))
     user_id = Column(Integer, ForeignKey("users.id"))
