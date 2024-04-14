def print_color(color_code, text):
    return f"\x1b[{color_code}m{text}\x1b[0m"


def print_color_variants(color_code, text):
    code = f"\x1b[{color_code}m"
    return (
        code
        + text
        + code.replace("\x1b", "\\x1b")
        + " "
        + print_color(color_code + 60, "亮" + text)
        + " "
        + print_color(color_code + 10, "底" + text)
        + " "
        + print_color(color_code + 70, "亮底" + text)
        + " "
        + print_color(color_code + 1, "粗" + text)
        + " "
        + print_color(color_code + 3, "斜" + text)
        + " "
        + print_color(color_code + 4, text + "底線")
        + " "
        + print_color(7, "反白" + text)
        + " "  # 反白效果
        + print_color(8, "隱藏" + text)
        + " "  # 隱藏文字
        + print_color(21, "雙下劃線" + text)
        + " "  # 下劃線雙線效果
        + print_color(22, "取消雙下劃線" + text)
        + " "
        + print_color(9, "交叉劃線" + text)
        + " "  # 交叉劃線效果
        + print_color(6, "爆發" + text)
        + " "  # 爆發效果
        + print_color(48, "背景圖案" + text)
        + " "  # 背景圖案
        + print_color(49, "取消背景圖案" + text)  # 取消背景圖案
    )


def print_ansi_colors():
    for i in range(30, 38):
        print(print_color(i, f"ANSI Color {i}"), end="")
        print(print_color_variants(i, f"ANSI Color {i}"))
    print("\n256 Colors:")
    for i in range(256):
        print(f"\x1b[38;5;{i}m {i:03d} \x1b[0m", end="")
        if (i + 1) % 16 == 0:
            print()  # 每16個顏色換一行
    print("\nBasic 16 Colors:")
    for i in range(16):
        print(f"\x1b[48;5;{i}m {i:02X} \x1b[0m", end="")
    print("\n216 Colors:")
    for i in range(16, 232, 36):
        for j in range(36):
            c = i + j
            print(f"\x1b[48;5;{c}m {c:02X} \x1b[0m", end="")
        print()
    print("Grayscale 24 Colors:")
    for i in range(232, 256):
        print(f"\x1b[48;5;{i}m {i:02X} \x1b[0m", end="")


print_ansi_colors()