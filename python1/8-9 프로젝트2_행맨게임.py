import time
import random

print("게임이 시작됩니다.")
time.sleep(1)

answers = ['orange', 'tiger', 'bank', 'world', 'cosmos']
answer = random.choice(answers)
mychars = ''
chance = 10

print('_ ' * len(answer))

while chance >0:
    success = 1
    char = input("추측 문자 입력: ").lower()
    mychars += char[0]
    chance -= 1
    print(f'남은 기회는 {chance}번 입니다.')
    for w in answer:
        if w in mychars:
            print(w, end=' ')
        else:
            print('_', end=" ")
            success = 0
    print()

    if success == 1:
        print("축하합니다!")
        break

if chance == 0:
    print(f"게임 오버! 정답은 '{answer}'입니다.")
