text = input("输入文字：")

width = len(text) + 4          # 两边各留 2 格空格
print("+" + "-" * width + "+")
print("|  " + text + "  |")
print("+" + "-" * width + "+")