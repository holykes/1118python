#### weatherAPI로 날씨 앱 만들기 ####

# 모듈 import
from tkinter import *
from tkinter import messagebox
import requests

# 프로그램 시작
if __name__ == "__main__":
    # 창 만들기
    w = Tk()

    # 창 크기 및 제목 설정하기
    w.title("현재 날씨 조회")
    w.geometry("500x400")

    # weatherAPI에서 날씨 정보 받기
    def get_weather(event):
        # 엔트리 상자의 값을 가져와 city 변수에 저장
        city = entry_city.get()
        # API key
        key = "자신의 api key"

        # 서버에 데이터 요청
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}")
        if response.status_code == 200:
            # 응답받은 데이터를 파이썬 자료형으로 변환
            weather = response.json()
            # 날씨 이미지가 있는 주소 생성
            icon_addr = "https:" + weather['current']['condition']['icon']
            # 주소에 요청 보내고 이미지 받기
            img = requests.get(icon_addr)
            # 이미지 저장하기
            with open("current_weather.png", "wb") as f:
                f.write(img.content)

            # 윈도우에 표시할 이미지 로드
            img = PhotoImage(file="current_weather.png")
            # GUI 업데이트
            label_country.config(text=weather['location']['country'] + '\n' + weather['location']['name'])
            label_temp.config(text=str(weather['current']['temp_c']) + "℃")
            label_condition.config(text=weather['current']['condition']['text'])
            image_weather.config(image=img)
            image_weather.image = img
            entry_city.delete(0, END)
        elif response.status_code == 400:
            messagebox.showinfo("지명 오류", "입력한 지명이 없습니다.")
            entry_city.delete(0, END)
        else:
            messagebox.showinfo("접속 오류", "서버에 접속할 수 없습니다.")
            entry_city.delete(0, END)


    # 위젯 생성
    # 제목
    label_search = Label(w, padx=10, pady=20, font=("맑은 고딕", 12), text="검색할 도시(지역)을 입력하고 엔터를 누르세요.")
    # 검색어 입력 상자
    entry_city = Entry(w, width=20, font=("hy견고딕", 20), justify="center")
    # 도시명이 표시될 레이블
    label_country = Label(w, font=("hy견고딕", 20), fg="red", height=2)
    # 기온이 표시될 레이블
    label_temp = Label(w, font=("hy견고딕", 20), fg="red", height=2)
    # 날씨 상태가 표시될 레이블
    label_condition = Label(w, font=("hy견고딕", 20), fg="red", height=2)
    # 이미지가 표시될 레이블
    image_weather = Label(w)

    # 윈도우에 위젯 배치하기
    label_search.pack()
    entry_city.pack()
    label_country.pack()
    label_temp.pack()
    label_condition.pack()
    image_weather.pack()

    # 이벤트 지정
    w.bind("<Return>", get_weather)

    # 창이 닫히지 않게 대기 상태로 만들기
    w.mainloop()
