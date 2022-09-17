from sqlalchemy import Column, Integer, ForeignKey, DateTime
import datetime
from back_end.database.connection2 import Base
 
class TBCart(Base):
    __tablename__ = 'carts'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    id = Column(Integer, primary_key = True, index = True)
    status_id = Column(Integer, ForeignKey("status.id"))
    user_id = Column(Integer, ForeignKey("users.id"))