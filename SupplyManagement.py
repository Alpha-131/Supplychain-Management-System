from tkinter import *
import sqlite3
from tkinter import messagebox

#id- DBMSproject
#pass - DBMSproject

# cursor.execute("insert into customer values('1','Varun','12345');")
# cursor.execute("select * from customer")
# print(cursor.fetchall())


top=Tk()
top.geometry("328x300")
top.title("PySQL WORKBENCH")
top.configure(bg='#222831')

def pop_message():
    if en.get()=="123" and en1.get()=="123":
        page1()
        top.destroy()
        #root.deiconify()
    else:
         messagebox.showwarning(title="Invalid Deatils",message="Invalid id or password")
    

label=Label(top,text="Welcome to PySQL WORKBENCH",bg='#00ADB5',font=('Arial',15,'bold'))
label.grid(row=0,column=3,pady=30)



l1=Label(top,text="Login Id:-",bg='#00ADB5',font=('Arial',8,'bold'))
l1.place(x=15,y=107)
en=Entry(top)
en.grid(row=2,column=3,pady=20)
l2=Label(top,text="Password:-",bg='#00ADB5',font=('Arial',8,'bold'))
l2.place(x=15,y=167)
en1=Entry(top,show='*')
en1.grid(row=3,column=3,pady=20)
lo_button=Button(top,text="Login",command=pop_message,height=1,width=10,bg='#00ADB5',border=5)
lo_button.grid(row=5,column=3,pady=15)
    


sqliteConnection = sqlite3.connect('SupplyChain.db')
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")

cursor.execute("create table if not exists supplier(sid varchar(20) primary key,sname varchar(40),sno varchar(20));")
cursor.execute("create table if not exists customer(cid varchar(20) primary key,cname varchar(40),cno varchar(20));")
cursor.execute("create table if not exists product(pid varchar(20) primary key,pname varchar(40),cost varchar(20));")
cursor.execute("create table if not exists supplies(cid varchar(20),sid varchar(20),discount varchar(20),delivery_date date,constraint c1 foreign key(cid) references customer(cid),constraint c2 foreign key(sid) references supplier(sid));")
cursor.execute("create table if not exists buys(sid varchar(20),pid varchar(20),discount varchar(20),buying_date date,constraint c3 foreign key(pid) references product(pid),constraint c4 foreign key(sid) references supplier(sid));")

def page1():
    top.destroy()
    root = Tk()
    root.title('Supply Chain Management System')
    root.geometry("700x500")
    root.configure(bg='#222831')


    def enterdata():
        root.withdraw()
        entwindow = Tk()
        entwindow.title('Supply Chain Management System')
        entwindow.geometry("800x600")
        entwindow.configure(bg='#222831')


        def supenter():
            entwindow.withdraw()
            supwindow = Tk()
            supwindow.geometry("800x600")
            supwindow.title('Supply Chain Management System')
            supwindow.configure(bg='#222831')
            sup_id = Label(supwindow,text="Supplier ID: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            sup_id.place(x=150,y=100)
            sup_name = Label(supwindow,text="Supplier Name: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            sup_name.place(x=150,y=250)
            sup_phone = Label(supwindow,text="Phone No.: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            sup_phone.place(x=150,y=400)

            inputid = Entry(supwindow,width=30)
            inputid.place(x=300,y=100)
            inputname = Entry(supwindow,width=30)
            inputname.place(x=300,y=250)
            inputnum = Entry(supwindow,width=30)
            inputnum.place(x=300,y=400)

            # sno=inputnum.get()
            # sname=inputname.get()
            # sid = inputid.get()


            def supstore():
                string1=f"insert into supplier(sid,sname,sno) values('{inputid.get()}','{inputname.get()}','{inputnum.get()}');"
                cursor.execute(string1)
                sqliteConnection.commit()


            supenterbtn = Button(supwindow,text="Enter",command=supstore,bg='#00ADB5',activebackground='#393E46',border=5,font=('Arial',12,'bold'))
            supenterbtn.place(x=300,y=450)
            supwindow.mainloop()

        def custenter():
            entwindow.withdraw()
            custwindow = Tk()
            custwindow.title('Supply Chain Management System')
            custwindow.geometry("800x600")
            custwindow.configure(bg='#222831')
            cust_id = Label(custwindow,text="Customer ID: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            cust_id.place(x=150,y=100)
            cust_name = Label(custwindow,text="Customer Name: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            cust_name.place(x=150,y=250)
            cust_phone = Label(custwindow,text="Customer No.: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            cust_phone.place(x=150,y=400)

            inputid = Entry(custwindow,width=30)
            inputid.place(x=300,y=100)
            inputname = Entry(custwindow,width=30)
            inputname.place(x=300,y=250)
            inputnum = Entry(custwindow,width=30)
            inputnum.place(x=300,y=400)

            # cno=inputnum.get()
            # cname=inputname.get()
            # cid = inputid.get()
            def custstore():
                string1=f"insert into customer(cid,cname,cno) values('{inputid.get()}','{inputname.get()}','{inputnum.get()}');"
                cursor.execute(string1)
                sqliteConnection.commit()


            custenterbtn = Button(custwindow,text="Enter",command=custstore,bg='#00ADB5',activebackground='#393E46',border=5,font=('Arial',12,'bold'))
            custenterbtn.place(x=350,y=450)
            custwindow.mainloop()

        def prodenter():
            entwindow.withdraw()
            prodwindow = Tk()
            prodwindow.title('Supply Chain Management System')
            prodwindow.geometry("800x600")
            prodwindow.configure(bg='#222831')
            prod_id = Label(prodwindow,text="Product ID: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            prod_id.place(x=150,y=100)
            prod_name = Label(prodwindow,text="Product Name: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            prod_name.place(x=150,y=250)
            prod_cost = Label(prodwindow,text="Cost: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            prod_cost.place(x=150,y=400)

            inputid = Entry(prodwindow,width=30)
            inputid.place(x=300,y=100)
            inputname = Entry(prodwindow,width=30)
            inputname.place(x=300,y=250)
            inputcost = Entry(prodwindow,width=30)
            inputcost.place(x=300,y=400)


            # pname=inputname.get()
            # pid = inputid.get()
            # cost = inputcost.get()
            def prodstore():
                string1=f"insert into product(pid,pname,cost) values('{inputid.get()}','{inputname.get()}','{inputcost.get()}');"
                cursor.execute(string1)
                sqliteConnection.commit()

            prodenterbtn = Button(prodwindow,text="Enter",command=prodstore,bg='#00ADB5',activebackground='#393E46',border=5,font=('Arial',12,'bold'))
            prodenterbtn.place(x=350,y=500)
            prodwindow.mainloop()

        def supplies_enter():
            entwindow.withdraw()
            supplieswindow = Tk()
            supplieswindow.title('Supply Chain Management System')
            supplieswindow.geometry("800x600")
            supplieswindow.configure(bg='#222831')
            supplies_id = Label(supplieswindow,text="Supplier ID: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            supplies_id.place(x=150,y=100)
            supplies_name = Label(supplieswindow,text="Customer ID: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            supplies_name.place(x=150,y=210)
            supplies_phone = Label(supplieswindow,text="Discount: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            supplies_phone.place(x=150,y=320)
            supplies_phone = Label(supplieswindow,text="Delivery Date: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            supplies_phone.place(x=150,y=430)

            inputid = Entry(supplieswindow,width=30)
            inputid.place(x=300,y=100)
            inputid2 = Entry(supplieswindow,width=30)
            inputid2.place(x=300,y=210)
            inputdisc = Entry(supplieswindow,width=30)
            inputdisc.place(x=300,y=320)
            inputdate = Entry(supplieswindow,width=30)
            inputdate.place(x=300,y=430)

            # sid=inputid.get()
            # cid=inputid2.get()
            # discount = inputdisc.get()
            # date = inputdate.get()

            def suppliesstore():
                string1=f"insert into supplies(cid,sid,discount,delivery_date) values('{inputid.get()}','{inputid2.get()}','{inputdisc.get()}','{inputdate.get()}');"
                cursor.execute(string1)
                sqliteConnection.commit()


            custenterbtn = Button(supplieswindow,text="Enter",command=suppliesstore,bg='#00ADB5',activebackground='#393E46',border=5,font=('Arial',12,'bold'))
            custenterbtn.place(x=350,y=505)
            supplieswindow.mainloop()

        def Buys_enter():
            entwindow.withdraw()
            Buyswindow = Tk()
            Buyswindow.title('Supply Chain Management System')
            Buyswindow.geometry("800x600")
            Buyswindow.configure(bg='#222831')
            Buys_id = Label(Buyswindow,text="Supplier ID: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            Buys_id.place(x=150,y=80)
            Buys_name = Label(Buyswindow,text="Product ID: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            Buys_name.place(x=150,y=200)
            Buys_phone = Label(Buyswindow,text="Discount: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            Buys_phone.place(x=150,y=320)
            Buys_phone = Label(Buyswindow,text="Buying Date: ",bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
            Buys_phone.place(x=150,y=440)

            inputid = Entry(Buyswindow,width=30)
            inputid.place(x=300,y=80)
            inputid2 = Entry(Buyswindow,width=30)
            inputid2.place(x=300,y=200)
            inputdisc = Entry(Buyswindow,width=30)
            inputdisc.place(x=300,y=320)
            inputdate = Entry(Buyswindow,width=30)
            inputdate.place(x=300,y=440)

            # sid=inputid.get()
            # pid=inputid2.get()
            # discount = inputdisc.get()
            # date = inputdate.get()

            def buyingstore():
                string1=f"insert into buys(sid,pid,discount,buying_date) values('{inputid.get()}','{inputid2.get()}','{inputdisc.get()}','{inputdate.get()}');"
                cursor.execute(string1)
                sqliteConnection.commit()


            custenterbtn = Button(Buyswindow,text="Enter",command=buyingstore,bg='#00ADB5',activebackground='#393E46',border=5,font=('Arial',12,'bold'))
            custenterbtn.place(x=350,y=470)
            Buyswindow.mainloop()


        btn1 = Button(entwindow,text="Suppliers",height=2,width=10,command=supenter,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn1.pack(pady=40)
        btn2 = Button(entwindow,text="Customer",height=2,width=10,command=custenter,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn2.pack(pady=40)
        btn3 = Button(entwindow,text="Product",height=2,width=10,command=prodenter,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn3.pack(pady=40)
        btn4 = Button(entwindow,text="Supplies-To",height=2,width=10,command=supplies_enter,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn4.pack(pady=40)
        btn5 = Button(entwindow,text="Buys",height=2,width=10,command=Buys_enter,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn5.pack(pady=40)

        root.iconify()
        entwindow.mainloop()

    def displaydata():
        root.withdraw()
        dispwindow = Tk()
        dispwindow.title('Supply Chain Management System')
        dispwindow.geometry("800x600")
        dispwindow.configure(bg='#222831')

        def supdisp():
            dispwindow.withdraw()
            dispw = Tk()
            dispw.geometry("800x600")
            dispw.title('Supply Chain Management System')
            dispw.configure(bg='#222831')
            # cursor.execute("insert into supplier values('10','Rachit','23456');")
            # cursor.execute("select * from supplier")
            # print(cursor.fetchall())
            r_set=cursor.execute('''SELECT * from supplier;''')
            i=0 # row value inside the loop 

            for student in r_set: 
                for j in range(len(student)):
                    e = Label(dispw, width=20, fg='blue',text=student[j]) 
                    e.grid(row=i, column=j,padx=1,pady=1) 
                    #e.insert(END, student[j])
                i=i+1
            dispw.mainloop()

        def custdisp():
            dispwindow.withdraw()
            dispw = Tk()
            dispw.title('Supply Chain Management System')
            dispw.geometry("800x600")
            dispw.configure(bg='#222831')
            r_set=cursor.execute('''SELECT * from customer;''')
            i=0 

            for student in r_set: 
                for j in range(len(student)):
                    e = Label(dispw, width=20, fg='blue',text=student[j]) 
                    e.grid(row=i, column=j,padx=1,pady=1) 
                i=i+1
            dispw.mainloop()

        def proddisp():
            dispwindow.withdraw()
            dispw = Tk()
            dispw.title('Supply Chain Management System')
            dispw.geometry("800x600")
            dispw.configure(bg='#222831')
            r_set=cursor.execute('''SELECT * from product;''')
            i=0 

            for student in r_set: 
                for j in range(len(student)):
                    e = Label(dispw, width=20, fg='blue',text=student[j]) 
                    e.grid(row=i, column=j,padx=1,pady=1) 
                i=i+1
            dispw.mainloop()

        def suptodisp():
            dispwindow.withdraw()
            dispw = Tk()
            dispw.title('Supply Chain Management System')
            dispw.geometry("800x600")
            dispw.configure(bg='#222831')
            r_set=cursor.execute('''SELECT * from supplies;''')
            i=0 

            for student in r_set: 
                for j in range(len(student)):
                    e = Label(dispw, width=20, fg='blue',text=student[j]) 
                    e.grid(row=i, column=j,padx=1,pady=1) 
                i=i+1
            dispw.mainloop()

        def buysdisp():
            dispwindow.withdraw()
            dispw = Tk()
            dispw.title('Supply Chain Management System')
            dispw.geometry("800x600")
            dispw.configure(bg='#222831')
            r_set=cursor.execute('''SELECT * from buys;''')
            i=0  

            for student in r_set: 
                for j in range(len(student)):
                    e = Label(dispw, width=20, fg='blue',text=student[j]) 
                    e.grid(row=i, column=j,padx=1,pady=1) 
                i=i+1
            dispw.mainloop()

        btn1 = Button(dispwindow,text="Suppliers",height=2,width=10,command=supdisp,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn1.pack(pady=40)
        btn2 = Button(dispwindow,text="Customer",height=2,width=10,command=custdisp,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn2.pack(pady=40)
        btn3 = Button(dispwindow,text="Product",height=2,width=10,command=proddisp,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn3.pack(pady=40)
        btn4 = Button(dispwindow,text="Supplies-To",height=2,width=10,command=suptodisp,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn4.pack(pady=40)
        btn5 = Button(dispwindow,text="Buys",height=2,width=10,command=buysdisp,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
        btn5.pack(pady=40)

        root.iconify()
        dispwindow.mainloop()

    def query():
        root.withdraw()
        qwindow = Tk()
        qwindow.title('Supply Chain Management System')
        qwindow.geometry('800x600')
        qwindow.configure(bg='#222831')

        def qchng():
            new_win = Tk()
            new_win.geometry('800x600')
            new_win.configure(bg='#222831')
            new_win.title('Supply Chain Management System')
            r_set=cursor.execute(f'{qentr.get()};')
            print(r_set)
            i=0 

            for student in r_set: 
                for j in range(len(student)):
                    e = Label(new_win, width=20, fg='blue',text=student[j]) 
                    e.grid(row=i, column=j,padx=1,pady=1) 
                i=i+1
            new_win.mainloop()

        qlbl=Label(qwindow,text="ENTER YOUR QUERY",bg='#00ADB5',border=20)
        qlbl.pack(pady=30)
        qentr = Entry(qwindow,width=129,font=('Bold',20))
        qentr.pack(pady=30,padx=10)
        entrbutt = Button(qwindow,text="Enter",command=qchng,bg='#00ADB5',activebackground='#393E46',border=10,width=20)
        entrbutt.pack(pady=30)

    entr = Button(root,text="Enter Data",height=2,width=10,command=enterdata,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
    entr.pack(pady=50)
    disp = Button(root,text="Display",height=2,width=10,command=displaydata,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
    disp.pack(pady=50)
    q = Button(root,text="Query-Input",height=2,width=10,command=query,bg='#00ADB5',activebackground='#393E46',border=10,font=('Arial',12,'bold'))
    q.pack(pady=50)
    root.mainloop()

top.mainloop()