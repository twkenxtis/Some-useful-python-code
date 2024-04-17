from datetime import datetime  # 導入 datetime 模組中的 datetime 類
import pytz  # 導入 pytz 模組

class TimeZoneConverter:
    def __init__(self, from_tz, to_tz):

        self.from_tz = pytz.timezone(from_tz)
        self.to_tz = pytz.timezone(to_tz)

    def convert_time_gmt_to_utc(
        self, time_str, format="%a, %d %b %Y %H:%M:%S %Z", output_format="%y%m%d %H:%M"
    ):
        # A time conversion method that converts a time string in a given time zone to a time string in a specified format in another time zone.

        time_obj = datetime.strptime(
            time_str, format
        )  # Parsing a time string into a datetime object
        time_obj_from_tz = self.from_tz.localize(
            time_obj
        )  # Add source time zone information to the time object
        time_obj_to_tz = time_obj_from_tz.astimezone(
            self.to_tz
        )  # Convert the time object to the target time zone.
        return time_obj_to_tz.strftime(
            output_format
        )  # Format the time object as a string and return the converted time string.

    def format_time_slice(
        self, time_str, format="%a, %d %b %Y %H:%M:%S %Z", output_format="%y%m%d %H:%M"
    ):
        # Time conversion method to convert a given GMT time string to a time string in a specified format in the UTC+8 time zone.

        return self.convert_time_gmt_to_utc(
            time_str, format, output_format
        )  # Call the time zone converter for conversion


class System_Time:
    @staticmethod
    def format_current_time(format_string="%m/%d %H:%M:%S"):
        # Static method, get the current time and format it as a string in the specified format.

        now = datetime.now()
        return now.strftime(format_string)


# 提示用戶輸入 GMT 時間
# Sat, 13 Apr 2024 17:02:08 GMT
# Sat, 13 Apr 2024 14:59:21 GMT
# Sat, 13 Apr 2024 16:09:30 GMT
# Sat, 13 Apr 2024 17:10:04 GMT

user_input_time = input("請輸入您的 GMT 時間：\n")
# 創建 GMTtoUTC8 實例


converter = TimeZoneConverter("GMT", "Asia/Taipei")
# 轉換時間

published_tw = converter.convert_time_gmt_to_utc(user_input_time)
# 獲取當前時間


System_current_Time = System_Time.format_current_time()

# 輸出結果

print(f"\nGMTtoUTC8 轉換後的時間為：", published_tw)

print(
    f"系統當前時間為: \033[90m{System_Time.format_current_time()}\033[0m"
)  # Gray color
