import random

while True:
    man = input('가위 바위 보 선택(종료는 엔터): ')
    if man == '': break
    if man not in ['가위', '바위', '보']:
        print('다시 입력하세요.')
        continue
    com = random.choice(['가위', '바위', '보'])
    # 무승부 조건
    if man == com:
        print('무승부')
    # 승 조건
    elif (man == '가위' and com == '보') or (man == '바위' and com == '가위') or (man == '보' and com == '바위'):
        print('승')
    # 패 
    else:
        print('무승부')
    print('-' * 50)
    print(f'컴퓨터:{com}, 사람:{man}')
    print('-' * 50)
