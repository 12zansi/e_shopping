from sqlalchemy import Column,String,ForeignKey,Integer
from back_end.database.connection2 import Base

class TBAddress(Base):
    __tablename__ = 'address'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    id = Column(Integer, primary_key = True, index = True)
    receiver_name = Column(String(50))
    mobile_no = Column(String(10))
    address_line1 = Column(String(100))
    address_line2 = Column(String(100))
    city = Column(String(20))
    pincode = Column(String(6))
    state = Column(String(20))
    type = Column(String(7))
    user_id = Column(Integer, ForeignKey("users.id"))
