"""
案例 4: 多型 (Polymorphism) 特性詳解
展示如何實現介面的靈活性，讓不同類別以統一方式交互
"""

print("=" * 80)
print("多型特性：實現介面的靈活性")
print("=" * 80)

# ========== Python 內建的多型 ==========
print("\n【1. Python 內建的多型：運算符重載】")

print("\n相同的 '+' 運算符，不同的行為：")
print(f"整數相加: 1 + 2 = {1 + 2}")
print(f"字串串接: 'Hello' + ' ' + 'World' = {'Hello' + ' ' + 'World'}")
print(f"列表合併: [1, 2] + [3, 4] = {[1, 2] + [3, 4]}")

print("\n背後的機制：特殊方法 (Dunder Methods)")
print(f"int 的 __add__: {(1).__add__(2)}")
print(f"str 的 __add__: {'Hello'.__add__(' World')}")


# ========== 方法多型：相同介面，不同實現 ==========
print("\n" + "=" * 80)
print("【2. 方法多型：統一的介面，不同的實現】")
print("=" * 80)

class Animal:
    """動物基礎類別"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """抽象方法：期望子類別覆寫"""
        raise NotImplementedError("子類別必須實現 speak 方法")
    
    def move(self):
        """抽象方法"""
        raise NotImplementedError("子類別必須實現 move 方法")


class Dog(Animal):
    """狗類別"""
    def speak(self):
        return f"{self.name} 說：汪汪汪！"
    
    def move(self):
        return f"{self.name} 正在奔跑"


class Cat(Animal):
    """貓類別"""
    def speak(self):
        return f"{self.name} 說：喵喵喵！"
    
    def move(self):
        return f"{self.name} 正在優雅地走動"


class Bird(Animal):
    """鳥類別"""
    def speak(self):
        return f"{self.name} 說：啾啾啾！"
    
    def move(self):
        return f"{self.name} 正在飛翔"


class Fish(Animal):
    """魚類別"""
    def speak(self):
        return f"{self.name} 無法發聲（在水中）"
    
    def move(self):
        return f"{self.name} 正在游泳"


# 多型的威力：統一處理不同類型的物件
def interact_with_animal(animal):
    """
    通用函式：可以處理任何 Animal 子類別
    這就是多型的核心價值
    """
    print(f"\n與 {animal.name} 互動：")
    print(f"  - {animal.speak()}")
    print(f"  - {animal.move()}")


# 創建不同類型的動物
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety"),
    Fish("Nemo")
]

print("\n多型實踐：用同一個函式處理不同的動物")
for animal in animals:
    interact_with_animal(animal)

print("\n✅ 關鍵點：")
print("   - 無需使用 if-else 判斷動物類型")
print("   - 統一的介面 (speak, move)")
print("   - 每個類別有自己的實現")
print("   - 易於擴展：新增動物類型無需修改現有程式碼")


# ========== 運算符重載：自定義多型行為 ==========
print("\n" + "=" * 80)
print("【3. 運算符重載：為自定義類別添加多型能力】")
print("=" * 80)

class Vector:
    """向量類別 - 展示運算符重載"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """重載 + 運算符：向量相加"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """重載 - 運算符：向量相減"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """重載 * 運算符：向量縮放"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """重載 == 運算符：向量相等判斷"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self):
        """重載 str()：自定義字串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """重載 repr()：自定義開發者表示"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __len__(self):
        """重載 len()：計算向量長度"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __getitem__(self, index):
        """重載 []：支持索引訪問"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("向量只有 x 和 y 兩個維度")


# 使用自定義的運算符
print("\n創建向量並使用運算符：")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

print(f"\nv1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 == v2 = {v1 == v2}")
print(f"v1 == Vector(3, 4) = {v1 == Vector(3, 4)}")

print(f"\nlen(v1) = {len(v1)}")
print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")


# ========== 白皮書中的範例：哺乳動物 "相加" ==========
print("\n" + "=" * 80)
print("【4. 白皮書範例：哺乳動物的 "相加" 運算】")
print("=" * 80)

class Mammal:
    """哺乳動物類別 - 自定義 "相加" 的意義"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __add__(self, other):
        """
        重載 + 運算符：兩個哺乳動物 "相加" = 產生後代
        後代的名字是父母名字的結合
        後代的壽命取父母中的最大值
        """
        if isinstance(other, Mammal):
            new_name = self.name + other.name
            new_age = max(self.age, other.age)
            offspring = Mammal(new_name, new_age)
            print(f"✓ {self.name} 和 {other.name} 產生了後代！")
            return offspring
        return NotImplemented
    
    def __str__(self):
        return f"{self.name} ({self.age}歲)"
    
    def __mul__(self, other):
        """
        重載 * 運算符：產生多個後代
        """
        if isinstance(other, Mammal):
            # 產生多個混合名字的後代
            offspring_count = 2
            offspring_list = []
            for i in range(offspring_count):
                new_name = f"{self.name}{other.name}_{i+1}"
                new_age = max(self.age, other.age)
                offspring_list.append(Mammal(new_name, new_age))
            print(f"✓ {self.name} 和 {other.name} 產生了 {offspring_count} 個後代！")
            return offspring_list
        return NotImplemented


# 使用哺乳動物的多型
print("\n創建哺乳動物並 "相加"：")
dog = Mammal("Max", 5)
cat = Mammal("Pumpkin", 8)

print(f"父: {dog}")
print(f"母: {cat}")

# 使用 + 運算符產生後代
offspring = dog + cat
print(f"後代: {offspring}")

print("\n使用 * 運算符產生多個後代：")
multiple_offspring = dog * cat
for child in multiple_offspring:
    print(f"  - {child}")


# ========== Duck Typing：鴨子型別 ==========
print("\n" + "=" * 80)
print("【5. Duck Typing：Python 的動態多型】")
print("=" * 80)

print("\n概念：「如果它走起來像鴨子，叫起來像鴨子，那它就是鴨子」")

class Duck:
    def swim(self):
        return "鴨子在游泳"
    
    def quack(self):
        return "嘎嘎嘎！"


class Person:
    """人類：不是鴨子，但可以模仿鴨子的行為"""
    def swim(self):
        return "人在游泳"
    
    def quack(self):
        return "（模仿）嘎嘎嘎！"


class Robot:
    """機器人：完全不同的類別，但有相同的介面"""
    def swim(self):
        return "機器人在水中移動"
    
    def quack(self):
        return "電子音：嘎嘎嘎！"


def make_it_quack(duck_like_object):
    """
    Duck Typing：不檢查類型，只要有 quack 和 swim 方法就可以
    """
    print(f"  - {duck_like_object.quack()}")
    print(f"  - {duck_like_object.swim()}")


# 使用 Duck Typing
print("\n測試 Duck Typing：")
objects = [Duck(), Person(), Robot()]

for obj in objects:
    print(f"\n{obj.__class__.__name__}:")
    make_it_quack(obj)

print("\n✅ Duck Typing 的優勢：")
print("   - 不需要繼承關係")
print("   - 只要有相同的介面就可以")
print("   - 更靈活，更符合 Python 的哲學")


# ========== 總結 ==========
print("\n" + "=" * 80)
print("多型特性總結")
print("=" * 80)
print("""
1. 多型的定義：
   - 相同的介面（方法名）
   - 不同的實現（每個類別自己的邏輯）
   - 可以用統一的方式處理不同類型的物件

2. 多型的實現方式：
   ① 方法覆寫 (Method Overriding)
      - 子類別重新定義父類別的方法
      - 統一的方法名，不同的行為
   
   ② 運算符重載 (Operator Overloading)
      - 重定義特殊方法 (__add__, __mul__ 等)
      - 讓自定義物件支持運算符
   
   ③ Duck Typing
      - 不依賴繼承關係
      - 只要有相同的介面就可以

3. 常用的特殊方法 (Dunder Methods)：
   - __add__(self, other)    : +
   - __sub__(self, other)    : -
   - __mul__(self, other)    : *
   - __eq__(self, other)     : ==
   - __lt__(self, other)     : <
   - __str__(self)           : str()
   - __repr__(self)          : repr()
   - __len__(self)           : len()
   - __getitem__(self, key)  : []

4. 多型的價值：
   ✓ 提高程式碼的靈活性
   ✓ 易於擴展（Open/Closed Principle）
   ✓ 減少 if-else 判斷
   ✓ 讓程式碼更通用、更優雅

5. 設計原則：
   - 對擴展開放，對修改封閉
   - 依賴抽象，不依賴具體實現
   - 面向介面編程

✅ 多型是 OOP 靈活性的核心體現！
""")
