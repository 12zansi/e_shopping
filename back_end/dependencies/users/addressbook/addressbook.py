from fastapi import Depends
from back_end.Models.address import Address
from back_end.database.connection import cursor, connection
from back_end.database.tables.tb_address import TBAddress
from back_end.dependencies.login import UserLogin,token_auth_scheme
from back_end.database.session import start_session
from fastapi import Depends
from sqlalchemy import and_, or_, not_
from requests import Session


class AddressBook(UserLogin):
    
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    def add_address(self,address:Address, token = Depends(token_auth_scheme)):
        user = AddressBook._get_user(token)

        query  = self.db.query(TBAddress).filter(TBAddress.address_line1 == address.address_line1 and TBAddress.user_id == user[1]).first()
    
        if query:
            return {"message":"address already added"}

        query2 = TBAddress(
            receiver_name = address.receiver_name,
            mobile_no = address.mobile_no,
            address_line1 = address.address_line1,
            address_line2  = address.address_line2,
            city  = address.city,
            pincode = address.pincode,
            state = address.state,
            type = address.type,
            user_id = user[1]
            )
        AddressBook._add_in_table(self,query2)

        return {"data":query2,"success": True }

    def get_address(self, id:int, token = Depends(token_auth_scheme)):
        user = AddressBook._get_user(token)
    
        query = self.db.query(TBAddress).filter(and_(TBAddress.id == id, TBAddress.user_id == user[1])).all()
        if not query:
           return {"data":query}
        
        return {"data":query, "success":True}
        
    def update_address(self,id:int,address:Address, token = Depends(token_auth_scheme)):
        user = AddressBook._get_user(token)

        query = self.db.query(TBAddress).filter(TBAddress.id == id, TBAddress.user_id == user[1]).update({
            
            TBAddress.receiver_name: address.receiver_name,
            TBAddress.mobile_no: address.mobile_no,
            TBAddress.address_line1:address.address_line1,
            TBAddress.address_line2 : address.address_line2,
            TBAddress.city : address.city,
            TBAddress.pincode : address.pincode,
            TBAddress.state : address.state,
            TBAddress.type : address.type,
            })

        self.db.commit()
        if not query:
            return { "message": "address not updated" }

        return { "message": "address successfully updated" }

    def delete_address(self,id:int, token = Depends(token_auth_scheme)):
        user = AddressBook._get_user(token)
        print(user[1])
        
        query = self.db.query(TBAddress).filter(and_(TBAddress.user_id == user[1], TBAddress.id == id))
        result = query.delete()
        self.db.commit()

        if not result:
            return {"message":"address can't removed"}
        
        return {"message":"address removed successfully"}




