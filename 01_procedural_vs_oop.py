"""
案例 1: 過程式編程 vs 物件導向編程
展示從混亂的過程式程式碼到結構化 OOP 的轉變
"""

print("=" * 80)
print("過程式編程範例：混亂且難以維護")
print("=" * 80)

# ========== 過程式風格 (Procedural Style) ==========
# 所有數據都分散定義
lion_name = "Simba"
lion_food = "肉類"
lion_fur_color = "金色"
lion_age = 5

parrot_name = "Polly"
parrot_food = "種子"
parrot_feather_color = "綠色"
parrot_age = 2

shark_name = "Jaws"
shark_food = "魚類"
shark_fin_type = "背鰭"
shark_age = 10

# 大量的 if-else 判斷邏輯，數據與邏輯分離
def make_sound(animal_type):
    """根據動物類型發出聲音 - 充滿 if-else 判斷"""
    if animal_type == "lion":
        return "吼叫！"
    elif animal_type == "parrot":
        return "嘎嘎叫！"
    elif animal_type == "shark":
        return "無聲"
    else:
        return "未知聲音"

def feed_animal(animal_type):
    """餵食動物 - 又是一堆 if-else"""
    if animal_type == "lion":
        print(f"餵食 {lion_name}：{lion_food}")
    elif animal_type == "parrot":
        print(f"餵食 {parrot_name}：{parrot_food}")
    elif animal_type == "shark":
        print(f"餵食 {shark_name}：{shark_food}")

def show_info(animal_type):
    """顯示動物資訊 - 持續的重複判斷"""
    if animal_type == "lion":
        print(f"獅子 {lion_name}，年齡 {lion_age}，毛色 {lion_fur_color}")
    elif animal_type == "parrot":
        print(f"鸚鵡 {parrot_name}，年齡 {parrot_age}，羽毛 {parrot_feather_color}")
    elif animal_type == "shark":
        print(f"鯊魚 {shark_name}，年齡 {shark_age}，鰭型 {shark_fin_type}")

# 使用過程式風格
print("\n過程式風格的使用方式：")
show_info("lion")
print(f"聲音：{make_sound('lion')}")
feed_animal("lion")

print()
show_info("parrot")
print(f"聲音：{make_sound('parrot')}")

print("\n⚠️ 問題點：")
print("1. 數據（屬性）與邏輯（方法）分離")
print("2. 充滿 if-else 判斷，新增動物類型需要修改多處")
print("3. 程式碼冗餘，難以維護")
print("4. 缺乏結構，隨著複雜度增加會變得越來越混亂")


print("\n" + "=" * 80)
print("物件導向編程範例：結構清晰且易於擴展")
print("=" * 80)

# ========== 物件導向風格 (OOP Style) ==========

class Animal:
    """動物基礎類別"""
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food
    
    def show_info(self):
        """顯示基本資訊 - 每個類別負責自己的顯示邏輯"""
        return f"{self.__class__.__name__} {self.name}，年齡 {self.age}"
    
    def feed(self):
        """餵食 - 封裝在物件內"""
        print(f"餵食 {self.name}：{self.food}")
    
    def make_sound(self):
        """發出聲音 - 多型，子類別可以覆寫"""
        return "動物的聲音"


class Lion(Animal):
    """獅子類別 - 繼承自 Animal"""
    def __init__(self, name, age, food, fur_color):
        super().__init__(name, age, food)
        self.fur_color = fur_color
    
    def show_info(self):
        """覆寫父類方法，添加獅子特有資訊"""
        base_info = super().show_info()
        return f"{base_info}，毛色 {self.fur_color}"
    
    def make_sound(self):
        """獅子特有的聲音"""
        return "吼叫！"


class Parrot(Animal):
    """鸚鵡類別 - 繼承自 Animal"""
    def __init__(self, name, age, food, feather_color):
        super().__init__(name, age, food)
        self.feather_color = feather_color
    
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}，羽毛 {self.feather_color}"
    
    def make_sound(self):
        """鸚鵡特有的聲音"""
        return "嘎嘎叫！"


class Shark(Animal):
    """鯊魚類別 - 繼承自 Animal"""
    def __init__(self, name, age, food, fin_type):
        super().__init__(name, age, food)
        self.fin_type = fin_type
    
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}，鰭型 {self.fin_type}"
    
    def make_sound(self):
        """鯊魚沒有聲音"""
        return "無聲"


# 使用物件導向風格
print("\nOOP 風格的使用方式：")
simba = Lion("Simba", 5, "肉類", "金色")
polly = Parrot("Polly", 2, "種子", "綠色")
jaws = Shark("Jaws", 10, "魚類", "背鰭")

# 將所有動物放入列表 - 體現多型的威力
animals = [simba, polly, jaws]

# 無需 if-else，統一的介面處理不同類型的動物
for animal in animals:
    print(animal.show_info())
    print(f"聲音：{animal.make_sound()}")
    animal.feed()
    print()

print("✅ 優勢：")
print("1. 數據與邏輯封裝在一起，每個類別職責明確")
print("2. 無需 if-else，新增動物只需創建新類別")
print("3. 通過繼承重用程式碼，遵循 DRY 原則")
print("4. 多型讓不同類型的物件可以用統一的方式處理")
print("5. 結構清晰，易於維護和擴展")

print("\n" + "=" * 80)
print("對比總結：OOP 將「散文」變成「結構化的議論文」")
print("=" * 80)
