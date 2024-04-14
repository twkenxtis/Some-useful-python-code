import datetime

def system_current_time(format_string="%m/%d at %H:%M:%S"):
    os_time = datetime.datetime.now()
    return os_time.strftime(format_string)

# 使用預設格式輸出當前日期和時間
print(system_current_time())