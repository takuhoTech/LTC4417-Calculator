import tkinter
from PIL import Image, ImageTk
from dataclasses import dataclass

@dataclass
class box:
   num: int
   pos: int

BOX_ACC = box(0,10)
BOX_R1 = box(1,40)
BOX_R2 = box(2,70)
BOX_R3 = box(3,100)
BOX_R12 = box(4,130)
BOX_R23 = box(5,160)
BOX_Rhys = box(6,190)

BOX_UV = box(7,250)
BOX_UVhys = box(8,280)
BOX_OV = box(9,310)
BOX_OVhys = box(10,340)
BOX_UV2 = box(11,250)
BOX_UVhys2 = box(12,280)
BOX_OV2 = box(13,310)
BOX_OVhys2 = box(14,340)

BOX_UVmax2 = box(15,250)
BOX_UVmin2 = box(16,250)
BOX_OVmax2 = box(17,310)
BOX_OVmin2 = box(18,310)

BOX_ERROR = box(20,370)

# クリックイベント
def btn_clear():
   i = 0
   while i <= 18:
      txt[i].delete(0, tkinter.END) # 削除の処理
      i = i + 1
def btn_click():
   # テキスト取得
   ACC = float(txt[BOX_ACC.num].get())
   R1 = float(txt[BOX_R1.num].get())*1000
   R2 = float(txt[BOX_R2.num].get())*1000
   R3 = float(txt[BOX_R3.num].get())*1000
   R12 = float(txt[BOX_R12.num].get())*1000
   R23 = float(txt[BOX_R23.num].get())*1000
   Rhys = float(txt[BOX_Rhys.num].get())*1000

   R123 = R1 + R2 + R3
   R4 = R1 + R2
   if Rhys != 0:
      Ihys = 63.0/(1000.0*Rhys)
      txt[BOX_ERROR.num].delete(0, tkinter.END)
      if (Ihys < 0.000000050) or (Ihys > 0.000000500):
         txt[BOX_ERROR.num].insert(0,"Ihys range error")
      OVhys = Ihys*((R12*R123/R1)+R2+R3)
      UVhys = Ihys*((R23*R123/R4)+R3)
   else:
      OVhys = 0.03
      UVhys = 0.03

   #OV = (R3+R4)/R1
   #UV = (R3+R4)/R4

   INC = 1.0 + ACC/100.0
   DEC = 1.0 - ACC/100.0

   OVmax = 1.0 + (R2+R3)/R1 * (INC/DEC)
   OV = 1.0 + (R2+R3)/R1
   OVmin = 1.0 + (R2+R3)/R1 * (DEC/INC)
   
   UVmax = 1.0 + (R3/(R1+R2)) * (INC/DEC)
   UV = 1.0 + (R3/(R1+R2))
   UVmin = 1.0 + (R3/(R1+R2)) * (DEC/INC)

   i = BOX_UV.num
   while i <= BOX_OVhys2.num:
      txt[i].delete(0, tkinter.END)
      i = i + 1

   txt[BOX_UV.num].insert(0,UV)
   txt[BOX_UVhys.num].insert(0,UVhys)
   txt[BOX_OV.num].insert(0,OV)
   txt[BOX_OVhys.num].insert(0,OVhys)
   txt[BOX_UV2.num].insert(0,UV/2.0)
   txt[BOX_UVhys2.num].insert(0,UVhys/2.0)
   txt[BOX_OV2.num].insert(0,OV/2.0)
   txt[BOX_OVhys2.num].insert(0,OVhys/2.0)


   txt[BOX_UVmax2.num].insert(0,UVmax/2.0)
   txt[BOX_UVmin2.num].insert(0,UVmin/2.0)
   txt[BOX_OVmax2.num].insert(0,OVmax/2.0)
   txt[BOX_OVmin2.num].insert(0,OVmin/2.0)

# 画面作成
tki = tkinter.Tk()
tki.geometry('750x400')
tki.title('LTC4417のOV/UVしきい値とヒステリシス電圧の計算機')
# ラベル
tkinter.Label(text='抵抗精度').place(x=30, y=BOX_ACC.pos)
tkinter.Label(text='%').place(x=250, y=BOX_ACC.pos)

tkinter.Label(text='R1').place(x=30, y=BOX_R1.pos)
tkinter.Label(text='R2').place(x=30, y=BOX_R2.pos)
tkinter.Label(text='R3').place(x=30, y=BOX_R3.pos)
tkinter.Label(text='R12').place(x=30, y=BOX_R12.pos)
tkinter.Label(text='R23').place(x=30, y=BOX_R23.pos)
tkinter.Label(text='R(HYSピン)').place(x=30, y=BOX_Rhys.pos)
i = 0
while i <= BOX_Rhys.num-BOX_R1.num:
   tkinter.Label(text='kΩ').place(x=250, y=BOX_R1.pos+30*i)
   i = i + 1

tkinter.Label(text='UV').place(x=30, y=BOX_UV.pos)
tkinter.Label(text='UVヒステリシス').place(x=30, y=BOX_UVhys.pos)
tkinter.Label(text='OV').place(x=30, y=BOX_OV.pos)
tkinter.Label(text='OVヒステリシス').place(x=30, y=BOX_OVhys.pos)

tkinter.Label(text='Error').place(x=30, y=BOX_ERROR.pos)

#i = 0
#while i <= BOX_OVhys.num-BOX_UV.num:
   #tkinter.Label(text='/2=').place(x=250, y=BOX_UV.pos+30*i)
   #tkinter.Label(text='V').place(x=410, y=BOX_UV.pos+30*i)
   #i = i + 1
tkinter.Label(text='/2=').place(x=230, y=BOX_UVhys.pos)
tkinter.Label(text='/2=').place(x=230, y=BOX_OVhys.pos)
tkinter.Label(text='/2=').place(x=230, y=BOX_UV.pos)
tkinter.Label(text='/2=').place(x=230, y=BOX_OV.pos)

tkinter.Label(text='<=').place(x=400, y=BOX_UV.pos)
tkinter.Label(text='<=').place(x=400, y=BOX_OV.pos)
tkinter.Label(text='<=').place(x=550, y=BOX_UV.pos)
tkinter.Label(text='<=').place(x=550, y=BOX_OV.pos)
tkinter.Label(text='V').place(x=700, y=BOX_UV.pos)
tkinter.Label(text='V').place(x=700, y=BOX_OV.pos)

# テキストボックス
txt = [0]*100

txt[BOX_ACC.num] = tkinter.Entry(width=20)
txt[BOX_ACC.num].place(x=120, y=BOX_ACC.pos)
txt[BOX_R1.num] = tkinter.Entry(width=20)
txt[BOX_R1.num].place(x=120, y=BOX_R1.pos)
txt[BOX_R2.num] = tkinter.Entry(width=20)
txt[BOX_R2.num].place(x=120, y=BOX_R2.pos)
txt[BOX_R3.num] = tkinter.Entry(width=20)
txt[BOX_R3.num].place(x=120, y=BOX_R3.pos)
txt[BOX_R12.num] = tkinter.Entry(width=20)
txt[BOX_R12.num].place(x=120, y=BOX_R12.pos)
txt[BOX_R23.num] = tkinter.Entry(width=20)
txt[BOX_R23.num].place(x=120, y=BOX_R23.pos)
txt[BOX_Rhys.num] = tkinter.Entry(width=20)
txt[BOX_Rhys.num].place(x=120, y=BOX_Rhys.pos)

txt[BOX_UV.num] = tkinter.Entry(width=15)
txt[BOX_UV.num].place(x=120, y=BOX_UV.pos)
txt[BOX_UVhys.num] = tkinter.Entry(width=15)
txt[BOX_UVhys.num].place(x=120, y=BOX_UVhys.pos)
txt[BOX_OV.num] = tkinter.Entry(width=15)
txt[BOX_OV.num].place(x=120, y=BOX_OV.pos)
txt[BOX_OVhys.num] = tkinter.Entry(width=15)
txt[BOX_OVhys.num].place(x=120, y=BOX_OVhys.pos)

txt[BOX_UV2.num] = tkinter.Entry(width=15)
txt[BOX_UV2.num].place(x=440, y=BOX_UV2.pos)
txt[BOX_UVhys2.num] = tkinter.Entry(width=15)
txt[BOX_UVhys2.num].place(x=280, y=BOX_UVhys2.pos)
txt[BOX_OV2.num] = tkinter.Entry(width=15)
txt[BOX_OV2.num].place(x=440, y=BOX_OV2.pos)
txt[BOX_OVhys2.num] = tkinter.Entry(width=15)
txt[BOX_OVhys2.num].place(x=280, y=BOX_OVhys2.pos)

txt[BOX_ERROR.num] = tkinter.Entry(width=60)
txt[BOX_ERROR.num].place(x=120, y=BOX_ERROR.pos)

txt[BOX_UVmax2.num] = tkinter.Entry(width=15)
txt[BOX_UVmax2.num].place(x=600, y=BOX_UVmax2.pos)
txt[BOX_UVmin2.num] = tkinter.Entry(width=15)
txt[BOX_UVmin2.num].place(x=280, y=BOX_UVmin2.pos)
txt[BOX_OVmax2.num] = tkinter.Entry(width=15)
txt[BOX_OVmax2.num].place(x=600, y=BOX_OVmax2.pos)
txt[BOX_OVmin2.num] = tkinter.Entry(width=15)
txt[BOX_OVmin2.num].place(x=280, y=BOX_OVmin2.pos)
# ボタン
btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=170, y=215)

btn = tkinter.Button(tki, text='クリア', command=btn_clear)
btn.place(x=260, y=215) # xが横,yが縦
# 画面をそのまま表示

img = Image.open('img.png')        # 画像ファイルを開き、ファイル情報取得。text.jpgは任意に設定
img = img.resize((img.width // 4, img.height // 4))
tk_img = ImageTk.PhotoImage(img)
img_width, img_height = img.size

canvas = tkinter.Canvas(tki, width=img_width, height=img_height)        # 画像表示エリアの作成
#canvas.pack()
canvas.place(x=400, y=20)
canvas.create_image(0, 0 , anchor = tkinter.NW, image=tk_img)        # 画像表示

tki.mainloop()