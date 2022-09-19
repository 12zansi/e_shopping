
from sqlalchemy import Column,Integer,String
from back_end.database.connection2 import Base


class TBUsers(Base):
    __tablename__ = 'users'
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(70), unique = True)
    email = Column(String(70), unique = True)
    password = Column(String(300))
    is_admin = Column(Integer, default = 0)
    otp = Column(Integer)




