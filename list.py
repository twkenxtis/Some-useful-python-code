import hashlib
import time
from datetime import datetime
import random

def format_current_time(format_string="%m/%d %H:%M:%S"):
    now = datetime.now()
    return now.strftime(format_string)

# 定義 Instagram_Rss_Account 列表

Instagram_Rss_List = [
    "fallingin__fall",
    "_yujin_an",
    "reinyourheart",
    "for_everyoung10",
    "liz.yeyo",
    "eeseooes",
]


# 定義一個 Class 來處理 Instagram RSS
class InstagramRSS:
    def __init__(self, rss_list):
        self.rss_list = rss_list

    # 定義一個方法來列印 RSS List 的內容
    def print_rss_list(self):
        print("用 for 迴圈每兩秒印一次 List 的內容，遞增列印", "\n")
        for account in self.rss_list:
            # 在變量 Cool_Down_Time 前面使用 ANSI escape code 將其設置為綠色
            Cool_Down_Time = random.randint(1, 5)
            print(
                f"\033[90m{format_current_time()}\033[0m", account,
                f"\033[Waiting for \033[92m{Cool_Down_Time}s\033[0m",
            )
            # 等待 Cool_Down_Time 秒
            time.sleep(Cool_Down_Time)  # 等待 Cool_Down_Time 繼續 for

# 創建 InstagramRSS 的實例
instagram_rss = InstagramRSS(Instagram_Rss_List)

# 調用 print_rss_list 方法來打印 RSS List 的內容
instagram_rss.print_rss_list()

print('用for迴圈每兩秒印一次List的內容，遞增列印','\n')
for account in Instagram_Rss_List:
    # 列印帳戶名稱
    
    print(format_current_time(),account,)
    # 等待2秒

    Cool_Down_Time = random.randint(2, 30)
    print(f"Cooldown time: {Cool_Down_Time} seconds")
    time.sleep(Cool_Down_Time)  # 等待 Cool_Down_Time 繼續for
      

# 列印列表中的第一個元素

first_account = Instagram_Rss_List[0]
print("第一個帳戶:", first_account, "\n")

# 對列表中的第一個元素進行切片

sliced_account = first_account[:5]
print("第一個帳戶的前5個字符:", sliced_account, "\n")

# 將列表中的所有元素轉換為大寫

upper_case_accounts = [account.upper() for account in Instagram_Rss_List]
print("所有帳戶的大寫形式:", upper_case_accounts, "\n")

# 將列表中的所有元素合併為一個字符串

combined_accounts = ", ".join(Instagram_Rss_List)
print("所有帳戶合併為一個字符串:", combined_accounts, "\n")

# 使用 print() 函數列印整個列表

print("使用 print() 函數列印整個列表:", Instagram_Rss_List, "\n")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

# 對列表中的每個元素進行哈希和轉換為UTF-8後列印

for account in Instagram_Rss_List:
    # 將字符串轉換為UTF-8編碼的字節串

    encoded_account = account.encode("utf-8")
    # 使用MD5哈希算法對字節串進行哈希

    hashed_account = hashlib.md5(encoded_account).hexdigest()
    # 列印哈希值

    print("哈希值:", hashed_account, account)
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
