import datetime
from sqlalchemy import Column,String,ForeignKey,Integer,DateTime
from back_end.database.connection2 import Base

class TBReview(Base):
    __tablename__ = 'reviews'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    id = Column(Integer, primary_key = True, index = True)
    rating = Column(Integer)
    comment = Column(String(700))
    date  = Column(DateTime, default = datetime.datetime.today())
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    like = Column(Integer, default = 1)
