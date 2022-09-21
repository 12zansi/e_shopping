from back_end.Models.status import Status
from back_end.database.session import start_session
from requests import Session
from fastapi import Depends
from back_end.database.tables.tb_order_item import TBOrderItems
from back_end.dependencies.login import UserLogin, token_auth_scheme


class AdminOrders(UserLogin):
    
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    def  change_order_status(self, id: int, status: Status , token: str = Depends(token_auth_scheme)):

        user = AdminOrders._get_user(token)

        if user[2] == 1:
            query = self.db.query(TBOrderItems).filter(TBOrderItems.id == id, TBOrderItems.order_id != None)\
                .update({ TBOrderItems.status_id: status.status_id})
    
            self.db.commit()
            if query:
                return { "message": "status updated" }

            return { "message": "order item doesn't exist " }
        
        return { "message": "Could Not Valid Credentials" }