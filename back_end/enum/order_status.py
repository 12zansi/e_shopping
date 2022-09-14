from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
    ONTHEWAY = "On the way"
    DELIVERED = "Delivered"

