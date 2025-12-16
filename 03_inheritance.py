"""
案例 3: 繼承 (Inheritance) 特性詳解
展示如何建立類別層次結構，實現程式碼重用
"""

print("=" * 80)
print("繼承特性：建立層次關係以實現程式碼重用")
print("=" * 80)

# ========== 基礎繼承：DRY 原則 ==========
print("\n【1. 基礎繼承：避免程式碼重複】")

class Mammal:
    """哺乳動物基礎類別（母類別/父類別）"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"✓ 創建哺乳動物：{name}")
    
    def feed(self):
        """餵食方法 - 所有哺乳動物共有的行為"""
        print(f"餵食 {self.name}，提供營養豐富的食物")
    
    def sleep(self):
        """睡覺方法 - 通用行為"""
        print(f"{self.name} 正在睡覺 Zzz...")
    
    def breathe(self):
        """呼吸方法 - 所有哺乳動物都需要呼吸"""
        print(f"{self.name} 正在呼吸")
    
    def get_info(self):
        """獲取基本資訊"""
        return f"{self.__class__.__name__}: {self.name}, {self.age}歲"


class Dog(Mammal):
    """狗類別 - 繼承自 Mammal"""
    
    def bark(self):
        """狗特有的行為：吠叫"""
        print(f"{self.name} 正在吠叫：汪汪汪！")
    
    def fetch(self):
        """狗特有的行為：撿球"""
        print(f"{self.name} 正在撿球")


class Cat(Mammal):
    """貓類別 - 繼承自 Mammal"""
    
    def meow(self):
        """貓特有的行為：貓叫"""
        print(f"{self.name} 正在叫：喵喵喵！")
    
    def scratch(self):
        """貓特有的行為：抓東西"""
        print(f"{self.name} 正在抓沙發")


# 使用繼承
print("\n創建並使用子類別實例：")
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

print("\n狗的行為（包含繼承的和自己的）：")
dog.feed()      # 繼承自 Mammal
dog.sleep()     # 繼承自 Mammal
dog.breathe()   # 繼承自 Mammal
dog.bark()      # Dog 自己的方法
dog.fetch()     # Dog 自己的方法

print("\n貓的行為：")
cat.feed()      # 繼承自 Mammal
cat.meow()      # Cat 自己的方法
cat.scratch()   # Cat 自己的方法

print(f"\n{dog.get_info()}")
print(f"{cat.get_info()}")


# ========== 檢驗繼承關係 ==========
print("\n" + "=" * 80)
print("【2. 檢驗繼承關係】")
print("=" * 80)

print("\n使用 isinstance() 檢查實例類型：")
print(f"dog 是 Dog 的實例嗎？ {isinstance(dog, Dog)}")
print(f"dog 是 Mammal 的實例嗎？ {isinstance(dog, Mammal)}")  # True，因為繼承
print(f"dog 是 Cat 的實例嗎？ {isinstance(dog, Cat)}")

print("\n使用 issubclass() 檢查繼承關係：")
print(f"Dog 是 Mammal 的子類別嗎？ {issubclass(Dog, Mammal)}")
print(f"Cat 是 Mammal 的子類別嗎？ {issubclass(Cat, Mammal)}")
print(f"Dog 是 Cat 的子類別嗎？ {issubclass(Dog, Cat)}")

print("\n查看類別的繼承層次：")
print(f"Dog 的基礎類別：{Dog.__bases__}")
print(f"Cat 的基礎類別：{Cat.__bases__}")
print(f"Dog 的 MRO (Method Resolution Order)：")
for cls in Dog.__mro__:
    print(f"  - {cls}")


# ========== super() 函式的應用 ==========
print("\n" + "=" * 80)
print("【3. super() 函式：擴展父類別功能】")
print("=" * 80)

class AdvancedDog(Mammal):
    """進階狗類別 - 使用 super() 擴展建構器"""
    
    def __init__(self, name, age, breed):
        """
        添加品種屬性，同時保留父類別的初始化邏輯
        :param breed: 狗的品種
        """
        # 調用父類別的 __init__，處理 name 和 age
        super().__init__(name, age)
        # 添加子類別特有的屬性
        self.breed = breed
        print(f"  品種：{breed}")
    
    def get_info(self):
        """
        覆寫父類別的方法，但先調用父類別的實現
        """
        # 獲取父類別的資訊
        base_info = super().get_info()
        # 添加子類別特有的資訊
        return f"{base_info}, 品種：{self.breed}"
    
    def feed(self):
        """
        擴展父類別的餵食方法
        """
        # 先執行父類別的餵食邏輯
        super().feed()
        # 添加子類別特有的邏輯
        print(f"  特別為 {self.breed} 品種準備的食物")


# 使用 super()
print("\n創建進階狗實例：")
golden = AdvancedDog("Max", 5, "黃金獵犬")

print("\n調用被擴展的方法：")
golden.feed()

print("\n獲取完整資訊：")
print(golden.get_info())


# ========== 多層繼承 ==========
print("\n" + "=" * 80)
print("【4. 多層繼承：建立更深的層次結構】")
print("=" * 80)

class ServiceDog(AdvancedDog):
    """服務犬類別 - 繼承自 AdvancedDog"""
    
    def __init__(self, name, age, breed, service_type):
        """
        :param service_type: 服務類型（導盲、搜救等）
        """
        super().__init__(name, age, breed)
        self.service_type = service_type
        print(f"  服務類型：{service_type}")
    
    def work(self):
        """服務犬特有的工作方法"""
        print(f"{self.name} 正在執行 {self.service_type} 任務")
    
    def get_info(self):
        """繼續擴展資訊顯示"""
        base_info = super().get_info()
        return f"{base_info}, 服務類型：{self.service_type}"


# 使用多層繼承
print("\n創建服務犬實例：")
guide_dog = ServiceDog("Lucy", 4, "拉布拉多", "導盲犬")

print("\n服務犬可以使用所有祖先類別的方法：")
guide_dog.breathe()  # 來自 Mammal
guide_dog.feed()     # 來自 AdvancedDog（已擴展）
guide_dog.work()     # 來自 ServiceDog

print("\n完整資訊：")
print(guide_dog.get_info())

print("\n繼承鏈：")
print(f"ServiceDog 是 AdvancedDog 的子類別嗎？ {issubclass(ServiceDog, AdvancedDog)}")
print(f"ServiceDog 是 Mammal 的子類別嗎？ {issubclass(ServiceDog, Mammal)}")
print(f"guide_dog 是 Mammal 的實例嗎？ {isinstance(guide_dog, Mammal)}")


# ========== 方法覆寫 (Method Overriding) ==========
print("\n" + "=" * 80)
print("【5. 方法覆寫：子類別自定義行為】")
print("=" * 80)

class WildDog(Mammal):
    """野狗類別 - 完全覆寫父類別的方法"""
    
    def feed(self):
        """
        完全覆寫父類別的 feed 方法
        不調用 super()，完全自定義行為
        """
        print(f"{self.name} 正在野外狩獵覓食")
    
    def sleep(self):
        """覆寫 sleep 方法"""
        print(f"{self.name} 在洞穴中警覺地休息")


# 使用覆寫
print("\n創建野狗實例：")
wild = WildDog("Shadow", 6)

print("\n野狗的行為（已被覆寫）：")
wild.feed()   # 使用覆寫後的方法
wild.sleep()  # 使用覆寫後的方法
wild.breathe()  # 仍然使用父類別的方法


# ========== 總結 ==========
print("\n" + "=" * 80)
print("繼承特性總結")
print("=" * 80)
print("""
1. 繼承的語法：
   class 子類別(父類別):
       pass

2. 繼承的優勢：
   ✓ 程式碼重用：避免重複編寫相同的程式碼
   ✓ 建立層次：清晰表達「is-a」關係
   ✓ 易於維護：修改父類別會自動影響所有子類別
   ✓ 易於擴展：在不修改原有程式碼的基礎上添加新功能

3. 關鍵概念：
   - isinstance(obj, Class): 檢查物件是否為某類別的實例
   - issubclass(Sub, Parent): 檢查類別繼承關係
   - super(): 調用父類別的方法
   - 方法覆寫: 子類別可以重新定義父類別的方法

4. super() 的兩種用法：
   - 擴展: 先調用父類別方法，再添加新邏輯
   - 覆寫: 不調用 super()，完全自定義行為

5. 多層繼承：
   - 可以建立多層繼承鏈
   - 子類別可以訪問所有祖先類別的方法
   - MRO (Method Resolution Order) 決定方法查找順序

✅ 繼承實踐了 DRY (Don't Repeat Yourself) 原則
""")
