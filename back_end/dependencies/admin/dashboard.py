from back_end.database.mysql.dashboard import DashBoard
from back_end.database.session import start_session
from fastapi import Depends
from sqlalchemy import and_
from requests import Session

from back_end.database.tables.tb_brand import TBBrands
from back_end.database.tables.tb_category import TBCategories
from back_end.database.tables.tb_order import TBPlaceOrders
from back_end.database.tables.tb_product import TBProducts
from back_end.database.tables.tb_users import TBUsers
from back_end.dependencies.login import UserLogin, token_auth_scheme

class AdminDashBoad(UserLogin):
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   
    
    def orders_status_wise(self, status_id):
        total_records = self.db.query(TBPlaceOrders).filter().count()

    def count_records(self, token: str = Depends(token_auth_scheme)):
        total_brands = self.db.query(TBBrands).count()

        total_categories = self.db.query(TBCategories).filter(TBCategories.parent_id == 0).count()

        total_products = self.db.query(TBProducts).count()

        total_orders = self.db.query(TBPlaceOrders).count()

        total_customers = self.db.query(TBUsers).filter(TBUsers.is_admin == 0).count()
        

        total_records = DashBoard()
        total_records.total_customers = total_customers
        total_records.total_brands = total_brands
        total_records.total_categories = total_categories
        total_records.total_products = total_products
        total_records.total_orders = total_orders
         
        return total_records
