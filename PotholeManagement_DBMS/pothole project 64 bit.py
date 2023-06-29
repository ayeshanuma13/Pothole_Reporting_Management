import cx_Oracle
con = cx_Oracle.connect('xe/xe@localhost')
cursor = con.cursor()
import tkinter
from tkinter import *
import tkinter.messagebox as MessageBox

login=Tk()

def insert_rep():
    repid=report_id.get();
    citname=name.get();
    citid=citizen_id.get();
    num=phone_number.get();

    if(repid=="" or citname=="" or citid=="" or num==""):
        MessageBox.showinfo("All Fields Are Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("insert into Report values('"+ repid +"','"+ citname +"','"+ citid +"','"+ num +"')")
        cursor.execute("commit")

        MessageBox.showinfo("Details Inserted Successfully")
        con.close()

def delete_rep():
    if(report_id.get()==""):
        MessageBox.showinfo("Report ID is Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("delete from Report where report_id='"+ report_id.get() +"'")
        cursor.execute("delete from Report_details where report_id='"+ report_id.get() +"'")
        cursor.execute("delete from report_officer where report_id='"+ report_id.get() +"'")
        cursor.execute("commit")

        MessageBox.showinfo("Details Deleted Successfully")
        con.close()

def select_rep():
    if(report_id.get()==""):
        MessageBox.showinfo("Report ID is Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("select * from Report where report_id='"+ report_id.get() +"'")
        row = cursor.fetchone()
        print(row)
        cursor.execute("commit")

        con.close()
    
def reporter():
    global report_id
    global name
    global citizen_id
    global phone_number
    rep_window=Toplevel(login)
    rep_window.geometry('500x500')
    rep_window.title("Reporter Details")
    
    id=Label(rep_window,text='Enter Report ID',font=('bold',10))
    id.place(x=20,y=30)

    r_name=Label(rep_window,text='Enter Your Name',font=('bold',10))
    r_name.place(x=20,y=60)

    ctzn_id=Label(rep_window,text='Enter Citizen ID',font=('bold',10))
    ctzn_id.place(x=20,y=90)


    phone=Label(rep_window,text='Enter Phone No.',font=('bold',10))
    phone.place(x=20,y=120);

    report_id=Entry(rep_window)
    report_id.place(x=150,y=30)

    name=Entry(rep_window)
    name.place(x=150,y=60)

    citizen_id=Entry(rep_window)
    citizen_id.place(x=150,y=90)

    phone_number=Entry(rep_window)
    phone_number.place(x=150,y=120)

    insert=Button(rep_window,text="INSERT",font=('bold',10),bg='white',command=insert_rep)
    insert.place(x=20,y=140)


    delete=Button(rep_window,text="DELETE",font=('bold',10),bg='white',command=delete_rep)
    delete.place(x=120,y=140)


    select=Button(rep_window,text="View my Information",font=('bold',10),bg='white',command=select_rep)
    select.place(x=220,y=140)

    rep_window.mainloop()


    
def insert_repdet():
    repid=rep_id.get();
    repdate=rep_date.get();
    pot=pot_count.get();
    accident=acci.get();
    status=stat.get();
    stnum=street_no.get();
    stname=street.get();
    remdate=rmv_date.get();

    if(repid=="" or repdate=="" or pot=="" or accident=="" or status=="" or stnum=="" or stname=="" or remdate==""):
        MessageBox.showinfo("All Fields Are Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("insert into Report_details values('"+ repid +"','"+ repdate +"','"+ pot +"','"+ accident +"','"+ status +"','"+ stnum +"','"+ stname +"','"+ remdate +"')")
        cursor.execute("commit")

        MessageBox.showinfo("Details Inserted Successfully")
        con.close()

def select_repdet():
    con = cx_Oracle.connect('xe/xe@localhost')
    cursor = con.cursor()
    cursor.execute("select * from Report_details")
    rows = cursor.fetchall()
    print(rows)
    cursor.execute("commit")

    con.close()

def selectspcfc_repdet():
    repid=rep_id.get();

    if(repid==""):
        MessageBox.showinfo("Report ID is Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("select * from Report_details where report_id='"+ rep_id.get() +"'")
        row = cursor.fetchone()
        print(row)
        cursor.execute("commit")

        con.close()

def delete_repdet():
    if(rep_id.get()==""):
        MessageBox.showinfo("Report ID is Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("delete from Report where report_id='"+ rep_id.get() +"'")
        cursor.execute("delete from Report_details where report_id='"+ rep_id.get() +"'")
        cursor.execute("delete from report_officer where report_id='"+ rep_id.get() +"'")
        cursor.execute("commit")

        MessageBox.showinfo("Details Deleted Successfully")
        con.close()

def update_repdet():
    repid=rep_id.get();
    repdate=rep_date.get();
    pot=pot_count.get();
    accident=acci.get();
    status=stat.get();
    stnum=street_no.get();
    stname=street.get();
    remdate=rmv_date.get();

    if(repid=="" or repdate=="" or pot=="" or accident=="" or status=="" or stnum=="" or stname=="" or remdate==""):
        MessageBox.showinfo("All Fields Are Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("update Report_details set report_date='"+ repdate +"',pothole_count='"+ pot +"',Accidents='"+ accident +"',status='"+ status +"',street_number='"+ stnum +"',street_name='"+ stname +"',Removed_date='"+ remdate +"' where report_id='"+ repid +"'")
        cursor.execute("commit")

        MessageBox.showinfo("Details Updated Successfully")
        con.close()
    
        
    
def report_det():
    global rep_id
    global rep_date
    global pot_count
    global acci
    global stat
    global street_no
    global street
    global rmv_date
    
    repdet_window=Toplevel(login)
    repdet_window.geometry('500x500')
    repdet_window.title("Report Details")
    
    rid=Label(repdet_window,text='Enter Report ID',font=('bold',10))
    rid.place(x=20,y=30)

    rdate=Label(repdet_window,text='Enter Date of report',font=('bold',10))
    rdate.place(x=20,y=60)

    rcount=Label(repdet_window,text='Enter Number of Potholes',font=('bold',10))
    rcount.place(x=20,y=90)

    racci=Label(repdet_window,text='Enter Number of Accidents',font=('bold',10))
    racci.place(x=20,y=120)

    rstat=Label(repdet_window,text='Status of Pothole (Active/Inactive)',font=('bold',10))
    rstat.place(x=20,y=150)

    rstrtno=Label(repdet_window,text='Enter Street Number',font=('bold',10))
    rstrtno.place(x=20,y=180)

    rstrt=Label(repdet_window,text='Enter Street Name',font=('bold',10))
    rstrt.place(x=20,y=210)

    rrmvdate=Label(repdet_window,text='Enter the date of repair (if repaired)',font=('bold',10))
    rrmvdate.place(x=20,y=240)

    rep_id=Entry(repdet_window)
    rep_id.place(x=300,y=30)

    rep_date=Entry(repdet_window)
    rep_date.place(x=300,y=60)

    pot_count=Entry(repdet_window)
    pot_count.place(x=300,y=90)

    acci=Entry(repdet_window)
    acci.place(x=300,y=120)

    stat=Entry(repdet_window)
    stat.place(x=300,y=150)

    street_no=Entry(repdet_window)
    street_no.place(x=300,y=180)

    street=Entry(repdet_window)
    street.place(x=300,y=210)

    rmv_date=Entry(repdet_window)
    rmv_date.place(x=300,y=240)

    insert=Button(repdet_window,text="INSERT",font=('bold',10),bg='white',command=insert_repdet)
    insert.place(x=100,y=300)

    select=Button(repdet_window,text="View all Reports",font=('bold',10),bg='white',command=select_repdet)
    select.place(x=350,y=300)

    selectspcfc=Button(repdet_window,text="View my Report details",font=('bold',10),bg='white',command=selectspcfc_repdet)
    selectspcfc.place(x=180,y=300)

    delete=Button(repdet_window,text="Delete",font=('bold',10),bg='white',command=delete_repdet)
    delete.place(x=200,y=350)

    update=Button(repdet_window,text="Update",font=('bold',10),bg='white',command=update_repdet)
    update.place(x=300,y=350)

    repdet_window.mainloop()
    

def insert_ofcrdet():
    off_id=ofcr_id.get();
    off_name=ofcr_name.get();
    num=p_num.get();

    if(off_id=="" or off_name=="" or num==""):
        MessageBox.showinfo("All Fields Are Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("insert into Officer values('"+ off_id +"','"+ off_name +"','"+ num +"')")
        cursor.execute("commit")

        MessageBox.showinfo("Details Inserted Successfully")
        con.close()

def delete_ofcrdet():
    off_id=ofcr_id.get();
    if(off_id==""):
        MessageBox.showinfo("Officer ID Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("delete from Officer where officer_ID='"+ off_id +"'")
        cursor.execute("delete from report_officer where officer_ID='"+ off_id +"'")
        cursor.execute("commit")

        MessageBox.showinfo("Details Deleted Successfully")
        con.close()

def select_ofcrdet():
    off_id=ofcr_id.get();
    if(off_id==""):
        MessageBox.showinfo("Officer ID Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("select * from Officer where officer_ID='"+ off_id +"'")
        row = cursor.fetchone()
        print(row)
        cursor.execute("commit")
        con.close()
        
def resp_ofcrdet():
    off_id=ofcr_id.get();
    if(off_id==""):
        MessageBox.showinfo("Officer ID Required");
    else:
        con = cx_Oracle.connect('xe/xe@localhost')
        cursor = con.cursor()
        cursor.execute("select * from report_officer where officer_ID='"+ off_id +"'")
        row = cursor.fetchone()
        print(row)
        cursor.execute("commit")
        con.close()
        
def dut_ofcrdet():
    con = cx_Oracle.connect('xe/xe@localhost')
    cursor = con.cursor()
    cursor.execute("select * from report_officer")
    row = cursor.fetchall()
    print(row)
    cursor.execute("commit")
    con.close()
           

def officer():
    global ofcr_id
    global ofcr_name
    global p_num

    ofcrdet_window=Toplevel(login)
    ofcrdet_window.geometry('500x500')
    ofcrdet_window.title("Officer Details")

    ofid=Label(ofcrdet_window,text='Enter Officer ID',font=('bold',10))
    ofid.place(x=20,y=30)

    o_name=Label(ofcrdet_window,text='Enter Your Name',font=('bold',10))
    o_name.place(x=20,y=60)

    o_phone=Label(ofcrdet_window,text='Enter Phone No.',font=('bold',10))
    o_phone.place(x=20,y=90)

    ofcr_id=Entry(ofcrdet_window)
    ofcr_id.place(x=300,y=30)

    ofcr_name=Entry(ofcrdet_window)
    ofcr_name.place(x=300,y=60)

    p_num=Entry(ofcrdet_window)
    p_num.place(x=300,y=90)

    insert=Button(ofcrdet_window,text="INSERT",font=('bold',10),bg='white',command=insert_ofcrdet)
    insert.place(x=150,y=200)

    delete=Button(ofcrdet_window,text="DELETE",font=('bold',10),bg='white',command=delete_ofcrdet)
    delete.place(x=250,y=200)

    select=Button(ofcrdet_window,text="VIEW MY DETAILS",font=('bold',10),bg='white',command=select_ofcrdet)
    select.place(x=100,y=300)

    view=Button(ofcrdet_window,text="VIEW MY RESPONSIBILITY",font=('bold',10),bg='white',command=resp_ofcrdet)
    view.place(x=270,y=300)

    view2=Button(ofcrdet_window,text="VIEW ALL DUTIES",font=('bold',10),bg='white',command=dut_ofcrdet)
    view2.place(x=180,y=400)
    

    ofcrdet_window.mainloop()
    

    
def cit_setting():
    ctzn_window=Toplevel(login)
    ctzn_window.geometry("500x500")
    ctzn_window.title("Citizen Settings")
    lbl=Label(ctzn_window,text="Select your course of action. \n We appreciate your service",
              font=('bold',20))
    lbl.place(x=60,y=10)
    
    btn=Button(ctzn_window,text='My Details',command=reporter)
    btn.pack(padx=80,pady=100)

    btn=Button(ctzn_window,text='Report Details',command=report_det)
    btn.pack(padx=60,pady=30)

def off_setting():
    ofcr_window=Toplevel(login)
    ofcr_window.geometry("500x500")
    ofcr_window.title("Officer Settings")
    lbl=Label(ofcr_window,text="Select your course of action",font=('bold',20))
    lbl.place(x=60,y=10)

    btn=Button(ofcr_window,text='My Details',command=officer)
    btn.pack(padx=80,pady=100)

    btn=Button(ofcr_window,text='Report Details',command=report_det)
    btn.pack(padx=60,pady=30)


btn=Button(login,text='Citizen',command=cit_setting)
btn.pack(padx=80,pady=100)

btn= Button(login,text='Officer',command=off_setting)
btn.pack(padx=60,pady=30)

select=Label(login,text="Select User Category",font=('bold',20))
select.place(x=100,y=20)

login.geometry("500x500")
login.title("Login")



