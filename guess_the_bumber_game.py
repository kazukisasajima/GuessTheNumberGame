import random

def guess_the_number_game():
    # ユーザーに最小数と最大数を入力させる
    while True:
        try:
            n = int(input("最小数を入力してください: "))
            m = int(input("最大数を入力してください: "))
            if n > m:
                print("最大数は最小数よりも大きい数字を入力してください：")
            else:
                break
        except ValueError:
            print("整数を入力してください")

    # n から m の範囲内で乱数を生成
    target_number = random.randint(n, m)
    max_attempts = 10  # 試行回数の制限を設定

    print(f"{n}から{m}までの数字を当ててください. 試行回数は{max_attempts}回までです")

    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f"{attempt}回目: 予想した数字を入力してください: "))
                break
            except ValueError:
                print("整数を入力してください:")

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"おめでとうございます!{attempt}回目で正解しました！")
            break
    else:
        print(f"試行回数が{max_attempts}回になりました。正解は{target_number}でした。")

if __name__ == "__main__":
    guess_the_number_game()
