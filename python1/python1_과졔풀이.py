###1. 동전교환 프로그램
money=int(input("금액 입력: "))
m500=money//500
m100=money%500//100
m50=money%500%100//50
m10=money%500%100%50//10
m1=money%500%100%50%10
print(f"500원짜리 :{m500}")
print(f"100원짜리 :{m100}")
print(f"50원짜리 :{m50}")
print(f"10원짜리 :{m10}")
print(f"나머지 돈 :{m1}")

###2. 띠찾기
animals="원숭이 닭 개 돼지 쥐 소 호랑이 토끼 용 뱀 말 양".split()
year=int(input("태어난 연도 입력: "))
animal=animals[year%12]
print(f"{year}년은 {animal}띠입니다.")

###3. 음식 궁합
foods={"떢볶이":"오뎅","짜장면":"단무지","라면":"김치","피자":"피클","맥주":"땅콩","치킨":"무","삼겹살":"상추"}
print(list(foods.keys()),end='')
food=input("중 좋아하는 음식은?")
print(f'"{food}"에는 "{foods[food]}"입니다.')

###4. 뻐꾸기 노래
time=input("현재 시간 입력: ")

if time[-2:]=="00":
    print("뻐꾸기가 노래를 시작합니다.")
else:
    print("정각이 아닙니다.")


###5. 중복되지 않은 5개의 정수 입력받아 출력하기
nums=set()

while len(nums)<5:
    num=int(input("정수 입력: "))
    nums.add(num)

print(nums)
