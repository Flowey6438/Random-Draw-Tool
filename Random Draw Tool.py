import random

def draw_lots(candidates):
    if candidates:
        chosen = random.choice(candidates)
        print(f"抽签结果是：{chosen}")
    else:
        print("候选项为空，请输入有效的候选项。")

if __name__ == "__main__":
    print("欢迎使用抽签小工具！")
    candidates = input("请输入候选项（用逗号分隔）：").split(',')
    candidates = [candidate.strip() for candidate in candidates if candidate.strip()]

    if candidates:
        draw_lots(candidates)
    else:
        print("没有有效的候选项，请重新运行程序。")
