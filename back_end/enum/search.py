from enum import Enum


class ProductSearch(str, Enum):
    BRAND = "brand"
    CATEGORY = "category"
    PRODUCT = "product"
