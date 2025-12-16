"""
案例 5: 綜合實戰 - 動物園管理系統
整合封裝、繼承與多型三大特性的完整應用
"""

from datetime import datetime
from typing import List, Optional

print("=" * 80)
print("綜合實戰案例：動物園管理系統")
print("整合 OOP 三大特性：封裝、繼承、多型")
print("=" * 80)


# ========== 基礎類別層次 ==========

class Animal:
    """
    動物基礎類別
    展示：封裝（數據與方法打包）
    """
    # 類別變數：所有實例共享
    total_animals = 0
    
    def __init__(self, name: str, species: str, age: int, weight: float):
        """
        建構器：初始化動物基本屬性
        展示：封裝特性
        """
        # 實例變數（私有）
        self.__name = name
        self.__species = species
        self.__age = age
        self.__weight = weight
        self.__health_status = "健康"
        self.__last_checkup = None
        
        # 增加動物總數
        Animal.total_animals += 1
        print(f"✓ 新增動物：{species} - {name}")
    
    # 使用 @property 提供受控的屬性訪問
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def species(self) -> str:
        return self.__species
    
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("年齡不能為負數")
        self.__age = value
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    @weight.setter
    def weight(self, value: float):
        if value <= 0:
            raise ValueError("體重必須大於 0")
        self.__weight = value
    
    @property
    def health_status(self) -> str:
        return self.__health_status
    
    def health_checkup(self, status: str):
        """
        健康檢查
        展示：封裝（控制內部狀態的修改）
        """
        self.__health_status = status
        self.__last_checkup = datetime.now()
        print(f"  ✓ {self.__name} 完成健康檢查，狀態：{status}")
    
    def feed(self, food: str, amount: float):
        """
        餵食方法（抽象行為，期望子類別覆寫）
        展示：多型的基礎
        """
        print(f"  餵食 {self.__name}：{food} {amount}kg")
    
    def make_sound(self) -> str:
        """
        發出聲音（抽象方法）
        展示：多型，子類別應覆寫此方法
        """
        return "動物的聲音"
    
    def daily_activity(self):
        """
        日常活動（抽象方法）
        展示：多型
        """
        print(f"  {self.__name} 正在活動")
    
    def get_info(self) -> str:
        """獲取動物資訊"""
        return (f"{self.__species}: {self.__name}, "
                f"{self.__age}歲, {self.__weight}kg, "
                f"健康狀態: {self.__health_status}")
    
    def __str__(self) -> str:
        """字串表示"""
        return f"{self.__species}({self.__name})"
    
    def __repr__(self) -> str:
        """開發者表示"""
        return f"Animal(name='{self.__name}', species='{self.__species}')"


class Mammal(Animal):
    """
    哺乳動物類別
    展示：繼承（is-a 關係）
    """
    
    def __init__(self, name: str, species: str, age: int, weight: float, 
                 fur_color: str):
        # 使用 super() 調用父類別建構器
        super().__init__(name, species, age, weight)
        self.fur_color = fur_color
    
    def feed(self, food: str = "肉類或植物", amount: float = 2.0):
        """
        覆寫餵食方法
        展示：多型（相同介面，不同實現）
        """
        print(f"  🥩 餵食哺乳動物 {self.name}：{food} {amount}kg")
        print(f"     {self.name} 正在用牙齒咀嚼食物")
    
    def nurse_young(self):
        """哺乳動物特有的行為"""
        print(f"  🍼 {self.name} 正在哺育幼獸")


class Bird(Animal):
    """
    鳥類別
    展示：繼承
    """
    
    def __init__(self, name: str, species: str, age: int, weight: float, 
                 wingspan: float):
        super().__init__(name, species, age, weight)
        self.wingspan = wingspan  # 翼展
    
    def feed(self, food: str = "種子或昆蟲", amount: float = 0.5):
        """
        覆寫餵食方法
        展示：多型
        """
        print(f"  🌾 餵食鳥類 {self.name}：{food} {amount}kg")
        print(f"     {self.name} 正在用喙啄食")
    
    def fly(self):
        """鳥類特有的行為"""
        print(f"  🦅 {self.name} 展開 {self.wingspan}m 的翅膀，正在飛翔")


class Reptile(Animal):
    """
    爬行動物類別
    展示：繼承
    """
    
    def __init__(self, name: str, species: str, age: int, weight: float, 
                 scale_type: str):
        super().__init__(name, species, age, weight)
        self.scale_type = scale_type  # 鱗片類型
    
    def feed(self, food: str = "肉類", amount: float = 1.5):
        """
        覆寫餵食方法
        展示：多型
        """
        print(f"  🦎 餵食爬行動物 {self.name}：{food} {amount}kg")
        print(f"     {self.name} 正在吞食獵物")
    
    def bask_in_sun(self):
        """爬行動物特有的行為：曬太陽"""
        print(f"  ☀️ {self.name} 正在曬太陽調節體溫")


# ========== 具體動物子類別 ==========

class Lion(Mammal):
    """獅子類別 - 多層繼承"""
    
    def __init__(self, name: str, age: int, weight: float, fur_color: str, 
                 pride_size: int = 1):
        super().__init__(name, "獅子", age, weight, fur_color)
        self.pride_size = pride_size  # 獅群大小
    
    def make_sound(self) -> str:
        """展示：多型"""
        return "吼叫：ROAR!!!"
    
    def daily_activity(self):
        """展示：多型"""
        print(f"  🦁 {self.name} 正在巡視領地")
    
    def hunt(self):
        """獅子特有的行為"""
        print(f"  🎯 {self.name} 正在狩獵，獅群規模：{self.pride_size}")


class Elephant(Mammal):
    """大象類別"""
    
    def __init__(self, name: str, age: int, weight: float, fur_color: str, 
                 tusk_length: float):
        super().__init__(name, "大象", age, weight, fur_color)
        self.tusk_length = tusk_length  # 象牙長度
    
    def make_sound(self) -> str:
        return "trumpet：嗚~~~"
    
    def daily_activity(self):
        print(f"  🐘 {self.name} 正在用長鼻子噴水洗澡")
    
    def spray_water(self):
        """大象特有的行為"""
        print(f"  💦 {self.name} 用鼻子噴水")


class Parrot(Bird):
    """鸚鵡類別"""
    
    def __init__(self, name: str, age: int, weight: float, wingspan: float, 
                 vocabulary_size: int = 0):
        super().__init__(name, "鸚鵡", age, weight, wingspan)
        self.vocabulary_size = vocabulary_size  # 詞彙量
    
    def make_sound(self) -> str:
        return "squawk：嘎嘎嘎！"
    
    def daily_activity(self):
        print(f"  🦜 {self.name} 正在樹枝上跳躍")
    
    def mimic_speech(self, phrase: str):
        """鸚鵡特有的行為：模仿說話"""
        print(f"  🗣️ {self.name} 模仿說話：「{phrase}」")


class Snake(Reptile):
    """蛇類別"""
    
    def __init__(self, name: str, age: int, weight: float, scale_type: str, 
                 length: float, is_venomous: bool = False):
        super().__init__(name, "蛇", age, weight, scale_type)
        self.length = length  # 長度
        self.is_venomous = is_venomous  # 是否有毒
    
    def make_sound(self) -> str:
        return "hiss：嘶嘶嘶..."
    
    def daily_activity(self):
        print(f"  🐍 {self.name} 正在草叢中爬行，長度：{self.length}m")
    
    def shed_skin(self):
        """蛇特有的行為：蛻皮"""
        venom_info = "有毒" if self.is_venomous else "無毒"
        print(f"  🔄 {self.name} 正在蛻皮 ({venom_info})")


# ========== 動物園管理類別 ==========

class Zoo:
    """
    動物園管理系統
    展示：封裝（管理複雜的狀態）、多型（統一處理不同動物）
    """
    
    def __init__(self, name: str):
        self.__name = name
        self.__animals: List[Animal] = []
        self.__staff_count = 0
        print(f"\n🏛️ {name} 動物園成立！")
    
    def add_animal(self, animal: Animal):
        """
        添加動物
        展示：多型（接受任何 Animal 子類別）
        """
        self.__animals.append(animal)
        print(f"   ✓ {animal} 已加入動物園")
    
    def daily_feeding(self):
        """
        每日餵食
        展示：多型的威力（統一處理不同類型的動物）
        """
        print(f"\n📋 {self.__name} 開始每日餵食：")
        for animal in self.__animals:
            print(f"\n{animal.get_info()}")
            animal.feed()  # 多型：每種動物有不同的餵食方式
    
    def morning_activities(self):
        """
        晨間活動
        展示：多型
        """
        print(f"\n🌅 {self.__name} 晨間活動：")
        for animal in self.__animals:
            print(f"\n{animal}:")
            print(f"  聲音：{animal.make_sound()}")  # 多型
            animal.daily_activity()  # 多型
    
    def health_checkup_all(self):
        """
        全體健康檢查
        展示：封裝（通過方法控制狀態修改）
        """
        print(f"\n🏥 {self.__name} 進行全體健康檢查：")
        import random
        statuses = ["健康", "健康", "健康", "輕微感冒", "健康"]
        
        for animal in self.__animals:
            status = random.choice(statuses)
            animal.health_checkup(status)
    
    def show_special_behaviors(self):
        """
        展示特殊行為
        展示：多型（不同類別有不同的特殊方法）
        """
        print(f"\n🎪 {self.__name} 特殊行為展示：")
        
        for animal in self.__animals:
            print(f"\n{animal}:")
            
            # 使用 isinstance 檢查類型，調用特定方法
            if isinstance(animal, Lion):
                animal.hunt()
            elif isinstance(animal, Elephant):
                animal.spray_water()
            elif isinstance(animal, Parrot):
                animal.mimic_speech("你好！")
            elif isinstance(animal, Snake):
                animal.shed_skin()
    
    def get_statistics(self):
        """獲取統計資訊"""
        print(f"\n📊 {self.__name} 統計資訊：")
        print(f"  總動物數：{len(self.__animals)}")
        
        # 按類別分類
        species_count = {}
        for animal in self.__animals:
            species = animal.species
            species_count[species] = species_count.get(species, 0) + 1
        
        print(f"  動物分佈：")
        for species, count in species_count.items():
            print(f"    - {species}: {count} 隻")
    
    def __len__(self) -> int:
        """
        重載 len()
        展示：多型（運算符重載）
        """
        return len(self.__animals)
    
    def __getitem__(self, index: int) -> Animal:
        """
        重載 []
        展示：多型（運算符重載）
        """
        return self.__animals[index]
    
    def __str__(self) -> str:
        return f"{self.__name} 動物園 ({len(self)} 隻動物)"


# ========== 主程式：展示完整的 OOP 實踐 ==========

def main():
    """主程式"""
    
    print("\n" + "=" * 80)
    print("開始建立動物園管理系統")
    print("=" * 80)
    
    # 創建動物園
    zoo = Zoo("台北市立動物園")
    
    # 創建各種動物（展示繼承層次）
    print("\n" + "=" * 80)
    print("添加動物到動物園")
    print("=" * 80)
    
    lion = Lion("辛巴", 5, 190.0, "金色", pride_size=3)
    elephant = Elephant("呆呆", 12, 5000.0, "灰色", tusk_length=1.5)
    parrot = Parrot("波利", 3, 0.4, 0.6, vocabulary_size=50)
    snake = Snake("小綠", 4, 2.5, "光滑鱗片", length=2.3, is_venomous=False)
    
    # 添加到動物園
    zoo.add_animal(lion)
    zoo.add_animal(elephant)
    zoo.add_animal(parrot)
    zoo.add_animal(snake)
    
    # 展示多型：每日餵食
    zoo.daily_feeding()
    
    # 展示多型：晨間活動
    zoo.morning_activities()
    
    # 展示封裝：健康檢查
    zoo.health_checkup_all()
    
    # 展示特殊行為
    zoo.show_special_behaviors()
    
    # 統計資訊
    zoo.get_statistics()
    
    # 展示運算符重載
    print(f"\n{zoo}")  # 調用 __str__
    print(f"動物數量：{len(zoo)}")  # 調用 __len__
    print(f"第一隻動物：{zoo[0]}")  # 調用 __getitem__
    
    print("\n" + "=" * 80)
    print("動物園管理系統演示完成")
    print("=" * 80)


if __name__ == "__main__":
    main()
    
    print("\n" + "=" * 80)
    print("OOP 三大特性總結")
    print("=" * 80)
    print("""
1. 封裝 (Encapsulation) 的應用：
   ✓ 使用私有屬性 (__name, __weight 等)
   ✓ 使用 @property 提供受控訪問
   ✓ 將相關數據和方法組織在類別中
   ✓ 通過方法控制內部狀態修改 (health_checkup)

2. 繼承 (Inheritance) 的應用：
   ✓ 建立類別層次：Animal -> Mammal/Bird/Reptile -> Lion/Elephant 等
   ✓ 使用 super() 調用父類別方法
   ✓ 程式碼重用：共同特性定義在父類別
   ✓ 多層繼承：Lion 繼承自 Mammal，Mammal 繼承自 Animal

3. 多型 (Polymorphism) 的應用：
   ✓ 方法覆寫：每種動物有自己的 feed(), make_sound(), daily_activity()
   ✓ 統一介面：Zoo 可以用相同方式處理所有動物
   ✓ 運算符重載：__len__, __getitem__, __str__
   ✓ Duck Typing：只要有相同的方法就可以被統一處理

💡 關鍵啟示：
   - 三大特性協同作用，構建出健壯的系統
   - 封裝保護數據，繼承重用程式碼，多型增加靈活性
   - 對擴展開放，對修改封閉（易於添加新動物種類）
   - 結構清晰，易於維護和擴展
    """)
