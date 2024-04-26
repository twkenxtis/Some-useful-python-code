import os
import subprocess

def execute_script(script_path):
    try:
        # 在 Windows 系統中呼叫 bat 腳本，並擷取標準輸出
        result = subprocess.run([script_path], shell=False, capture_output=True, text=True, check=True)
        # 傳回腳本的標準輸出
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("执行脚本失败:", e)
        return None

# 取得腳本檔案的完整路徑
script_dir = os.path.dirname(os.path.abspath(__file__))  # 取得目前腳本檔案所在目錄
script_name = 'script.bat'  # 脚本文件名
script_path = os.path.join(script_dir, script_name)  # 組合成完整路徑

# 嘗試呼叫 bat 腳本並列印輸出值
bat_output = execute_script(script_path)
if bat_output is not None:
    print("bat 脚本的输出:", bat_output)
