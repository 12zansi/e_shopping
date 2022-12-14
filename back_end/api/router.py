from datetime import date
from typing import Optional
from fastapi import UploadFile,Form, File, APIRouter, Depends, Query
from back_end.Models.brand import Brand
from back_end.Models.cart import OrderItem
from back_end.Models.login import ForgotPassword, Login
from back_end.Models.product import Product, ProductAttribute, ProductDetail
from back_end.Models.address import Address
from back_end.Models.orders import Orders
from back_end.Models.product_return import ProductReturn
from back_end.Models.favorite_list import FavoriteList
from back_end.Models.bank_account import BankAccount
from back_end.Models.register import Register, Verification
from back_end.Models.review import Review
from back_end.Models.status import Status
from back_end.database.connection2 import Base,connection
from back_end.dependencies.admin.brands.brand import AdminBrands
from back_end.dependencies.admin.categories.category import AdminCategories
from back_end.dependencies.admin.dashboard import AdminDashBoad
from back_end.dependencies.admin.orders.get_orders import AdminOrders
from back_end.dependencies.admin.products.product import AdminProducts
from back_end.dependencies.admin.products.product_attributes import AdminProductAttributes
from back_end.dependencies.admin.products.product_images import AdminProductImages
from back_end.dependencies.admin.return_product.get_return_product import AdminReturns
from back_end.dependencies.login import UserLogin
from back_end.dependencies.users.addressbook.addressbook import AddressBook
from back_end.dependencies.users.bank_account.bank_account import UserBankAccount
from back_end.dependencies.users.brand.brand import UserBrand
from back_end.dependencies.users.category.category import UserCategory
from back_end.dependencies.users.checkout.cart import UserCart
from back_end.dependencies.users.checkout.orders import UserOrder
from back_end.dependencies.users.favorite_list.favoritelist import UserFavorite
from back_end.dependencies.users.product.product import UserProduct
from back_end.dependencies.users.user_info.forgot_password import UserForgotPassword
from back_end.dependencies.users.user_info.profile import UserProfile
from back_end.dependencies.users.user_info.register import UsersRegister
from back_end.enum.search import ProductSearch
from fastapi.security import HTTPBearer 

token_auth_scheme = HTTPBearer()

router = APIRouter(prefix="/api/v1")

Base.metadata.create_all(bind = connection)

@router.post('/auth/register', tags = ['auth'])
async def register(user:Register, user_register: UsersRegister = Depends(UsersRegister)):
    
    data = await user_register.register(user)
    return data


@router.post('/auth/otp',tags = ['auth'])
def verify_account(verification:Verification, user_register: UsersRegister = Depends(UsersRegister)):
    data = user_register.verify_otp(verification)
    return data

@router.post('/auth/login', tags = ['auth'])
def login(user:Login, user_login: UserLogin = Depends(UserLogin)):
   data = user_login.login(user)
   return { "token_detail":data,"success": True }

@router.get('/admin/dashboard', tags = ['admin'])
def  get_all_report(token: str = Depends(token_auth_scheme), admin_dashboard: AdminDashBoad = Depends(AdminDashBoad)):
    data = admin_dashboard.count_records(token)
    return { "data": data, "success": True }

@router.get('/admin/product/{search}', tags = ['admin'])
def  get_all_detail(search: ProductSearch, token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.post('/admin/brands', tags = ['admin'])
def add_brand(brand:Brand, token: str = Depends(token_auth_scheme),admin_brand: AdminBrands = Depends(AdminBrands)):
    data = admin_brand.add_brand(brand, token)
    return data 

@router.get('/admin/brands/{id}', tags = ['admin'])
def get_brand(id:int,token: str = Depends(token_auth_scheme),admin_brand: AdminBrands = Depends(AdminBrands)):
    data = admin_brand.get_brand(id, token)
    return data 

@router.put('/admin/brands/{id}', tags = ['admin'])
def update_brand(id:int, brand:Brand,token: str = Depends(token_auth_scheme),admin_brand: AdminBrands = Depends(AdminBrands)):
    data = admin_brand.change_brand(id, brand, token)
    return data 
    

@router.delete('/admin/brands/{id}', tags = ['admin'])
def remove_brand(id:int,token: str = Depends(token_auth_scheme),admin_brand: AdminBrands = Depends(AdminBrands)):
    data = admin_brand.delete_brand(id, token)
    return data 

@router.post('/admin/categories', tags = ['admin'])
def add_category(name: str = Form(...),image: UploadFile = File(...) ,parent_id: str = Form(default=0),token: str = Depends(token_auth_scheme),admin_category: AdminCategories = Depends(AdminCategories)):
    data = admin_category.publish_category(name, image, parent_id, token)
    return data

@router.get('/admin/categories/{id}', tags = ['admin'])
def get_category(id:int,token: str = Depends(token_auth_scheme),admin_category: AdminCategories = Depends(AdminCategories)):
    data = admin_category.view_category(id, token)
    return data

@router.put('/admin/categories/{id}', tags = ['admin'])
def update_category(id:int,name:str = Form(...),image:UploadFile = File(default = None) ,parent_id:str = Form(default=0),token: str = Depends(token_auth_scheme),admin_category: AdminCategories = Depends(AdminCategories)):
    data = admin_category.change_category(id, name, image, parent_id, token)
    return data

@router.delete('/admin/categories/{id}', tags = ['admin'])
def remove_category(id:int, token: str = Depends(token_auth_scheme), admin_category: AdminCategories = Depends(AdminCategories)):
    data = admin_category.delete_category(id, token)
    return data

@router.post('/admin/products', tags = ['admin'])
def add_product(product:Product, token: str = Depends(token_auth_scheme), admin_product: AdminProducts = Depends(AdminProducts)):
    data = admin_product.publish_product(product, token)
    return data

@router.get('/admin/products/{id}', tags = ['admin'])
def get_product(id: int, token: str = Depends(token_auth_scheme), admin_product: AdminProducts = Depends(AdminProducts)):
    data = admin_product.view_product(id, token)
    return data

@router.put('/admin/products/{id}', tags = ['admin'])
def update_product(id:int, product:Product, token: str = Depends(token_auth_scheme), admin_product: AdminProducts = Depends(AdminProducts)):
    data = admin_product.change_product(id,product, token)
    return data

@router.delete('/admin/products/{id}', tags = ['admin'])
def remove_product(id:int,token: str = Depends(token_auth_scheme),admin_product: AdminProducts = Depends(AdminProducts)):
    data = admin_product.delete_product(id, token)
    return data 

@router.post('/admin/products/{id}/images', tags = ['admin'])
def add_images(id: int, image_name: list[UploadFile] = File(...), token: str = Depends(token_auth_scheme), admin_product_images: AdminProductImages = Depends(AdminProductImages)):
    data = admin_product_images.upload_product_images(id, image_name, token)
    return data

@router.get('/admin/products/images/{id}', tags = ['admin'])
def get_images(id: int, token: str = Depends(token_auth_scheme), admin_product_images: AdminProductImages = Depends(AdminProductImages)):
    data = admin_product_images.view_product_images(id, token)
    return data

@router.put('/admin/products/images/{id}', tags = ['admin'])
def update_product_images(id:int, image: UploadFile = File(...),token: str = Depends(token_auth_scheme), admin_product_images: AdminProductImages = Depends(AdminProductImages)):
    data = admin_product_images.change_product_images(id, image, token)
    return data

@router.delete('/admin/products/images/{id}', tags = ['admin'])
def remove_product_images(id:int, token: str = Depends(token_auth_scheme)):

    return { "success": True }

@router.post('/admin/products/{id}/attributes', tags = ['admin'])
def add_attribute(id:int, detail:ProductDetail, token: str = Depends(token_auth_scheme), admin_product_attribute: AdminProductAttributes = Depends(AdminProductAttributes) ):
    data = admin_product_attribute.add_product_attribute(id, detail, token)
    return data

@router.delete('/admin/products/attributes/{id}', tags = ['admin'])
def remove_attribute(id:int, token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.put('/admin/products/attributes/{id}', tags = ['admin'])
def update_product_attribute(id:int, detail:ProductAttribute,token: str = Depends(token_auth_scheme), admin_product_attribute: AdminProductAttributes = Depends(AdminProductAttributes)):
    data = admin_product_attribute.change_product_attribute(id, detail, token)
    return data

@router.get('/admin/products/attributes/{id}', tags = ['admin'])
def get_product_attribute(id:int, token: str = Depends(token_auth_scheme), admin_product_attribute: AdminProductAttributes = Depends(AdminProductAttributes)):
    data = admin_product_attribute.view_product_attribute(id, token)
    return data

@router.get('/admin/products/{id}/detail', tags = ['admin'])
def get_product_detail(id:int, token: str = Depends(token_auth_scheme), admin_product: AdminProducts = Depends(AdminProducts)):
    data = admin_product.view_product_detail(id, token)
    return data

@router.get('/admin/orders/', tags = ['admin'])
def get_orders(start_date:date,end_date:date,status : Optional[str] = None , token: str = Depends(token_auth_scheme), orders : AdminOrders = Depends(AdminOrders)):
    data = orders.view_orders(start_date, end_date, status, token)
    return data

@router.put('/admin/orders/{id}', tags = ['admin'])
def update_order_status(id:int, status: Status , token: str = Depends(token_auth_scheme), orders : AdminOrders = Depends(AdminOrders)):
    data = orders.change_order_status(id, status, token)
    return data

@router.get('/admin/returns', tags = ['admin'])
def get_returned_product(start_date:date,end_date:date,status: Optional[str] = None, token: str = Depends(token_auth_scheme), returns : AdminReturns = Depends(AdminReturns)):
    data = returns.view_returns(start_date, end_date, token)
    return data
                       
@router.put('/admin/returns/{id}', tags = ['admin'])
def update_return_status(id:int, status: Status , token: str = Depends(token_auth_scheme), returns : AdminReturns = Depends(AdminReturns)):
    data = returns.change_returns_status(id, status, token)
    return data

@router.post('/address', tags = ['addressbook'])
def add_address(address: Address,token: str = Depends(token_auth_scheme),addressbook: AddressBook = Depends(AddressBook)):
    data = addressbook.add_address(address, token)
    return data

@router.put('/address/{id}', tags = ['addressbook'])
def update_address(id:int,address: Address,token: str = Depends(token_auth_scheme), addressbook: AddressBook = Depends(AddressBook)):
    data = addressbook.update_address(id,address,token)
    return  data

@router.get('/address/{id}', tags = ['addressbook'])
def get_address(id:int, token: str = Depends(token_auth_scheme), addressbook: AddressBook = Depends(AddressBook)):
    data = addressbook.get_address(id,token)
    return  data

@router.delete('/address/{id}', tags = ['addressbook'])
def remove_address(id:int,token: str = Depends(token_auth_scheme), addressbook: AddressBook = Depends(AddressBook)):
    data = addressbook.delete_address(id,token)
    return data


@router.post('/users/forgotpassword', tags = ['users'])
async def forgot_password(user: ForgotPassword,user_password:UserForgotPassword = Depends(UserForgotPassword)):
    data = await user_password.change_password(user)
    return data

@router.post('/users/verification', tags = ['users'])
def verify_change_password_otp(verification: Verification,user_password:UserForgotPassword = Depends(UserForgotPassword)):
    data = user_password.verify_otp(verification)
    return data

@router.get('/profile', tags = ['users'])
def get_user_profile(token: str = Depends(token_auth_scheme), profile: UserProfile = Depends(UserProfile)):
    data = profile.get_profile(token)
    return {"data": data, "success": True}


@router.post('/favoritelist', tags = ['favoritelist'])
def add_into_favorite_list(favorite_list:FavoriteList,token: str = Depends(token_auth_scheme), user_favorite: UserFavorite = Depends(UserFavorite)):
    data = user_favorite.add_into_favorite_list(favorite_list,token)
    return  data 

@router.get('/favoritelist', tags = ['favoritelist'])
def view_favorite_products(token: str = Depends(token_auth_scheme), user_favorite: UserFavorite = Depends(UserFavorite)):
    data = user_favorite.get_favorite_list(token)
    return { "data":data,"success": True }

@router.delete('/favoritelist/{id}', tags = ['favoritelist'])
def remove_from_favorite_list(id:int,token: str = Depends(token_auth_scheme), user_favorite: UserFavorite = Depends(UserFavorite)):
    data = user_favorite.delete_into_favorite_list(id,token)
    return  data 


@router.post('/bank/accounts', tags = ['accounts'])
def add_bank_account_detail(account: BankAccount,token: str = Depends(token_auth_scheme), bank: UserBankAccount = Depends(UserBankAccount)):
    data = bank.add_bank_account(account, token)
    return data

@router.put('/bank/accounts/{id}', tags = ['accounts'])
def update_bank_account_detail(id:int, bank_account:BankAccount,token: str = Depends(token_auth_scheme), bank: UserBankAccount = Depends(UserBankAccount)):
    data = bank.change_bank_account(id, bank_account, token)
    return data

@router.get('/bank/accounts/{id}', tags = ['accounts'])
def view_bank_account_detail(id:int,token: str = Depends(token_auth_scheme), bank: UserBankAccount = Depends(UserBankAccount)):
    data = bank.view_bank_account(id, token)
    return data

@router.get('/categories/{id}', tags = ['categories'])
def view_category(id : int, user_category: UserCategory = Depends(UserCategory)):
    data = user_category.get_category(id)
    return data

@router.get('/categories/{id}/child', tags = ['categories'])
def view_child_category(id:int, user_category: UserCategory = Depends(UserCategory)):
    data = user_category.get_child_category(id)
    return data

@router.get('/brands/{id}', tags = ['brands'])
def view_brand(id:int, user_brand: UserBrand = Depends(UserBrand)):
    data = user_brand.get_brand(id)
    return data

@router.get('/products/search', tags = ['products'])
def view_products(q: str, search: UserProduct = Depends(UserProduct)):
    data = search.search_product(q)
    return { "data":data,"success": True }

@router.get('/products/{id}', tags = ['products'])
def view_product_detail(id:int, user_product: UserProduct = Depends(UserProduct)):
    data = user_product.get_product_detail(id)
    return data

@router.post('/products/{id}/review', tags = ['products'])
def add_review(id:int, product:Review,token: str = Depends(token_auth_scheme)):
    return { "success": True }

@router.get('/products/{id}/review', tags = ['products'])
def get_review(id:int):
    return True

@router.post('/carts', tags = ['carts'])
def add_into_cart(user:OrderItem,token: str = Depends(token_auth_scheme), cart: UserCart = Depends(UserCart)):
    data = cart.add_in_cart(user,token)
    return data

@router.get('/carts', tags = ['carts'])
def view_cart(token: str = Depends(token_auth_scheme), cart: UserCart = Depends(UserCart)):
   data = cart.get_cart_item(token)
   return data

@router.put('/carts/{id}', tags = ['carts'])
def update_quantity(id:int,quantity: int = Query(default = 1, gt = 0, lt = 5),token: str = Depends(token_auth_scheme), cart: UserCart = Depends(UserCart)):
    data = cart.update_cart_item(id, quantity, token)
    return data
    

@router.delete('/carts/{id}', tags = ['carts'])
def remove_item(id: Optional[int] = None, token: str = Depends(token_auth_scheme), cart: UserCart = Depends(UserCart)):
    data = cart.delete_cart_item(id, token)
    return data


@router.post('/orders', tags = ['orders'])
def place_an_order(user:Orders, token: str = Depends(token_auth_scheme), user_order : UserOrder = Depends(UserOrder)):
   data = user_order.add_in_place_order(user,token)
   return data

@router.post('/orders/{id}/cancel', tags = ['orders'])
def cancel_order(id:int,token: str = Depends(token_auth_scheme)):
    return {"success": True}

@router.get('/orders/{id}', tags = ['orders'])
def get_order_detail(id:int , token: str = Depends(token_auth_scheme), user_order : UserOrder = Depends(UserOrder)):
    data = user_order.get_order_detail(id, token)
    return data

@router.post('/orders/{id}/items/{item_id}/return', tags = ['orders'])
def create_return_request(id:int,item_id:int,product:ProductReturn,token: str = Depends(token_auth_scheme)):
    return { "success": True }





