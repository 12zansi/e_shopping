from back_end.database.connection import cursor
# from back_end.database.mysql.product import TBProduct

class UserProduct:

    def search_product(self,q: str):
        
        query = """SELECT product.id, product.name, product.price, product.mrp, product.return_policy_in_days, category.name, brand.name
            FROM product \
            LEFT JOIN category ON category.id = product.category_id \
            LEFT JOIN brand ON brand.id = product.brand_id and \
            product.name = %s or category.name = %s or brand.name = %s
            """
        cursor.execute(query,(q, q, q))
        result = cursor.fetchall()
        data_list = []
        # for data in result:
        #     product = TBProduct()
        #     product.id = data[0]
        #     product.name = data[1]
        #     product.mrp = data[3]
        #     product.price = data[2]
        #     product.category_name = data[5]
        #     product.brand_name = data[6]
        #     product.return_policy_in_days = data[4]
        #     data_list.append(product)
        return data_list

