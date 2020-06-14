import tkinter as tk
import tkinter.filedialog as tkfiledialog
import qrcode
from PIL import Image
# 生成面板
window = tk.Tk()
# 面板名字
window.title('二维码生成器')
# 面板大小
window.geometry('300x300')

text = tk.Label(window,text='输入信息',font=20)
text.place(x=120,y=30,anchor='nw')
inputs = tk.Entry(window,show=None,font=16)
inputs.place(x=70,y=60,anchor='nw')


text_root = tk.Label(window,text='输入图片路径',font=14)
text_root.place(x=100,y=110,anchor='nw')

e = tk.StringVar()
text_img =tk.Entry(window,textvariable =0,font=16)

def choose_file():
    selectFileName = tkfiledialog.askopenfile(title='选择文件')
    e.set(selectFileName)

submit_button = tk.Button(window,text='选择照片',commond=choose_file)