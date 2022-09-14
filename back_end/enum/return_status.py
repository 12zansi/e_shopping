from enum import Enum


class ReturnStatus(str, Enum):
    PENDING = "Pending"
    CANCELLED = "Cancelled"
    REJECTED = "Rejected"
    RECEIVED = "Received"
    RESTOCKED = "Restocked"
    CLOSED = "Closed"