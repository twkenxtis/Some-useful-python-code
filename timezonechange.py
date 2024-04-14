from datetime import datetime
import pytz

class GMTtoUTC8:
    def __init__(self, from_tz, to_tz):
        # 初始化方法，用於創建TimeConverter對象，from_tz和to_tz是時區的名稱
        # self表示類的實例本身，可以訪問類的屬性
        # pytz.timezone是創建pytz時區對象的函數，from_tz和to_tz分別是源時區和目標時區的名稱
        self.from_tz = pytz.timezone(from_tz)  # 將源時區名稱轉換為pytz時區對象
        self.to_tz = pytz.timezone(to_tz)  # 將目標時區名稱轉換為pytz時區對象

    def convert_time(self, time_str, format="%a, %d %b %Y %H:%M:%S %Z", output_format="%y%m%d %H:%M"):
        # convert_time方法用於將給定時區的時間字符串轉換為另一個時區的指定格式的時間字符串
        # time_str是待轉換的時間字符串
        # format是待轉換的時間字符串的格式，默認為"%a, %d %b %Y %H:%M:%S %Z"
        # output_format是轉換後的時間字符串的格式，默認為"%y%m%d %H:%M"
        # datetime.strptime是將字符串解析為datetime對象的函數，time_str是待解析的字符串，format是時間字符串的格式
        time_obj = datetime.strptime(time_str, format)
        # self.from_tz.localize用於將datetime對象添加時區信息，轉換為源時區的時間對象
        time_obj_from_tz = self.from_tz.localize(time_obj)
        # time_obj_from_tz.astimezone用於將時間對象轉換為目標時區的時間對象
        time_obj_to_tz = time_obj_from_tz.astimezone(self.to_tz)
        # time_obj_to_tz.strftime用於將時間對象格式化為字符串，output_format是目標格式的時間字符串格式
        return time_obj_to_tz.strftime(output_format)  # 返回轉換後的時間字符串

# 提示用戶輸入 GMT 時間
user_input_time = input("What is your GMT timezone? \n")
# sample 
# Sat, 13 Apr 2024 17:02:08 GMT
# Sat, 13 Apr 2024 14:59:21 GMT
# Sat, 13 Apr 2024 16:09:30 GMT
# Sat, 13 Apr 2024 17:10:04 GMT

# 創建 TimeConverter 實例
converter = GMTtoUTC8("GMT", "Asia/Taipei")

# 轉換時間
published_tw = converter.convert_time(user_input_time)
print(published_tw)