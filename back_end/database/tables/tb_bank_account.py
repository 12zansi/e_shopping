from sqlalchemy import Column,String,ForeignKey,Integer
from back_end.database.connection2 import Base

class TBBankAccounts(Base):
    __tablename__ = 'bank_accounts'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    id = Column(Integer, primary_key = True, index = True)
    holder_name = Column(String(50))
    account_no = Column(String(30))
    ifsc_code =  Column(String(50))
    branch_name = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.id"))