import hashlib
import json
from datetime import datetime, timedelta
import threading
import time

# 定義超時時間常量

Timeout_Duration = timedelta(minutes=5)

# 定義定期清理的時間間隔（假設為1小時）

Clean_Interval = timedelta(hours=1)

# 定義冷卻時間（假設為5分鐘）

Cooldown_Duration = timedelta(minutes=5)

# 創建空的字典，用於RAM優先存儲

url_dict = {}

# 鏡像到本地磁碟上的JSON文件的函數


def mirror_to_disk():
    with open("backup_data.json", "w") as f:
        json.dump(url_dict, f)


# 定義清理過期資料的函數


def clean_expired_data():
    current_time = datetime.now()
    expired_keys = [
        key
        for key, value in url_dict.items()
        if current_time - value["timestamp"] > Timeout_Duration
    ]
    for key in expired_keys:
        del url_dict[key]


# 定義定期清理的函數


def periodic_cleaning():
    while True:
        clean_expired_data()
        mirror_to_disk()
        # 等待指定的時間間隔後再次執行清理

        time.sleep(Clean_Interval.total_seconds())


# 定義事件類


class EventManager:
    def __init__(self):
        self.handlers = {}
        self.cooldown = False

    def add_event_handler(self, event, handler):
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(handler)

    def trigger_event(self, event, *args, **kwargs):
        if not self.cooldown and event in self.handlers:
            for handler in self.handlers[event]:
                handler(*args, **kwargs)
            self.cooldown = True
            threading.Timer(
                Cooldown_Duration.total_seconds(), self.reset_cooldown
            ).start()

    def reset_cooldown(self):
        self.cooldown = False


# 創建事件管理器

event_manager = EventManager()

# 定義匯入新資料時觸發的處理函數


def on_new_data_imported():
    event_manager.trigger_event("new_data_imported")


# 監聽匯入新資料事件

event_manager.add_event_handler("new_data_imported", clean_expired_data)

# 假設網址列表為 urls，對每個網址計算 MD5 哈希值並存儲在字典中

for url in urls:
    md5 = hashlib.md5(url.encode()).hexdigest()
    url_dict[md5] = {"url": url, "timestamp": datetime.now()}
    on_new_data_imported()
# 啟動定期清理任務

threading.Thread(target=periodic_cleaning, daemon=True).start()