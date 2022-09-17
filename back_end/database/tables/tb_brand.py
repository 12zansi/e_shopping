from email.policy import default
from sqlalchemy import Column,Integer,String, ForeignKey
from back_end.database.connection2 import Base

class TBBrand(Base):
    __tablename__ = 'brands'
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(50), unique = True)