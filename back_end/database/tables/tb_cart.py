from sqlalchemy import Column, Integer, ForeignKey
from back_end.database.connection2 import Base
 
class TBCarts(Base):
    __tablename__ = 'carts'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    id = Column(Integer, primary_key = True, index = True)
    status_id = Column(Integer, default = 1)
    user_id = Column(Integer, ForeignKey("users.id"))