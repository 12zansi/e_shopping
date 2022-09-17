from sqlalchemy import Column,Integer,String
from back_end.database.connection2 import Base

class TBStatus(Base):
    __tablename__ = 'status'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    id =  Column(Integer, primary_key = True, index = True)
    code = Column(String(20))
    type = Column(String(10))
    description = Column(String(70))