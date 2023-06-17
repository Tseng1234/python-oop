# main.py

from shape_factory import ShapeFactory

# 創建簡單工廠實例
factory = ShapeFactory()

# 根據用戶輸入創建圖形
shape_type = input("Enter shape type (rectangle/circle): ")
shape = factory.create_shape(shape_type)

# 使用創建的圖形
shape.draw()
