from email.policy import default
from sqlalchemy import Column,Integer,String,ForeignKey
from back_end.database.connection2 import Base

class TBProducts(Base):
    __tablename__ = 'products'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    id = Column(Integer, primary_key = True)
    name = Column(String(200))
    description = Column(String(800))
    mrp = Column(Integer)
    price = Column(Integer)
    brand_id = Column(Integer,ForeignKey("brands.id"))
    thumbnail_id = Column(Integer, default= 0)
    category_id = Column(Integer,ForeignKey("categories.id"))
    return_policy_in_days = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Integer,default = 1)
