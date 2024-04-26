import os
import subprocess

def execute_script(script_path):
    try:
        # 在 Unix-like 系統中調用 sh 腳本，並捕獲標準輸出
        result = subprocess.run(['sh', script_path], capture_output=True, text=True, check=True)
        # 返回腳本的標準輸出
        return result.stdout
    except subprocess.CalledProcessError as e:
        pass  # 什麼都不做

# 取得腳本檔案的完整路徑
script_dir = os.path.dirname(os.path.abspath(__file__))  # 取得目前腳本檔案所在目錄
script_name = 'script.bat'  # 脚本文件名
script_path = os.path.join(script_dir, script_name)  # 組合成完整路徑

# 指定 sh 腳本的路徑
sh_script_path = 'script.sh'

# 嘗試調用 sh 腳本並列印輸出值
sh_output = execute_script(sh_script_path)
if sh_output is not None:
    print("sh 腳本的輸出:",sh_output)
