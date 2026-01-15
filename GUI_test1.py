import tkinter # Python 기본 GUI Package
from tkinter import messagebox # 팝업창 GUI Package
######################################
# Login 모듈 (from tkinter import messagebox)
count = 3
def user_login(event=None): # event=None을 추가하여 event값 입력 받음을 선언
    global count
    login_id = user_id.get()
    login_pw = user_pw.get()
    print(f"ID : {login_id} | PW : {login_pw}")
    print("DB Connected ...")
    count = count - 1
    if login_id == "lus" or login_pw == "tiger": # 일치조건 > DB 연동 예정
        print("Login Successful")
        messagebox.showinfo("Login", "Login Successful")
        login.destroy() # Window (Login) 종료
        run_main()
    else:
        print("Login Failed")
        messagebox.showinfo("Login", f"Login Failed\nChance(3) : {count}")
    if count == 0:
        messagebox.showinfo("Login", "Please Contact the Administrator")
        print("Not Connected")
        login.destroy()
######################################
# Window (Main) 모듈 (tkinter)
def run_main():
    main = tkinter.Tk()
    main.title("Sakila DB")
    center_window(main, 600, 400)
    ######################################
    # 입력값 검사 모듈
    def check_digit(incoming): # incoming: 사용자가 입력을 마친 후의 '결과값' (%P)
        if incoming.isdigit() or incoming == "": # 숫자이거나, 다 지워서 빈칸("")이면 -> 허용(True)
            return True
        else:
            return False
    validation = main.register(check_digit)
    ######################################
    # DB 조회 모듈
    def search_db():
        customer = customer_date.get() # .get().strip() > 입력받은 customer_date를 가져오고 앞뒤 공백 제거 > 앞뒤 공백 제거 부분은 검사 모듈과 겹치기에 삭제
        print(f"Customer ID Check ... {customer}")
    search_frame = tkinter.LabelFrame(main, text="Customer Search")
    search_frame.pack(fill="x", padx=5, pady=5) # pack(fill="x") > width = 최대치
    tkinter.Label(search_frame, text="Customer ID :").pack(side="left", padx=5, pady=5) # grid 대신 pack 사용 / side="left" > 읽는 순서대로 좌측 정렬
    customer_date = tkinter.Entry(search_frame, validate="key", validatecommand=(validation, '%P'))
    # validate="key" > 입력값 상시확인 / validatecommand=(validation, '%P') > check_digit 모듈을 통과하는 입력값(%p)만 허용
    customer_date.pack(side="left", padx=5, pady=5)
    tkinter.Button(search_frame, text="Search", command=search_db).pack(side="left", padx=5, pady=5)
    main.mainloop()
######################################
# Window 자동 중앙 정렬 모듈 (미정렬 시 좌측 상단) (tkinter)
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth() # 현재 모니터의 해상도(크기)를 가져옴
    screen_height = window.winfo_screenheight()
    x_pos = (screen_width // 2) - (width // 2) # 정중앙 좌표 계산 \ (//)는 정수 나누기
    y_pos = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x_pos}+{y_pos}") # 위치 적용 (가로x세로+X좌표+Y좌표)
    window.resizable(False, False) # Window Size 변동 금지 (가로, 세로)
# 적용 > center_window([tkinter Window],[width],[height])
######################################
# 변수명 지정 없이 tkinter.Tk()로 작성하면 해당하는 속성이 포함된 창 3개가 출력
# tkinter.Tk().title("DVD")
# tkinter.Tk().geometry("500x500")
# tkinter.Tk().mainloop()
######################################
# tkinter Package 에서는 불가능한 방식 -> return self 없음 -> 한줄에 하나의 속성만 사용가능
# tkinter.Tk().title("PU").geometry("500x500").mainloop()
######################################
# Window (Login)
login = tkinter.Tk() # 표사되는 Window(tkinter.Tk())에 변수명을 지정하여 변수명을 기준으로 속성을 추가
login.title("Sakila Login")
center_window(login, 260, 100)
######################################
# Login 화면 구성 grid
tkinter.Label(login, text="Username").grid(row=0, column=0, padx=5, pady=5, sticky="e")
user_id = tkinter.Entry(login) # Entry -> 입력칸 | 입력된 값을 사용하기 위해 변수명 지정 필요
user_id.grid(row=0, column=1, padx=10, pady=5)
login.grid_columnconfigure(0, weight=1) # ([열],[배당 비율])
tkinter.Label(login, text="Password").grid(row=1, column=0, padx=5, pady=5, sticky="e")
user_pw = tkinter.Entry(login, show="*") # show="*" > 유출 방지 : 입력값 * 대체 출력
user_pw.grid(row=1, column=1, padx=10, pady=5)
user_pw.bind("<Return>", user_login) # Enter key 입력으로 Login 모듈 동작 ("[입력키]", [모듈])
login.grid_columnconfigure(1, weight=1)
tkinter.Button(login, text="Login", command=user_login).grid(row=2, column=0, columnspan=2, padx=10, pady=3, sticky="ew") # command=[클릭시 동작내용] | sticky="e" > 우측 정렬
# row=[행], column=[열]) > 0행 0열 = 좌측 상단 / 행과 열이 겹치는 경우 덮어씌워짐
# padx=[좌측우측외부여백], pady=[상단하단외부여백], ipa~=[내부여백]
# 상세 정리 : https://puliseul.tistory.com/81
######################################
login.mainloop() # root(Window)를 지속적으로 반복 실행 (종료방지)
######################################