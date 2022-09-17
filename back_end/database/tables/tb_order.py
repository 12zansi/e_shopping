import datetime
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from back_end.database.connection2 import Base


class TBPlaceOrder(Base):
      
      __tablename__ = 'orders'
      __table_args__ = {
        'mysql_engine': 'InnoDB'
      }
      id = Column(Integer, primary_key = True, index = True)
      total_price = Column(Integer)
      payment_method = Column(String(50), default = "cash on delivery")
      address_id = Column(Integer, ForeignKey("address.id"))
      order_date = Column(DateTime, default = datetime.datetime.today())
      user_id = Column(Integer, ForeignKey("users.id"))