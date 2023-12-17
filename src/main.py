import tkinter
from PIL import Image, ImageTk
# クリックイベント
def btn_clear():
   i = 1
   while i <= 10:
      txt[i].delete(0, tkinter.END) # 削除の処理
      i = i + 1
def btn_click():
   # テキスト取得
   R1 = float(txt[1].get())*1000
   R2 = float(txt[2].get())*1000
   R3 = float(txt[3].get())*1000
   R12 = float(txt[4].get())*1000
   R23 = float(txt[5].get())*1000
   Rhys = float(txt[6].get())*1000

   Ihys = 63.0/(1000.0*Rhys)

   R123 = R1 + R2 + R3
   R4 = R1 + R2
   OVhys = Ihys*((R12*R123/R1)+R2+R3)
   UVhys = Ihys*((R23*R123/R4)+R3)

   OV = (R3+R4)/R1
   UV = (R3+R4)/R4

   txt[7].insert(0,UV)
   txt[8].insert(0,str(UVhys))
   txt[9].insert(0,OV)
   txt[10].insert(0,str(OVhys))

# 画面作成
tki = tkinter.Tk()
tki.geometry('700x450')
tki.title('LTC4417のOV/UVしきい値とヒステリシス電圧の計算機')
# ラベル
tkinter.Label(text='R1').place(x=30, y=70)
tkinter.Label(text='R2').place(x=30, y=100)
tkinter.Label(text='R3').place(x=30, y=130)
tkinter.Label(text='R12').place(x=30, y=160)
tkinter.Label(text='R23').place(x=30, y=190)
tkinter.Label(text='R(HYSピン)').place(x=30, y=220)

i = 0
while i <= 5:
   tkinter.Label(text='kΩ').place(x=250, y=70+30*i)
   i = i + 1

tkinter.Label(text='UV').place(x=30, y=280)
tkinter.Label(text='UVヒステリシス').place(x=30, y=310)
tkinter.Label(text='OV').place(x=30, y=340)
tkinter.Label(text='OVヒステリシス').place(x=30, y=370)

i = 0
while i <= 3:
   tkinter.Label(text='V').place(x=250, y=280+30*i)
   i = i + 1

# テキストボックス
txt = [0]*11

txt[1] = tkinter.Entry(width=20)
txt[1].place(x=120, y=70)
txt[2] = tkinter.Entry(width=20)
txt[2].place(x=120, y=100)
txt[3] = tkinter.Entry(width=20)
txt[3].place(x=120, y=130)
txt[4] = tkinter.Entry(width=20)
txt[4].place(x=120, y=160)
txt[5] = tkinter.Entry(width=20)
txt[5].place(x=120, y=190)
txt[6] = tkinter.Entry(width=20)
txt[6].place(x=120, y=220)

txt[7] = tkinter.Entry(width=20)
txt[7].place(x=120, y=280)
txt[8] = tkinter.Entry(width=20)
txt[8].place(x=120, y=310)
txt[9] = tkinter.Entry(width=20)
txt[9].place(x=120, y=340)
txt[10] = tkinter.Entry(width=20)
txt[10].place(x=120, y=370)

# ボタン
btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=170, y=245)

btn = tkinter.Button(tki, text='クリア', command=btn_clear)
btn.place(x=260, y=245) # xが横,yが縦
# 画面をそのまま表示

img = Image.open('img.png')        # 画像ファイルを開き、ファイル情報取得。text.jpgは任意に設定
img = img.resize((img.width // 3, img.height // 3))
tk_img = ImageTk.PhotoImage(img)
img_width, img_height = img.size

canvas = tkinter.Canvas(tki, width=img_width, height=img_height)        # 画像表示エリアの作成
#canvas.pack()
canvas.place(x=330, y=60)
canvas.create_image(0, 0 , anchor = tkinter.NW, image=tk_img)        # 画像表示

tki.mainloop()