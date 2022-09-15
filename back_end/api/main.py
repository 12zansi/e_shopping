from datetime import date
from typing import Optional
from fastapi import FastAPI, UploadFile,Form, File, APIRouter, Depends, Query
from back_end.Models.brand import Brand
from back_end.Models.cart import OrderItem
from back_end.Models.login import ForgotPassword, Login
from back_end.Models.product import Product, ProductDetail
from back_end.Models.address import Address
from back_end.Models.orders import Orders
from back_end.Models.product_return import ProductReturn
from back_end.Models.favorite_list import FavoriteList
from back_end.Models.bank_account import BankAccount
from back_end.Models.register import Register
from back_end.Models.review import Review
from back_end.dependencies.login import UserLogin
from back_end.dependencies.users.addressbook.addressbook import AddressBook
from back_end.dependencies.users.user_info.profile import UserProfile
from back_end.dependencies.users.user_info.register import UsersRegister
from back_end.enum.order_status import OrderStatus
from back_end.enum.return_status import ReturnStatus
from back_end.enum.search import ProductSearch
from fastapi.security import HTTPBearer 


token_auth_scheme = HTTPBearer()


router = APIRouter(prefix="/api/v1")


@router.post('/auth/register', tags = ['auth'])
def register(user:Register, user_register: UsersRegister = Depends(UsersRegister)):
    data = user_register.register(user)
    return { "data":data }

@router.post('/auth/login', tags = ['auth'])
def login(user:Login, user_login: UserLogin = Depends(UserLogin)):
   data = user_login.login(user)
   return { "token_detail":data,"success": True }

@router.get('/admin/dashboard', tags = ['admin'])
def  get_all_report(token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/products/{search}', tags = ['admin'])
def  get_all_detail(search: ProductSearch,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.post('/admin/brands', tags = ['admin'])
def add_brand(brand:Brand,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/brands/{id}', tags = ['admin'])
def get_brand(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/brands/{id}', tags = ['admin'])
def update_brand(id:int, brand:Brand,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.delete('/admin/brands/{id}', tags = ['admin'])
def remove_brand(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.post('/admin/categories', tags = ['admin'])
def add_category(name:str = Form(...),image:UploadFile = File(...) ,parent_id:str = Form(default=0),token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/categories/{id}', tags = ['admin'])
def get_category(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/categories/{id}', tags = ['admin'])
def update_category(id:int,name:str = Form(...),image:UploadFile = File(...) ,parent_id:str = Form(default=0),token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.delete('/admin/categories/{id}', tags = ['admin'])
def remove_category(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.post('/admin/products', tags = ['admin'])
def add_product(product:Product,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/products/{id}', tags = ['admin'])
def update_product(id:int, product:Product,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.post('/admin/products/{id}/images', tags = ['admin'])
def add_images( id: int, image: list[UploadFile] = File(...),token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/products/images/{id}', tags = ['admin'])
def get_images( id: int, token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/products/images/{id}', tags = ['admin'])
def update_product_images(id:int, image: UploadFile = File(...),token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.delete('/admin/products/images/{id}', tags = ['admin'])
def remove_product_images(id:int, token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.post('/admin/products/{id}/attributes', tags = ['admin'])
def add_attribute(id:int, detail:ProductDetail, token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.delete('/admin/products/attributes/{id}', tags = ['admin'])
def remove_attribute(id:int, token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/products/attributes/{id}', tags = ['admin'])
def update_product_attribute(id:int, detail:ProductDetail,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/products/attributes/{id}', tags = ['admin'])
def view_product_attribute(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/products/{id}/detail', tags = ['admin'])
def view_product_detail(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/orders/', tags = ['admin'])
def view_orders(start_date:date,end_date:date,status:OrderStatus,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/orders/{id}', tags = ['admin'])
def change_order_status(id:int, status:OrderStatus,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/admin/returns', tags = ['admin'])
def view_returned_product(start_date:date,end_date:date, token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/returns/{id}', tags = ['admin'])
def change_return_status(id:int, status: ReturnStatus, token: str = Depends(token_auth_scheme)):
    return { "success": True }


@router.post('/address', tags = ['addressbook'])
def add_address(address: Address,token: str = Depends(token_auth_scheme),addressbook: AddressBook = Depends(AddressBook)):
    data = addressbook.add_address(address, token)
    return { "data": data,"success": True }

@router.put('/address/{id}', tags = ['addressbook'])
def update_address(id:int,address: Address,token: str = Depends(token_auth_scheme), addressbook: AddressBook = Depends(AddressBook)):
    data = addressbook.update_address(id,address,token)
    return { "data": data,"success": True }

@router.get('/address', tags = ['addressbook'])
def get_address(token: str = Depends(token_auth_scheme), addressbook: AddressBook = Depends(AddressBook)):
    data = addressbook.get_address(token)
    return { "data": data, "success": True }

@router.delete('/address/{id}', tags = ['addressbook'])
def remove_address(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }


@router.post('/users/forgotpassword', tags = ['users'])
def forgot_password(user: ForgotPassword):
    return { "success": True }

@router.get('/profile', tags = ['users'])
def get_user_profile(token: str = Depends(token_auth_scheme), profile: UserProfile = Depends(UserProfile)):
    data = profile.get_profile(token)
    return {"data": data, "success": True}


@router.post('/favoritelist', tags = ['favoritelist'])
def add_into_favorite_list(favoritelist: FavoriteList,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/favoritelist', tags = ['favoritelist'])
def view_favorite_products(token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.delete('/favoritelist/{id}', tags = ['favoritelist'])
def remove_from_favorite_list(id:int,token: str = Depends(token_auth_scheme)):
    return { "success": True }


@router.post('/bank/accounts', tags = ['accounts'])
def add_bank_account_detail(bank_account: BankAccount,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/bank/accounts/{id}', tags = ['accounts'])
def update_bank_account_detail(id:int,bank_account:BankAccount,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/bank/accounts', tags = ['accounts'])
def view_bank_account_detail(token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/categories/{id}', tags = ['categories'])
def view_category(id : int):
    return { "success": True }

@router.get('/categories/{id}/child', tags = ['categories'])
def view_child_category(id:int):
    return { "success": True }

@router.get('/brands/{id}', tags = ['brands'])
def view_brand(id:int):
    return { "success": True }


@router.get('/products/search', tags = ['products'])
def view_products(q: str):
    return { "success": True }

@router.get('/products/{id}', tags = ['products'])
def view_product_detail(id:int):
    return { "success": True }

@router.post('/products/{id}/review', tags = ['products'])
def add_review(id:int, product:Review,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/products/{id}/review', tags = ['products'])
def get_review(id:int):
    return { "success": True }

@router.post('/carts', tags = ['carts'])
def add_into_cart(user:OrderItem,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/carts', tags = ['carts'])
def view_cart(token: str = Depends(token_auth_scheme)):
   return { "success": True }

@router.put('/carts/{id}', tags = ['carts'])
def update_quantity(id:int,quantity: int = Query(default = 1, gt = 0),token: str = Depends(token_auth_scheme)):
  
    return { "success": True }
    

@router.delete('/carts/{id}', tags = ['carts'])
def remove_item(id: Optional[int] = None, token: str = Depends(token_auth_scheme)):
    return { "success": True }


@router.post('/orders', tags = ['orders'])
def place_an_order(user:Orders, token: str = Depends(token_auth_scheme)):
   return {"success": True}

@router.post('/orders/{id}/cancel', tags = ['orders'])
def cancel_order(id:int,token: str = Depends(token_auth_scheme)):
    return {"success": True}

@router.get('/orders', tags = ['orders'])
def get_order_detail(id:Optional[int] = None , token: str = Depends(token_auth_scheme)):
    return {"success": True}

@router.post('/orders/{id}/items/{item_id}/return', tags = ['orders'])
def create_return_request(id:int,item_id:int,product:ProductReturn,token: str = Depends(token_auth_scheme)):
    return { "success": True }

app = FastAPI(
    title="e-Shopping",
    description="This is online shopping site for customer."
   
)
app.include_router(router)


