from typing import Optional,Union
from fastapi import FastAPI



app = FastAPI(
    title="e-Shopping",
    description="This is online shopping site for customer."
)

@app.post('/api/auth/register', tags = ['auth'])
def register():
    return { "success": True }

@app.post('/api/auth/login', tags = ['auth'])
def login():
   return { "success": True }

@app.get('/api/admin/dashboard', tags = ['admin'])
def  get_all_report():
    return { "success": True }

@app.get('/api/admin/{search}', tags = ['admin'])
def  get_all_detail(search: str):
    return { "success": True }

@app.post('/api/admin/brand', tags = ['admin'])
def add_brand():
    return { "success": True }

@app.put('/api/admin/brand', tags = ['admin'])
def update_brand():
    return { "success": True }

@app.post('/api/admin/category', tags = ['admin'])
def add_category():
    return { "success": True }

@app.put('/api/admin/category', tags = ['admin'])
def update_category():
    return { "success": True }

@app.post('/api/admin/product', tags = ['admin'])
def add_product():
    return { "success": True }

@app.put('/api/admin/product', tags = ['admin'])
def update_product():
    return { "success": True }

@app.post('/api/admin/product/images', tags = ['admin'])
def add_images():
    return { "success": True }

@app.put('/api/admin/product/images', tags = ['admin'])
def update_images():
    return { "success": True }

@app.post('/api/admin/product/detail', tags = ['admin'])
def add_detail():
    return { "success": True }

@app.put('/api/admin/product/detail', tags = ['admin'])
def update_detail():
    return { "success": True }

@app.get('/api/admin/product/detail', tags = ['admin'])
def veiw_product_detail():
    return { "success": True }

@app.get('/api/admin/orders', tags = ['admin'])
def view_orders():
    return { "success": True }

@app.post('/api/admin/orders/status', tags = ['admin'])
def change_order_status():
    return { "success": True }

@app.get('/api/admin/product/return', tags = ['admin'])
def view_returned_product():
    return { "success": True }

@app.post('/api/admin/return/status', tags = ['admin'])
def change_return_status():
    return { "success": True }

@app.get('/api/admin/product/review', tags = ['admin'])
def view_product_review():
    return { "success": True }

@app.post('/api/address', tags = ['addressbook'])
def add_address():
    return { "success": True }

@app.put('/api/address', tags = ['addressbook'])
def update_address():
    return { "success": True }

@app.get('/api/address', tags = ['addressbook'])
def get_address():
    return { "success": True }

@app.delete('/api/address', tags = ['addressbook'])
def remove_address():
    return { "success": True }

@app.post('/api/user/forgotpassword', tags = ['user'])
def forgot_password():
    return { "success": True }

@app.post('/api/favoritelist', tags = ['user'])
def add_into_favorite_list():
    return { "success": True }

@app.get('/api/favoritelist', tags = ['user'])
def view_favorite_products():
    return { "success": True }

@app.delete('/api/favoritelist', tags = ['user'])
def remove_from_favorite_list(product_id:int):
    return { "success": True }

@app.post('/api/user/bank/account', tags = ['user'])
def add_bank_account_detail():
    return { "success": True }

@app.put('/api/user/bank/account', tags = ['user'])
def update_bank_account_detail():
    return { "success": True }

@app.get('/api/user/bank/account', tags = ['user'])
def add_bank_account_detail():
    return { "success": True }

@app.get('/api/user/return', tags = ['user'])
def get_returned_product():
    return {"success": True}

@app.get('/api/category', tags = ['category'])
def view_category():
    return {"success": True}

@app.get('/api/category/{root_category_id}', tags = ['category'])
def view_child_category(root_category_id:int):
    return {"success": True}

@app.get('/api/category/{child_category_id}', tags = ['category'])
def view_parent_category(child_category_id:int):
    return {"success": True}

@app.get('/api/brand', tags = ['brand'])
def view_brand():
    return {"success": True}

@app.get('/api/product/{product_id}', tags = ['product'])
def view_product_detail(product_id:int):
    return {"success": True}

@app.get('/api/product', tags = ['product'])
def view_all_product(product_id:int):
    return {"success": True}

@app.get('/api/search', tags = ['product'])
def view_product(q: Union[str, None] = None):
    return {"success": True}

@app.get('/api/product/price', tags = ['product'])
def filter_product_price_wise(min:int, max:int):
    return {"success": True}

@app.post('/api/product/{product_id}/review', tags = ['product'])
def add_review(product_id:int):
    return {"success": True}

@app.get('/api/product/{product_id}/review', tags = ['product'])
def get_review(product_id:int):
    return {"success": True}

@app.post('/api/product/return', tags = ['product'])
def create_return_request():
    return {"success": True}


@app.post('/api/cart', tags = ['cart'])
def add_into_cart():
    return {"success": True}

@app.post('/api/order', tags = ['orders'])
def place_an_order():
   return {"success": True}

@app.get('/api/cart', tags = ['cart'])
def view_cart():
   return {"success": True}

@app.put('/api/cart', tags = ['cart'])
def update_quantity():
    return {"success": True}

@app.delete('/api/cart', tags = ['cart'])
def remove_item(item_id: Optional[int] = None):
    return {"success": True}


@app.post('/api/orders/{order_id}/cancel', tags = ['orders'])
def cancel_order(order_id:int):
    return {"success": True}

@app.get('/api/user/order', tags = ['user'])
def get_order_detail(order_id:Optional[int] = None):
    return {"success": True}



