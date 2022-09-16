from fastapi import Depends
from back_end.Models.address import Address
from back_end.database.connection import cursor, connection
from back_end.database.mysql.address import TBAddress
from back_end.dependencies.login import UserLogin,token_auth_scheme

class AddressBook(UserLogin):
    
    def add_address(self,address:Address, token = Depends(token_auth_scheme)):
        username, user_id = AddressBook._get_user(token)
        print(user_id)
        query = """SELECT * FROM address WHERE address_line1 = %s AND user_id = %s"""
        value = (address.address_line1,user_id)
        cursor.execute(query, value)
        result = cursor.fetchone()
        if result:
            return "address already added"
        query = """INSERT INTO address (receiver_name,mobile_no,address_line1,address_line2,city,pincode,state,type,user_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = ( 
                address.receiver_name,
                address.mobile_no,
                address.address_line1,
                address.address_line2,
                address.city,
                address.pincode,
                address.state,
                address.type,
                user_id
                )

        cursor.execute(query, val)
        connection.commit()

        return "record inserted successfully"

    def get_address(self, token = Depends(token_auth_scheme)):
        username, user_id = AddressBook._get_user(token)
    
        query = """SELECT * FROM address WHERE user_id = %s"""
        cursor.execute(query,(user_id, ))
        result = cursor.fetchall()   
        
        address_list = []
        for i in result:
           address = TBAddress()
           address.id = i[0]
           address.receiver_name = i[1]
           address.mobile_no = i[2]
           address.address_line1 = i[3]
           address.address_line2 = i[4]
           address.city = i[5]
           address.pincode = i[6]
           address.state = i[7]
           print(address)
           address_list.append(address)
           
        return address_list
        
    def update_address(self,id:int,address:Address, token = Depends(token_auth_scheme)):
    
        sql = "UPDATE address SET  receiver_name = %s, mobile_no = %s, address_line1 = %s, address_line2 = %s, city = %s, pincode = %s,state = %s,type = %s WHERE id = %s"
        val = ( address.receiver_name,
                address.mobile_no,
                address.address_line1,
                address.address_line2,
                address.city,
                address.pincode,
                address.state,
                address.type,
                id 
              )

        cursor.execute(sql, val)

        connection.commit()

        return "update record successfully"




