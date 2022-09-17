import datetime
from sqlalchemy import Column,String,ForeignKey,Integer,DateTime
from back_end.database.connection2 import Base

class TBReturn(Base):
    __tablename__ = 'product_returns'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    id = Column(Integer, primary_key = True, index = True)
    reason = Column(String(300))
    date = Column(DateTime, default = datetime.datetime.today())
    order_item_id =  Column(Integer, ForeignKey("order_items.id"))
    order_id =  Column(Integer, ForeignKey("orders.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    status_id = Column(Integer, ForeignKey("status.id"))
    bank_id = Column(Integer, ForeignKey("bank_accounts.id"))
