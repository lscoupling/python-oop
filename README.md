# Python 物件導向程式設計 (OOP) 實戰案例

Python OOP 核心特性實作參考

## 📚 專案結構

```
python-oop/
├── README.md                           # 專案說明
├── 01_procedural_vs_oop.py            # 過程式 vs OOP 對比
├── 02_encapsulation.py                # 封裝特性詳解
├── 03_inheritance.py                  # 繼承特性詳解
├── 04_polymorphism.py                 # 多型特性詳解
└── 05_comprehensive_zoo_system.py     # 綜合實戰案例
```

## 🎯 核心特性

1. **封裝 (Encapsulation)** - 將數據與行為打包
2. **繼承 (Inheritance)** - 建立層次關係以實現程式碼重用
3. **多型 (Polymorphism)** - 實現介面的靈活性

## 📖 案例說明

### 案例 1: 過程式 vs 物件導向編程對比

**檔案**: `01_procedural_vs_oop.py`

**內容**:
- 展示過程式編程的問題（充滿 if-else、數據與邏輯分離）
- 對比 OOP 的優雅結構
- 理解為何 OOP 是「結構化的議論文」而非「散文」

**執行**:
```bash
python 01_procedural_vs_oop.py
```

**關鍵概念**:
- 過程式風格的混亂
- OOP 的結構化優勢
- 無需 if-else 的多型處理

---

### 案例 2: 封裝特性詳解

**檔案**: `02_encapsulation.py`

**內容**:
- 類別與實例的概念
- `__init__` 建構器的作用
- 私有屬性（`__attribute`）與訪問控制
- `@property` 裝飾器的優雅應用

**執行**:
```bash
python 02_encapsulation.py
```

**關鍵概念**:
- 基礎封裝：`BankAccount` 類別
- 進階封裝：`SecureBankAccount` 私有屬性
- 屬性裝飾器：`SmartBankAccount` 的 `@property`

**程式碼參考**:
```python
# 私有屬性
self.__balance = 0

# Property 裝飾器
@property
def balance(self):
    return self.__balance

@balance.setter
def balance(self, value):
    if value < 0:
        raise ValueError("餘額不能為負數")
    self.__balance = value
```

---

### 案例 3: 繼承特性詳解

**檔案**: `03_inheritance.py`

**內容**:
- 基礎繼承：母類別與子類別
- `super()` 函式的應用
- 多層繼承結構
- 方法覆寫 (Method Overriding)
- 繼承關係檢驗（`isinstance`, `issubclass`）

**執行**:
```bash
python 03_inheritance.py
```

**關鍵概念**:
```python
# 基礎繼承
class Mammal:
    def feed(self):
        print("餵食")

class Dog(Mammal):
    def bark(self):
        print("汪汪")

# 使用 super()
class AdvancedDog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 調用父類別
        self.breed = breed
```

**技術重點**:
- DRY (Don't Repeat Yourself) 原則
- 多層繼承：`ServiceDog -> AdvancedDog -> Mammal`
- 方法覆寫 vs 方法擴展

---

### 案例 4: 多型特性詳解

**檔案**: `04_polymorphism.py`

**內容**:
- Python 內建的多型（運算符重載）
- 方法多型：相同介面，不同實現
- 運算符重載：自定義多型行為
- Duck Typing：Python 的動態多型
- 特殊方法（Dunder Methods）詳解

**執行**:
```bash
python 04_polymorphism.py
```

**關鍵概念**:
```python
# 方法多型
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵"

# 統一處理
def interact(animal):
    print(animal.speak())  # 多型！

# 運算符重載
class Vector:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

**技術重點**:
- 常用特殊方法：`__add__`, `__mul__`, `__eq__`, `__str__`, `__len__`
- Duck Typing：「如果它走起來像鴨子...」
- Open/Closed Principle：對擴展開放，對修改封閉

---

### 案例 5: 綜合實戰 - 動物園管理系統

**檔案**: `05_comprehensive_zoo_system.py`

**內容**:
- 整合三大特性的完整應用
- 完整的類別層次結構
- 實際的管理系統設計
- 類型提示（Type Hints）的使用

**執行**:
```bash
python 05_comprehensive_zoo_system.py
```

**系統架構**:
```
Animal (基礎類別)
├── Mammal (哺乳動物)
│   ├── Lion (獅子)
│   └── Elephant (大象)
├── Bird (鳥類)
│   └── Parrot (鸚鵡)
└── Reptile (爬行動物)
    └── Snake (蛇)

Zoo (動物園管理系統)
├── 添加動物
├── 每日餵食 (多型)
├── 晨間活動 (多型)
├── 健康檢查 (封裝)
└── 統計資訊
```

**關鍵特性展示**:

1. **封裝**:
   - 私有屬性：`__name`, `__health_status`
   - 受控訪問：`@property`
   - 方法控制狀態：`health_checkup()`

2. **繼承**:
   - 多層繼承結構
   - `super()` 的正確使用
   - 程式碼重用

3. **多型**:
   - 統一的 `feed()` 介面
   - 不同動物的不同實現
   - 運算符重載：`__len__`, `__getitem__`

---

## 🚀 執行方式

**環境需求**: Python 3.7+

```bash
# 執行所有案例
python 01_procedural_vs_oop.py
python 02_encapsulation.py
python 03_inheritance.py
python 04_polymorphism.py
python 05_comprehensive_zoo_system.py
```

---

## 💡 核心概念速查

### 封裝 (Encapsulation)

```python
class Example:
    def __init__(self, value):
        self.__private = value  # 私有屬性
    
    @property
    def value(self):
        return self.__private
    
    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError()
        self.__private = new_value
```

### 繼承 (Inheritance)

```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)  # 調用父類別
        self.y = y
```

### 多型 (Polymorphism)

```python
# 方法多型
class Animal:
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "汪"

class Cat(Animal):
    def speak(self): return "喵"

# 統一處理
animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())  # 多型！

# 運算符重載
class Point:
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

---

## 📚 相關主題

### 設計模式
- 單例模式 (Singleton Pattern)
- 工廠模式 (Factory Pattern)
- 觀察者模式 (Observer Pattern)
- 策略模式 (Strategy Pattern)

### 進階主題
- 抽象基礎類別 (ABC - Abstract Base Classes)
- 多重繼承與 MRO (Method Resolution Order)
- 描述器 (Descriptors)
- 元類別 (Metaclasses)
