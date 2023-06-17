import numpy as np
class Singleton:
    __instance = None  # 保存唯一的實例

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("單例類已存在，請使用 get_instance() 方法獲取實例。")
        else:
            Singleton.__instance = self

# 測試
instance1 = Singleton.get_instance()
instance2 = Singleton.get_instance()

print(instance1 is instance2)  # True，兩個變數引用相同的實例
