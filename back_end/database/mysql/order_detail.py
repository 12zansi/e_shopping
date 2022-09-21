from datetime import date

class UserOrderItems:
    id: int
    product_name: str
    image_name: str
    price: int
    quantity: int
    status: str

class UserOrderDetail:
     id: int
     receiver_name: str
     order_date: date
     shipping_address: str
     mobile_no: str
     total_price: int
     order_items: list[UserOrderItems]