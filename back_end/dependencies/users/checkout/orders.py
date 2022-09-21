from back_end.database.mysql.order_detail import UserOrderDetail, UserOrderItems
from back_end.database.tables.tb_address import TBAddress
from back_end.database.tables.tb_cart import TBCarts
from back_end.database.tables.tb_order import TBPlaceOrders
from fastapi import Depends
from sqlalchemy import and_
from back_end.Models.orders import Orders
from back_end.database.tables.tb_order_item import TBOrderItems
from back_end.database.tables.tb_status import TBStatus
from back_end.dependencies.add_into_table import AddIntoTable
from back_end.dependencies.login import UserLogin, token_auth_scheme


class UserOrder(UserLogin, AddIntoTable):

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    def add_in_place_order(self, cart: Orders, token:str = Depends(token_auth_scheme)):
        user = UserOrder._get_user(token)
    
        query  = self.db.query(TBOrderItems).filter(and_(TBOrderItems.user_id == user[1]),TBOrderItems.order_id == None).all()
        total = 0
        if query:
            for data in query:
                total += data.product_price*data.quantity
                
            order_query = TBPlaceOrders(
                total_price = total, 
                address_id = cart.address_id,
                user_id = user[1]
            )
            UserOrder._add_in_table(self,order_query)

            self.db.query(TBOrderItems).filter(and_(TBOrderItems.user_id == user[1]),TBOrderItems.order_id == None)\
                .update({TBOrderItems.order_id: order_query.id })
            self.db.commit()
            
            self.db.query(TBCarts.id).filter(TBCarts.user_id == user[1])\
            .update({TBCarts.status_id: 2})
            self.db.commit()

            return { "data": order_query }
            

        return { "message": "Order already Placed"}

    def get_order_detail(self, id: int, token: str = Depends(token_auth_scheme)):
        user = UserOrder._get_user(token)
    
        query = self.db.query(TBPlaceOrders.id, TBPlaceOrders.order_date, TBPlaceOrders.total_price\
            ,TBAddress.address_line1, TBAddress.address_line2, TBAddress.city, TBAddress.pincode, TBAddress.state, TBAddress.receiver_name\
            ,TBOrderItems.id, TBOrderItems.product_name, TBOrderItems.product_price, TBOrderItems.quantity, TBOrderItems.image_name, TBStatus.description)\
            .join(TBOrderItems, TBPlaceOrders.id == TBOrderItems.order_id)\
            .join(TBStatus, TBStatus.id == TBOrderItems.status_id)\
            .join(TBAddress, TBAddress.id == TBPlaceOrders.address_id)\
            .filter(TBPlaceOrders.id == id, TBPlaceOrders.user_id == user[1]).all()
        
        order_items_list = []
        if not query:

           return  { "message": 'Order not found' }


        for i in query:
  
            order = UserOrderDetail()
            order.id = i[0]
            order.order_date = i[1].date()
            order.total_price = i[2]
            order.shipping_address = i[3] + ', '+ i[4] + ',' + i[5] + ',' + i[6] + ', ' + i[7]
            order.receiver_name = i[8]

            order_item = UserOrderItems()
            order_item.id = i[9]
            order_item.product_name = i[10]
            order_item.quantity = i[12]
            order_item.price = i[11]
            order_item.image_name = i[13]
            order_item.status = i[14]

            
            order_items_list.append(order_item)

        order.order_items = order_items_list

        return { "data": order, "success": True}

