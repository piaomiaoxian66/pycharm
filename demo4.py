import qrcode #导入模块
date = input(">>>请输入一段内容：") #输入内容
img = qrcode.make(date) #生成二维码
img.save('code.jpg') #保存二维码
img.show() #显示二维码
