#โปรแกรมคำนวณค่าไฟฟ้า 
from operator import not_
import sqlite3
from struct import calcsize 
import datetime
from tkinter import *
from email.mime import image

t = datetime.datetime.now()
n = []
h = []
w = []
cal = 0
total = 0
aa_aa = {}
id_1=[]
id_2=0
conn = sqlite3.connect("Projjj.db")
cursor= conn.execute('SELECT * FROM login_1')
for i in cursor:
   id_1.append(int(i[0]))

x_w=int(input("1.สมัคร หรือ 2.เข้าสู่ระบบ :"))
if x_w== 1:
   for i in range(100):
      Fname = str(input("Plese Enter your First name : "))
      if Fname.isalpha() == True:
         break
      else: 
         print ("XXXโปรดป้อนตัวอักษรภาษาอังกฤษเท่านั้นXXX")
      
   for i in range(100):   
      Lname = str(input("Plese Enter your Last name : "))
      if Lname.isalpha() == True:
         break
      else: 
         print ("XXXโปรดป้อนตัวอักษรภาษาอังกฤษเท่านั้นXXX")

   for i in range(100):
      contact = str(input("Plese Enter Phone number : "))
      if contact.isnumeric() == True and len(contact) == 10:
         break
      else:
         print ("XXXโปรดป้อนตัวเลข 10 หลักเท่านั้นXXX")
   
   for i in range(100):
      a_3=input("รหัส : ")
      if a_3.isnumeric() == True and len(a_3) == 6:
         break
      else:
         print ("XXXโปรดป้อนตัวเลข 6 ตัวเท่านั้นXXX")
   c = conn.cursor()
   id_Customer = max(id_1)+1
   if len(str(id_Customer))==1:
      id_Customer = "0"+str(id_Customer)
   c.execute(f"""INSERT INTO login_1 (id,name,phone,password) VALUES ("{id_Customer}","{Fname+" "+Lname}","{contact}","{a_3}")""")
   conn.commit() 
   conn.close()   

elif x_w== 2:
   for i in range(100):
      a_1=input("ชื่อ-สกุล : ")
      a_3=input("รหัส : ")
      cursor= conn.execute(f""" SELECT * FROM login_1 WHERE name=="{a_1}" and password =="{a_3}" """)
      for i in cursor:
         id_2=1
         id_Customer = i[0]
      if id_2==1:
         break
      else:
         print ("XXXชื่อหรือรหัสผ่านไม่ถูกต้องXXX")
else:
   exit()

conn = sqlite3.connect("Projjj.db")
c = conn.cursor()
jj_jj = c.execute('SELECT * FROM name_appliance') 
for a_1 in jj_jj:
   aa_aa [ a_1[0] ] = a_1[1]
################################################################################################
def a(unit):
   global x,service_charge,w_w

   if(unit<=150):
         service_charge = 8.19
         for i in range(len(unit_t)):
            if(unit<=unit_t[i]): 
               x = service_charge+w_w+((unit-ee_ee[i])*rr_rr[i])
               break
            else:
               w_w+=tt_tt[i]
   else:
      service_charge = 38.22
      if(unit<=400):
         x = service_charge + (150*3.2484) + (unit-150)*4.2218
      elif(unit>=400):
         x = service_charge + (150*3.2484) + (250*4.2218) + (unit-400)*4.4217
##################################################################################################

appliance = int(input("Plese Enter number of appliance : "))

for i in range(appliance):
     
   name = str(input("Plese Enter  name of appliance  : "))
   if name in aa_aa:
      p_p=input("เรามี "+name+" ที่มีค่า watt เท่ากับ "+str(aa_aa[name])+" watt ในระบบ ต้องการใช้ค่านี้หรือไม่ y/n : " )
      if p_p =="y" :
         print("watt = ",aa_aa[name])
         watt=aa_aa[name]
      else:
         watt = int(input("Plese Enter power  : "))
   else:
      watt = int(input("Plese Enter power  : "))
   if  name in aa_aa:
      pass
   else:
      l_l=input("ไม่มี"+name+"ในระบบ ต้องการเพิ่มเข้าในระบบหรือไม่ y/n : ")
      if l_l =="y" :
         conn = sqlite3.connect("Projjj.db")
         c = conn.cursor()
         data = (name,watt)
         c.execute('INSERT INTO name_appliance (name,watt) VALUES (?,?)',data)
         conn.commit() 
         c.close()   
         print("เราได้ทำการเพิ่มเข้าไปในระบบให้แล้ว")

   hour = int(input("Plese Enter  time  : "))
   conn = sqlite3.connect("Projjj.db")
   cal = (watt/1000)*hour
   c = conn.cursor()
   data = (t.strftime("%d/%m/%Y"),id_Customer,name,hour,watt,cal)
   c.execute('INSERT INTO charge_electricity (date,id,name_of_appliance,hour,power,cal) VALUES (?,?,?,?,?,?)',data)
   conn.commit() 
   c.close()    
   
   print("หน่วยไฟฟ้าที่ใช้ %.4f" % cal)
   n.append(name)
   h.append(hour)
   w.append(watt)
   total+=cal
print("หน่วยไฟฟ้าที่ใช้ทั้งหมดต่อวัน %.4f" % total)
total_unit = total*30
print("หน่วยไฟฟ้าที่ใช้ทั้งหมดต่อเดือน %.4f" % total_unit)

unit = total_unit
service_charge = 0
unit_t=[15,25,35,100,150]
ee_ee=[0,15,25,65,100]
tt_tt=[0,35.2320,29.882,32.405,235.5405]
rr_rr=[2.3488,2.9882,3.2405,3.6237,3.7171]
w_w=0
x=0
a(unit)

Ft = unit*(0.0139) #อัตราค่าไฟฟ้าลอยตัว หรือ floattime เปลี่ยนแปลงทุกๆ 4 เดือน
vat = (x + Ft)*0.07
bill = x + Ft + vat

price = ( "%.4f" % x, "%.4f" % service_charge,"%.4f" % Ft, "%.4f" % vat ,"%.4f" % bill )
list = (["electricity bill","service charge","Ft\t","vat7%","sum\t"])
for i in range(len(list)):
    print(list[i], "=" ,price[i])


root = Tk()
canvas = Canvas(root, width=393, height=502)
canvas.pack()
Photo = PhotoImage(file='D:\\pyphon\\pro.png')
canvas.create_image(195,255, image = Photo , anchor=CENTER )

Label(root,text = f"รหัสประจำตัวผู้ใช้งาน     ",justify = "left", font=('TH SarabunPSK', 13, 'bold'),bg = "#CC66FF",fg="white").place(x=30,y=100,width=250,height=25)
Label(root,text = id_Customer,justify ="left",bg = "#CC66FF", font=('TH SarabunPSK', 13, 'bold'),fg="white").place(x=200,y=100,width=170,height=25)

Label(root,text = f"ค่าพลังงานไฟฟ้า             ",justify = "left", font=('TH SarabunPSK', 13, 'bold'),bg = "#CC66FF",fg="white").place(x=30,y=140,width=250,height=30)
Label(root,text = f"ค่าบริการรายเดือน            ",justify = "left", font=('TH SarabunPSK', 13, 'bold'),bg = "#CC66FF",fg="white").place(x=30,y=160,width=250,height=30)
Label(root,text = f"ค่าFt 0.0139บาท/หน่วย    ",justify = "left", font=('TH SarabunPSK', 13, 'bold'),bg = "#CC66FF",fg="white").place(x=30,y=180,width=235,height=30)
Label(root,text = f"ค่าภาษีมูลค่าเพิ่ม 7 %          ",justify = "left", font=('TH SarabunPSK', 13, 'bold'),bg = "#CC66FF",fg="white").place(x=30,y=200,width=250,height=30)
Label(root,text = f"รวมค่าไฟฟ้าเดือนปัจจุบัน       ",justify = "left", font=('TH SarabunPSK', 13, 'bold'),bg = "#CC66FF",fg="white").place(x=30,y=220,width=250,height=25)

Label(root,text = "%.4f" % x, justify = "left",bg = "#CC66FF", font=('TH SarabunPSK', 13, 'bold'),fg="white").place(x=200,y=140,width=170,height=25)
Label(root,text = "%.4f" % service_charge, justify = "left",bg = "#CC66FF", font=('TH SarabunPSK', 13, 'bold'),fg="white").place(x=200,y=160,width=170,height=25)
Label(root,text = "%.4f" % Ft, justify = "left",bg = "#CC66FF", font=('TH SarabunPSK', 13, 'bold'),fg="white").place(x=200,y=180,width=170,height=25)
Label(root,text = "%.4f" % vat, justify = "left",bg = "#CC66FF", font=('TH SarabunPSK', 13, 'bold'),fg="white").place(x=200,y=200,width=170,height=25)
Label(root,text = "%.4f" % bill, justify = "left",bg = "#CC66FF", font=('TH SarabunPSK', 13, 'bold'),fg="white").place(x=200,y=220,width=170,height=25)

root.mainloop()

conn = sqlite3.connect("Projjj.db")
c = conn.cursor()
S = (t.strftime("%d/%m/%Y"),id_Customer,"%.4f" % x, "%.4f" % service_charge,"%.4f" % Ft, "%.4f" % vat ,"%.4f" % bill)
c.execute('INSERT INTO electricity_bill (date,id,x,service_charge,Ft,vat,bill) VALUES (?,?,?,?,?,?,?)',S)
conn.commit() 
conn.close()   
   
root.mainloop()

