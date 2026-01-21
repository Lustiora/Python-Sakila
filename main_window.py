# ---------------------------------------------------------
# Import Package
# ---------------------------------------------------------
import psycopg2
import tkinter
from tkinter import messagebox
from window import center_window
from window import set_focus_force
import os
import configparser
import hashlib # 해시값 Encoding
import base64
# ---------------------------------------------------------
# Variable
# ---------------------------------------------------------
count = 3
current_login_data = None
# ---------------------------------------------------------
# Main Window Module
# ---------------------------------------------------------
def run_main():
    main = tkinter.Tk()
    main.title("Sakila")
    center_window(main, 1024, 768, min_size=(1024,768))# -- DB 유령 연결 방지 --
    def on_closing():
        if messagebox.askokcancel("Quit", "Exit?"):
            print("Sakila Exit")
            # conn.close()  # DB 연결 종료
            main.destroy()
    main.protocol("WM_DELETE_WINDOW", on_closing)  # 메인 윈도우의 닫기 프로토콜에 연결
    # ---------------------------------------------------------
    # Main Window GUI
    # ---------------------------------------------------------
    # -- Menubar Start --
    menubar = tkinter.Menu(main)
    # -- Menubar 1 --
    menu1 = tkinter.Menu(menubar, tearoff=0) # tearoff : 하위 메뉴 사용시 활성화
    menu1.add_command(label="상태")
    menu1.add_separator() # 구분선
    menu1.add_command(label="종료", command=on_closing)
    menubar.add_cascade(label="메뉴", menu=menu1)
    # -- Menubar 2 --
    menu2 = tkinter.Menu(menubar, tearoff=0)
    menu2.add_command(label="고객")
    menu2.add_separator()
    menu2.add_command(label="재고")
    menu2.add_separator()
    menu2.add_command(label="영화")
    menu2.add_separator()
    menu2.add_command(label="대여")
    menu2.add_separator()
    menu2.add_command(label="결제")
    menubar.add_cascade(label="조회", menu=menu2)
    # -- Menubar 3 --
    menu3 = tkinter.Menu(menubar, tearoff=0)
    menu3.add_command(label="고객")
    menu3.add_separator()
    menu3.add_command(label="재고")
    menu3.add_separator()
    menu3.add_command(label="영화")
    menu3.add_separator()
    menu3.add_command(label="대여")
    menu3.add_separator()
    menu3.add_command(label="결제")
    menubar.add_cascade(label="변경", menu=menu3)
    # -- Menubar 4 --
    menu4 = tkinter.Menu(menubar, tearoff=0)
    menu4.add_command(label="고객")
    menu4.add_separator()
    menu4.add_command(label="재고")
    menu4.add_separator()
    menu4.add_command(label="영화")
    menu4.add_separator()
    menu4.add_command(label="대여")
    menu4.add_separator()
    menu4.add_command(label="결제")
    menubar.add_cascade(label="삭제", menu=menu4)
    # -- Menubar 5 --
    menu5 = tkinter.Menu(menubar, tearoff=0)
    menu5.add_command(label="고객")
    menu5.add_separator()
    menu5.add_command(label="재고")
    menu5.add_separator()
    menu5.add_command(label="영화")
    menu5.add_separator()
    menu5.add_command(label="배우")
    menu5.add_separator()
    menu5.add_command(label="장르")
    menubar.add_cascade(label="추가", menu=menu5)
    # -- Menubar 6 --
    menu6 = tkinter.Menu(menubar, tearoff=0)
    menu6.add_command(label="대여 / 반납")
    menu6.add_separator()
    menu6.add_command(label="대여 순위")
    menubar.add_cascade(label="통계", menu=menu6)
    # -- Menubar 7 --
    menu7 = tkinter.Menu(menubar, tearoff=0)
    menu7.add_command(label="직원")
    menubar.add_cascade(label="관리", menu=menu7)
    # -- Menubar End --
    main.config(menu=menubar)
    def main_focus_force():
        main.lift()
        main.attributes('-topmost', True)
        main.attributes('-topmost', False)
        main.focus_force() # 강제 포커스 (Entry or window 지정가능)
    main.after(200, main_focus_force)
    main.mainloop()
# ---------------------------------------------------------
# Check Login Process Module
# ---------------------------------------------------------
def main_check_login_process(event = None):
    global current_login_data
    # -- Load Config --
    appdata = os.getenv("APPDATA")
    config_dir = os.path.join(appdata, "sakila", "db")
    config_file = os.path.join(config_dir, "config.ini")
    config = configparser.ConfigParser()
    current_login_data = None
    if config.read(config_file):
        # -- DB Connect --
        login_db = config['DB Connect']['dbname']
        login_host = config['DB Connect']['host']
        login_port = config['DB Connect']['port']
        login_id = config['DB Connect']['user']
        # -- Password Base64 Decode --
        encrypted_pw = config['DB Connect']['password']  # Encode Text Call
        pw_bytes = base64.b64decode(encrypted_pw)  # base64.b64decode Decode
        decrypted_pw = pw_bytes.decode('utf-8')  # utf-8 Decode
        # --
        conn = psycopg2.connect(dbname=login_db,
                                        host=login_host, # Default : localhost
                                        port=login_port, # Default : 5432
                                        user=login_id,
                                        password=decrypted_pw)
        print("DB Connected Main")
        run_main()