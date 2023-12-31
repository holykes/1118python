### 버튼 클릭시 이미지 표시하기 1
from tkinter import *

if __name__ == "__main__":
    # 창 만들기
    w = Tk()

    # 창 크기 및 제목 설정하기
    w.title("현재 날씨 조회")
    w.geometry("500x400")

    # 이미지가 표시될 레이블
    image_weather = Label(w)
    # 버튼
    btn=Button(w,text="클릭")

    def change_image(event):
        # 윈도우에 표시할 이미지 로드
        img = PhotoImage(file="current_weather.png")   # img는 지역 변수이다.
        # GUI 업데이트
        image_weather.config(image=img)
        # 이미지가 레이블에 표시될 동안에는 해당 이미지 객체가 계속해서 참조되어야 합니다. image_weather.image = img는 이 참조를 유지시켜주는 역할을 한다.이 부분이 생략되면, 이미지 객체는 참조되지 않아 가비지 컬렉션에 의해 소멸된다.
        image_weather.image = img

    # 윈도우에 위젯 배치하기
    image_weather.pack()
    btn.bind("<Button>",change_image)
    btn.pack()


    # 창이 닫히지 않게 대기 상태로 만들기
    w.mainloop()


### 버튼 클릭시 이미지 표시하기 2
### PhotoImage 객체를 참조하는 변수를 global로 선언하면 image_weather.image = img는 필요 없다.
from tkinter import *

if __name__ == "__main__":
    # 창 만들기
    w = Tk()

    # 창 크기 및 제목 설정하기
    w.title("현재 날씨 조회")
    w.geometry("500x400")

    # 이미지가 표시될 레이블
    image_weather = Label(w)
    # 버튼
    btn=Button(w,text="클릭")

    # 이미지 객체의 변수 선언
    img=None
    def change_image(event):
        # img를 global로 선언
        global img
        # 윈도우에 표시할 이미지 로드
        img = PhotoImage(file="current_weather.png")   # img는 지역 변수이다.
        # GUI 업데이트
        image_weather.config(image=img)

    # 윈도우에 위젯 배치하기
    image_weather.pack()
    btn.bind("<Button>",change_image)
    btn.pack()


    # 창이 닫히지 않게 대기 상태로 만들기
    w.mainloop()