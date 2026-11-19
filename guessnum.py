import random

def guess_number():
    print("欢迎来到猜数字游戏！")
    
    
    # 随机生成 1-100 之间的数字
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7  # 7次机会，因为 2^7=128 > 100
    
    print(f"我心里想了一个 1 到 100 之间的数字")
    print(f"你有 {max_attempts} 次机会猜中它！\n")
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts
        
        try:
            guess = int(input(f"第 {attempts} 次猜测（还剩 {remaining} 次）："))
        except ValueError:
            print("请输入一个整数\n")
            attempts = attempts - 1  # 输入错误不消耗次数
            continue
        
        # 判断
        if guess == secret:
            print(f"\n恭喜你！用了 {attempts} 次就猜中了！")
            if attempts == 1:
                print("你居然一次就中！")
            elif attempts <= 3:
                print("三次以内猜对直觉也很厉害！")
            elif attempts <= 5:
                print("不错不错，稳扎稳打！")
            else:
                print("惊险过关，差点就输了！")
            return
        elif guess < secret:
            print("你猜小了，可以往大猜~\n")
        else:
            print("你猜大了，可以往小猜~\n")
    
    print(f"\n💀 机会用完了！那个数字其实是 {secret}")
    print("下次好运~")

def main():
    while True:
        guess_number()
        again = input("\n要再来一局吗？(y/n)：").strip().lower()
        if again != 'y':
            print("👋 拜拜，下次再玩！")
            break

main()