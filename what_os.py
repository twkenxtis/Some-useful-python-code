import sys

if sys.platform.startswith('linux'):
    print("運行在 Unix-like 環境下")
elif sys.platform.startswith('win32'):
    print("運行在 Windows 環境下")
else:
    print("未知作業系統")