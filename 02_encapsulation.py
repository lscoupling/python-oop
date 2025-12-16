"""
案例 2: 封裝 (Encapsulation) 特性詳解
展示如何將數據與行為打包，以及私有屬性的應用
"""

print("=" * 80)
print("封裝特性：將數據與行為打包成獨立單元")
print("=" * 80)

# ========== 基礎封裝：類別與實例 ==========
print("\n【1. 基礎封裝：類別作為藍圖】")

class BankAccount:
    """銀行帳戶類別 - 展示封裝的基本概念"""
    
    def __init__(self, account_holder, initial_balance=0):
        """
        建構器：在創建實例時自動調用
        :param account_holder: 帳戶持有人
        :param initial_balance: 初始餘額，預設為 0
        """
        # 實例變數：每個實例獨有的數據
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"✓ 已創建帳戶：{account_holder}，初始餘額：${initial_balance}")
    
    def deposit(self, amount):
        """存款方法 - 行為與數據封裝在一起"""
        if amount > 0:
            self.balance += amount
            print(f"✓ {self.account_holder} 存款 ${amount}，餘額：${self.balance}")
        else:
            print("✗ 存款金額必須大於 0")
    
    def withdraw(self, amount):
        """提款方法"""
        if amount > self.balance:
            print(f"✗ 餘額不足！目前餘額：${self.balance}")
        elif amount <= 0:
            print("✗ 提款金額必須大於 0")
        else:
            self.balance -= amount
            print(f"✓ {self.account_holder} 提款 ${amount}，餘額：${self.balance}")
    
    def get_balance(self):
        """查詢餘額方法"""
        return self.balance


# 創建實例（物件）
account1 = BankAccount("張三", 1000)
account2 = BankAccount("李四", 500)

print("\n操作帳戶：")
account1.deposit(500)
account1.withdraw(200)
print(f"張三的餘額：${account1.get_balance()}")

print("\n每個實例擁有獨立的數據：")
account2.deposit(300)
print(f"李四的餘額：${account2.get_balance()}")


# ========== 進階封裝：私有屬性與訪問控制 ==========
print("\n" + "=" * 80)
print("【2. 進階封裝：私有屬性與訪問控制】")
print("=" * 80)

class SecureBankAccount:
    """安全銀行帳戶 - 使用私有屬性保護敏感數據"""
    
    def __init__(self, account_holder, pin_code, initial_balance=0):
        """
        :param pin_code: 密碼（私有）
        """
        self.account_holder = account_holder  # 公開屬性
        self.__pin_code = pin_code  # 私有屬性（雙底線開頭）
        self.__balance = initial_balance  # 私有屬性
        self.__transaction_history = []  # 私有交易紀錄
        print(f"✓ 已創建安全帳戶：{account_holder}")
    
    def __verify_pin(self, pin):
        """私有方法：驗證密碼（外部無法直接調用）"""
        return pin == self.__pin_code
    
    def deposit(self, amount, pin):
        """存款需要密碼驗證"""
        if not self.__verify_pin(pin):
            print("✗ 密碼錯誤！")
            return
        
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"存款: +${amount}")
            print(f"✓ 存款 ${amount} 成功，餘額：${self.__balance}")
        else:
            print("✗ 存款金額必須大於 0")
    
    def withdraw(self, amount, pin):
        """提款需要密碼驗證"""
        if not self.__verify_pin(pin):
            print("✗ 密碼錯誤！")
            return
        
        if amount > self.__balance:
            print(f"✗ 餘額不足！目前餘額：${self.__balance}")
        elif amount <= 0:
            print("✗ 提款金額必須大於 0")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"提款: -${amount}")
            print(f"✓ 提款 ${amount} 成功，餘額：${self.__balance}")
    
    def get_balance(self, pin):
        """查詢餘額需要密碼"""
        if not self.__verify_pin(pin):
            print("✗ 密碼錯誤！")
            return None
        return self.__balance
    
    def get_transaction_history(self, pin):
        """查詢交易紀錄需要密碼"""
        if not self.__verify_pin(pin):
            print("✗ 密碼錯誤！")
            return []
        return self.__transaction_history.copy()
    
    def change_pin(self, old_pin, new_pin):
        """修改密碼"""
        if not self.__verify_pin(old_pin):
            print("✗ 舊密碼錯誤！")
            return
        self.__pin_code = new_pin
        print("✓ 密碼修改成功")


# 使用安全帳戶
print("\n創建安全帳戶：")
secure_account = SecureBankAccount("王五", "1234", 1000)

print("\n正確密碼操作：")
secure_account.deposit(500, "1234")
secure_account.withdraw(200, "1234")
balance = secure_account.get_balance("1234")
print(f"餘額：${balance}")

print("\n錯誤密碼操作：")
secure_account.withdraw(100, "0000")  # 密碼錯誤
secure_account.get_balance("9999")  # 密碼錯誤

print("\n嘗試直接訪問私有屬性：")
try:
    # 這會失敗，因為 __balance 是私有的
    print(secure_account.__balance)
except AttributeError as e:
    print(f"✗ 無法訪問：{e}")

print("\nPython 的 name mangling 機制：")
print(f"實際屬性名稱被改寫為：{dir(secure_account)[-3:]}")  # _SecureBankAccount__balance


# ========== 屬性裝飾器 (Property) ==========
print("\n" + "=" * 80)
print("【3. 使用 @property 裝飾器：優雅的訪問控制】")
print("=" * 80)

class SmartBankAccount:
    """智慧銀行帳戶 - 使用 property 提供受控的屬性訪問"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance
    
    @property
    def balance(self):
        """
        使用 @property 將方法轉換為屬性
        可以像訪問屬性一樣調用，但實際執行的是方法
        """
        print("(正在檢查餘額...)")
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """
        使用 @balance.setter 控制賦值行為
        可以添加驗證邏輯
        """
        if value < 0:
            raise ValueError("餘額不能為負數！")
        print(f"(正在更新餘額：${self.__balance} -> ${value})")
        self.__balance = value
    
    @property
    def formatted_balance(self):
        """只讀屬性：格式化的餘額顯示"""
        return f"${self.__balance:,.2f}"


# 使用智慧帳戶
print("\n創建智慧帳戶：")
smart_account = SmartBankAccount("趙六", 5000)

print("\n使用 property 訪問餘額（像屬性一樣）：")
print(f"餘額：{smart_account.balance}")  # 調用 getter

print("\n使用 property 設置餘額（像屬性一樣）：")
smart_account.balance = 6000  # 調用 setter

print("\n訪問只讀屬性：")
print(f"格式化餘額：{smart_account.formatted_balance}")

print("\n嘗試設置非法值：")
try:
    smart_account.balance = -100  # setter 會驗證並拋出錯誤
except ValueError as e:
    print(f"✗ 錯誤：{e}")


# ========== 總結 ==========
print("\n" + "=" * 80)
print("封裝特性總結")
print("=" * 80)
print("""
1. 基礎封裝：
   - 使用 class 定義類別（藍圖）
   - 使用 __init__ 建構器初始化實例
   - self 代表實例本身
   - 將相關的數據和方法組織在一起

2. 訪問控制：
   - 單底線 (_attribute): 約定為內部使用（protected）
   - 雙底線 (__attribute): 名稱改寫，更強的私有性（private）
   - 無底線: 公開屬性和方法（public）

3. Property 裝飾器：
   - @property: 將方法轉換為可讀屬性
   - @property.setter: 控制屬性的賦值行為
   - 提供優雅的訪問控制，同時保持簡潔的語法

✅ 封裝的核心價值：
   - 隱藏內部實現細節
   - 保護數據完整性
   - 提供清晰的介面
   - 提高程式碼的安全性和可維護性
""")
