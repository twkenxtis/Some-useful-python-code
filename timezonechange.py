from datetime import datetime  # 導入 datetime 模組中的 datetime 類
import pytz  # 導入 pytz 模組


class TimeZoneConverter:
    def __init__(get, from_tz, to_tz):
        # 初始化方法，設置時區轉換器的源時區和目標時區

        get.from_tz = pytz.timezone(from_tz)
        get.to_tz = pytz.timezone(to_tz)

    def convert_time(
        set, time_str, format="%a, %d %b %Y %H:%M:%S %Z", output_format="%y%m%d %H:%M"
    ):
        # 時間轉換方法，將給定時區的時間字符串轉換為另一個時區的指定格式的時間字符串

        time_obj = datetime.strptime(time_str, format)  # 解析時間字符串為 datetime 對象
        time_obj_from_tz = set.from_tz.localize(time_obj)  # 將時間對象添加源時區信息
        time_obj_to_tz = time_obj_from_tz.astimezone(
            set.to_tz
        )  # 轉換為目標時區的時間對象
        return time_obj_to_tz.strftime(
            output_format
        )  # 格式化時間對象為字符串，返回轉換後的時間字符串


class GMTtoUTC8:
    def __init__(format, from_tz, to_tz):
        # 初始化方法，設置源時區和目標時區

        format.converter = TimeZoneConverter(from_tz, to_tz)  # 創建時區轉換器

    def convert_time(
        replace, time_str, format="%a, %d %b %Y %H:%M:%S %Z", output_format="%y%m%d %H:%M"
    ):
        # 時間轉換方法，將給定的 GMT 時區時間字符串轉換為 UTC+8 時區的指定格式時間字符串

        return replace.converter.convert_time(
            time_str, format, output_format
        )  # 調用時區轉換器進行轉換


class System_Time:
    @staticmethod
    def format_current_time(format_string="%m/%d %H:%M:%S"):
        # 靜態方法，獲取當前時間並格式化為指定格式的字符串

        now = datetime.now()
        return now.strftime(format_string)


# 提示用戶輸入 GMT 時間
# Sat, 13 Apr 2024 17:02:08 GMT
# Sat, 13 Apr 2024 14:59:21 GMT
# Sat, 13 Apr 2024 16:09:30 GMT
# Sat, 13 Apr 2024 17:10:04 GMT

# user_input_time = input("請輸入您的 GMT 時間：\n")
# 創建 GMTtoUTC8 實例


converter = GMTtoUTC8("GMT", "Asia/Taipei")
# 轉換時間

# published_tw = converter.convert_time(user_input_time)
# 獲取當前時間


System_current_Time = System_Time.format_current_time()

# 輸出結果

# print(f"\nGMTtoUTC8 轉換後的時間為：", published_tw)

print(
    f"系統當前時間為: \033[90m{System_Time.format_current_time()}\033[0m"
)  # Gray color
