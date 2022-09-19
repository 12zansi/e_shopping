from email.policy import default
from sqlalchemy import Column,Integer,String
from back_end.database.connection2 import Base

class TBCategories(Base):
    __tablename__ = 'categories'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(50))
    image_name = Column(String(50))
    parent_id = Column(Integer, default = 0)
    is_active = Column(Integer,default = 1)


    