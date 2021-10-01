from tkinter import*
from tkinter import messagebox

window = Tk()

window.title("STAR COFFEE")
window.geometry("650x950+100+100")
window.resizable(False, False)
window.configure(background='white')

label = Label(window, font=7, height=2, width=50, text = "주문하려는 메뉴를 클릭해 주세요", bg='green')
label.config(fg='white', anchor=CENTER)
label.pack()

n = 0
mon = 0

class menu:
    def __init__(self, window):
        self.buttonframe = Frame(window, bg='white')
        self.buttonframe.pack(fill =X, anchor=N)
        self.button_a = Button(self.buttonframe, text="에스프레소", width = 12, command=Espresso)
        self.button_a.pack(side = LEFT, padx = 10, pady=10)
        self.button_b = Button(self.buttonframe, text="프라푸치노", width=12, command=Frappuccino)
        self.button_b.pack(side=LEFT, padx = 10,pady=10)
        self.button_c = Button(self.buttonframe, text="블렌디드",width=12, command=blend)
        self.button_c.pack(side=LEFT, padx = 10, pady=10)
        self.button_d = Button(self.buttonframe, text="피지오", width=12, command=Fizzio)
        self.button_d.pack(side=LEFT, padx = 10, pady=10)
        self.button_e = Button(self.buttonframe, text="티", width=12, command=Tea)
        self.button_e.pack(side=LEFT, padx = 10, pady=10)

def credit():
    res = messagebox.askokcancel('질문 메시지', '결제하시겠습니까?')

def money1():
    global n, mon
    n = n+1
    num.configure(text=n)
    mon = mon + 4100
    total.configure(text=mon)
    
def money2():
    global n, mon
    n = n+1
    num.configure(text=n)
    mon = mon + 4600
    total.configure(text=mon)

def money3():
    global n, mon
    n = n+1
    num.configure(text=n)
    mon = mon + 5400
    total.configure(text=mon)

def money4():
    global n, mon
    n = n+1
    num.configure(text=n)
    mon = mon + 5600
    total.configure(text=mon)

def money5():
    global n, mon
    n = n+1
    num.configure(text=n)
    mon = mon + 6100
    total.configure(text=mon)

def money6():
    global n, mon
    n = n+1
    num.configure(text=n)
    mon = mon + 6300
    total.configure(text=mon)

def reset():
    global n, mon
    n = 0
    num.configure(text=n)
    mon=0
    total.configure(text=mon)

button_f = Button(window, text='-')
button_f.place(x=30, y = 110)
button_g = Button(window, text="+")
button_g.place(x=160, y = 110)
num = Button(window, width=10, text=n,bg='white')
num.place(x=60, y = 110)
button_h = Button(window, text="결제하기", width=10, height=2, command=credit)
button_h.place(x=500, y=100)
total = Button(window, width=20, text=mon, bg='white')
total.place(x=310, y=110)
retry = Button(window, text='초기화', command=reset)
retry.place(x=200, y=110)

def Espresso():
    americano = '카페 아메리카노.png'
    photo=PhotoImage(file=americano)
    slabel = Label(window, image=photo, width=250, height=270)
    slabel.place(x=40, y=190)
    caramel = '카라멜 마키아또.png'
    photo=PhotoImage(file=caramel)
    slabel = Label(window, image=photo, width=250, height=270)
    slabel.place(x=350, y=190)
    latte = '카페 라떼.png'
    photo=PhotoImage(file=latte)
    slabel = Label(window, image=photo, width=250, height=270)
    slabel.place(x=40, y=560)
    cappuccino = '카푸치노.png'
    photo=PhotoImage(file=cappuccino)
    slabel = Label(window, image=photo, width=250, height=270)
    slabel.place(x=350, y=560)

    btn1=Button(window, text="카페 아메리카노", width=35, command=money1)
    btn1.place(x=20, y=470)
    btn2=Button(window, text="카라멜 마키아또", width=35, command=money4)
    btn2.place(x=330, y=470)
    btn3=Button(window, text="카페 라떼",width=35, command=money2)
    btn3.place(x=20, y=840)
    btn4=Button(window, text="카푸치노", width=35, command=money2)
    btn4.place(x=330, y=840)

    btn_1=Button(window, text="4100원", width=7)
    btn_1.place(x=130, y=510)
    btn_2=Button(window, text="5600원", width=7)
    btn_2.place(x=445, y=510)
    btn_3=Button(window, text="4600원", width=7)
    btn_3.place(x=130, y=880)
    btn_4=Button(window, text="4600원", width=7)
    btn_4.place(x=445, y=880)


def Frappuccino():
    chocolate = '초콜릿 크림 프라푸치노.png'
    photo=PhotoImage(file=chocolate)
    blabel = Label(window, image=photo, width=250, height=270)
    blabel.place(x=40, y=190)
    malcha = '제주 유기농 말차로 만든 크림 프라푸치노.png'
    photo=PhotoImage(file=malcha)
    blabel = Label(window, image=photo, width=250, height=270)
    blabel.place(x=350, y=190)
    javachip = '자바 칩 프라푸치노.png'
    photo=PhotoImage(file=javachip)
    blabel = Label(window, image=photo, width=250, height=270)
    blabel.place(x=40, y=560)
    pistachio = '피스타치오 크림 프라푸치노.png'
    photo=PhotoImage(file=pistachio)
    blabel = Label(window, image=photo, width=250, height=270)
    blabel.place(x=350, y=560)

    btn5=Button(window, text="초콜릿 크림 프라푸치노",width=35, command=money4)
    btn5.place(x=20, y=470)
    btn6=Button(window, text="제주 유기농 말차로 만든 크림 프라푸치노",width=35, command=money6)
    btn6.place(x=330, y=470)
    btn7=Button(window, text="자바 칩 프라푸치노",width=35, command=money5)
    btn7.place(x=20, y=840)
    btn8=Button(window, text="피스타치오 크림 프라푸치노",width=35, command=money6)
    btn8.place(x=330, y=840)

    btn_5=Button(window, text="5600원", width=7)
    btn_5.place(x=130, y=510)
    btn_6=Button(window, text="6300원", width=7)
    btn_6.place(x=445, y=510)
    btn_7=Button(window, text="6100원", width=7)
    btn_7.place(x=130, y=880)
    btn_8=Button(window, text="6300원", width=7)
    btn_8.place(x=445, y=880)

def blend():
    strawberry = '딸기 요거트 블렌디드.png'
    photo=PhotoImage(file=strawberry)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=40, y=190)
    mango = '망고 패션 후르츠 블렌디드.png'
    photo=PhotoImage(file=mango)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=350, y=190)
    grapefruit = '자몽 셔벗 블렌디드.png'
    photo=PhotoImage(file=grapefruit)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=40, y=560)
    extreme = '익스트림 티 블렌디드.png'
    photo=PhotoImage(file=extreme)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=350, y=560)

    btn9=Button(window, text="딸기 요거트 블렌디드", width=35, command=money6)
    btn9.place(x=20, y=470)
    btn10=Button(window, text="망고 패션 후르츠 블렌디드", width=35, command=money4)
    btn10.place(x=330, y=470)
    btn11=Button(window, text="자몽 셔벗 블렌디드", width=35, command=money5)
    btn11.place(x=20, y=840)
    btn12=Button(window, text="익스트림 티 블렌디드", width=35, command=money6)
    btn12.place(x=330, y=840)

    btn_9=Button(window, text="6300원", width=7)
    btn_9.place(x=130, y=510)
    btn_10=Button(window, text="5400원", width=7)
    btn_10.place(x=445, y=510)
    btn_11=Button(window, text="6100원", width=7)
    btn_11.place(x=130, y=880)
    btn_12=Button(window, text="6300원", width=7)
    btn_12.place(x=445, y=880)

def Fizzio():
    coollime = '쿨 라임 피지오.png'
    photo=PhotoImage(file=coollime)
    alabel = Label(window, image=photo, width=200, height=270)
    alabel.place(x=40, y=190)
    fashion = '패션 탱고 티 레모네이드 피지오.png'
    photo=PhotoImage(file=fashion)
    blabel = Label(window, image=photo, width=200, height=270)
    blabel.place(x=350, y=190)
    black = '블랙 티 레모네이드 피지오.png'
    photo=PhotoImage(file=black)
    clabel = Label(window, image=photo, width=200, height=270)
    clabel.place(x=40, y=560)
    magic = '매직 팝 스플래쉬 피지오.png'
    photo=PhotoImage(file=magic)
    dlabel = Label(window, image=photo, width=200, height=270)
    dlabel.place(x=350, y=560)

    btn13=Button(window, text="쿨 라임 피지오",width=35, command=money5)
    btn13.place(x=20, y=470)
    btn14=Button(window, text="패션 탱고 티 레모네이드 피지오",width=35, command=money3)
    btn14.place(x=330, y=470)
    btn15=Button(window, text="블랙 티 레모네이드 피지오",width=35, command=money3)
    btn15.place(x=20, y=840)
    btn16=Button(window, text="매직 팝 스플래쉬 피지오",width=35, command=money3)
    btn16.place(x=330, y=840)

    btn_13=Button(window, text="6100원", width=7)
    btn_13.place(x=130, y=510)
    btn_14=Button(window, text="5400원", width=7)
    btn_14.place(x=445, y=510)
    btn_15=Button(window, text="5400원", width=7)
    btn_15.place(x=130, y=880)
    btn_16=Button(window, text="5400원", width=7)
    btn_16.place(x=445, y=880)
        
def Tea():
    mint = '민트 블랜드 티.png'
    photo=PhotoImage(file=mint)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=40, y=190)
    lime = '라임 패션 티.png'
    photo=PhotoImage(file=lime)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=350, y=190)
    apple = '그랜마 애플 블랙 티.png'
    photo=PhotoImage(file=apple)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=40, y=560)
    chamomile = '캐모마일 블렌드 티.png'
    photo=PhotoImage(file=chamomile)
    slabel = Label(window, image=photo, width=200, height=270)
    slabel.place(x=350, y=560)

    btn17=Button(window, text="민트 블랜드 티",width=35, command=money1)
    btn17.place(x=20, y=470)
    btn18=Button(window, text="라임 패션 티",width=35, command=money3)
    btn18.place(x=330, y=470)
    btn19=Button(window, text="그랜마 애플 블랙 티",width=35, command=money3)
    btn19.place(x=20, y=840)
    btn20=Button(window, text="캐모마일 블렌드 티",width=35, command=money1)
    btn20.place(x=330, y=840)

    btn_17=Button(window, text="4100원", width=7)
    btn_17.place(x=130, y=510)
    btn_18=Button(window, text="5400원", width=7)
    btn_18.place(x=445, y=510)
    btn_19=Button(window, text="5400원", width=7)
    btn_19.place(x=130, y=880)
    btn_20=Button(window, text="4100원", width=7)
    btn_20.place(x=445, y=880)
        

espressomenu = menu(window)

window.mainloop()

