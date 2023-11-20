
from tkinter import *
import math

##ฟังก์ชันคำนวณค่าที่ต้องจ่าย
def calculate () :
    try :
        r = (float(EntryNumber3.get()) / 12) / 100
        k = float(EntryNumber1.get()) - float(EntryNumber2.get())
        m = (1 + r) ** (float(EntryNumber4.get())) - 1
        result = r * k / ((1 + r) ** -(float(EntryNumber4.get())) * m)

        print(result)
        Labelresult.configure(text="ผ่อนเดือนละประมาณ \n" + str(math.ceil(result)) + " บาท ")
    except:
        Labelresult.configure(text="ระบบผิดพลาด")

##ฟังก์ชันล้างข้อความ
def clear_text():
   EntryNumber1.delete(0, END)
   EntryNumber2.delete(0, END)
   EntryNumber3.delete(0, END)
   EntryNumber4.delete(0, END)


##GUI
main = Tk()
main.title("SpentDebtCalculate")
main.minsize(height=400,width = 600)
main.configure(bg="black")


Topic = Label(main, text = "คำนวณการผ่อนค่างวด/เดือน", width=30, fg = "white", bg = "black", font=('Helvetica', 10, 'bold'))
Topic.place(x=170,y=0)

Label1 = Label(main, text = "ราคาสินค้าทั้งหมด", width=20, fg = "white", bg = "black", font=('Helvetica', 10, 'bold'))
Label1.place(x=210,y=30)

Label2 = Label(main, text = "เงินดาวน์", width=20, fg = "white", bg = "black", font=('Helvetica', 10, 'bold'))
Label2.place(x=210,y=80)

Label3 = Label(main, text = "ดอกเบี้ย(ร้อบละปี)", width=20, fg = "white", bg = "black", font=('Helvetica', 10, 'bold'))
Label3.place(x=210,y=130)

Label4 = Label(main, text = "จำนวนงวด", width=20, fg = "white", bg = "black", font=('Helvetica', 10, 'bold'))
Label4.place(x=210,y=170)

Labelresult = Label(main, text = "[ค่าผ่อน/เดือน]", width=20, fg = "yellow", bg = "black", font=('Helvetica', 10, 'bold'))
Labelresult.place(x=210,y=250)

Summit = Button(main,width=10 ,text = "คำนวณ",command = calculate)
Summit.place(x=255,y=215)

clear = Button(main,width=10 ,text = "ล้าง",command = clear_text)
clear.place(x=255,y=305)


EntryNumber1 = Entry() #ที่ใส่ราคาสินค้า
EntryNumber1.place(x=230,y=50)

EntryNumber2 = Entry() #ที่ใส่ราคาดาวน์
EntryNumber2.place(x=230,y=100)

EntryNumber3 = Entry() #ที่ใส่ดอกเบี้่ย/ปี
EntryNumber3.place(x=230,y=150)

EntryNumber4 = Entry()  #ที่ใส่จำนวนของงวด
EntryNumber4.place(x=230,y=190)


main.mainloop()