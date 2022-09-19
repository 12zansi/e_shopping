from sqlalchemy import Column,Integer,String, ForeignKey
from back_end.database.connection2 import Base

class TBProductDetails(Base):
     __tablename__ = 'product_details'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }

     id = Column(Integer, primary_key = True, index = True)
     attribute_name = Column(String(300))
     attribute_value = Column(String(700))
     product_id = Column(Integer, ForeignKey("products.id"))
     user_id = Column(Integer, ForeignKey("users.id"))