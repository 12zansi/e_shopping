from sqlalchemy import Column,Integer,ForeignKey, String
from back_end.database.connection2 import Base

class TBPOrderItems(Base):
      
      __tablename__ = 'order_items'
      __table_args__ = {
        'mysql_engine': 'InnoDB'
      }
      id = Column(Integer, primary_key = True, index = True)
      product_name = Column(String(300))
      product_price = Column(Integer)
      product_mrp = Column(Integer)
      quantity = Column(Integer)
      image_name = Column(String(100))
      product_id = Column(Integer, ForeignKey("products.id"))
      status_id = Column(Integer, ForeignKey("status.id"))
      order_id =  Column(Integer, ForeignKey("orders.id"))
      cart_id = Column(Integer,ForeignKey("carts.id"))
      user_id = Column(Integer, ForeignKey("users.id"))