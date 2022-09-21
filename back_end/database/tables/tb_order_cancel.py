import datetime
from sqlalchemy import Column,Integer,String, ForeignKey, DateTime
from back_end.database.connection2 import Base

class TBProductDetails(Base):
     __tablename__ = 'order_cancel'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }
 
     id = Column(Integer, primary_key = True, index = True)
     order_id =  Column(Integer, ForeignKey("orders.id"))
     date = Column(DateTime, default = datetime.datetime.today())
     reason = Column(String(500))