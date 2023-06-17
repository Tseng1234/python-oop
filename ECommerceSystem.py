class Product:
    def __init__(self,name,price,quantity) :
        self.name=name
        self.price=float(price)
        self.quantity=int(quantity)
class EcommerceSystem:
    def __init__(self):
        self.products=[]
        self.cart=[]
    def add_product(self,name,price,quantity):
        product=Product(name,price,quantity)
        self.products.append(product)
    def display(self):
        for product in self.products:
            print("Name: ",product.name)
            print("Price: ",product.price)
            print("quantity: ",product.quantity)
            print("----------------------------")
    def add_to_cart(self,name,quantity):
        for product in self.products:
            if product.name==name:
                product.quantity-=quantity
                self.cart.append(product)
    def display_cart(self):
        for product in self.cart:
            print("Name: ",product.name)
            print("Price: ",product.price)
            print("quantity: ",product.quantity)
            print("----------------------------")
    def checkout(self):
        total_price=0
        for product in self.cart:
            total_price+=product.price*product.quantity
        self.cart=[]
        print("total price: ",total_price)

# 建立電子商務系統
ecommerce = EcommerceSystem()

# 添加商品
ecommerce.add_product("iPhone", 999, 10)
ecommerce.add_product("iPad", 799, 5)
ecommerce.add_product("MacBook", 1999, 3)

# 顯示所有商品
ecommerce.display()

# 將商品添加到購物車
ecommerce.add_to_cart("iPhone", 2)
ecommerce.add_to_cart("MacBook", 1)

# 顯示購物車內容
ecommerce.display_cart()

# 結帳並顯示總價格
ecommerce.checkout()
