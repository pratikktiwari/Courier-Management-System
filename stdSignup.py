from imports import *
import index
def studentSignup():
    stdSup=Tk()

    stdSup.title('Student Signup | CMS')
    #stdSup.tk.call('wm', 'iconphoto', stdSup._w, PhotoImage(file='ires/ns.png'))
    stdSup.resizable(0, 0)

    L1 = Label(stdSup,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.grid(row=0,column=0, rowspan=2, columnspan=12)

    #L2
    L2 = Label(stdSup,text="Student Signup - Account Creation",font = ( "bold" , 15 , ), fg="green")
    L2.grid(row=3,column=0, rowspan=2, columnspan=12)
    #L3 empty
    L3 = Label(stdSup,text="")
    L3.grid(row=5,column=0, rowspan=1, columnspan=12)
    def doSomething():
        stdSup.destroy()
        index.main_scr()
        #print("Went Home")
        
    def signUpNow():
        name=E1.get()
        reg_num=E2.get()
        mobile=E3.get()
        uname=E4.get()
        uname=uname.lower()
        pwd=E5.get()
        #check_uname == True) and 
        if (name!='' and reg_num!='' and mobile!='' and uname!='' and pwd!=''):
	    #insert_db(item_name, item_quantity, item_price, item_dec)
            check_uname = check_if_user_exists(uname)
            #print("Reg",reg_num.isdigit())
            if ((len(uname)>4) and (len(pwd)>4) and reg_num.isdigit() and mobile.isdigit() and len(mobile)==10):
                #print("OK")
                if check_uname==False:
                    L9.config(text="Data Validated")
                    try:
                        insert_db(reg_num, name, uname,pwd, mobile)
                        L10.config(text="Account Created...Please Login on the next screen...")
                        #time.sleep(3)
                        #messagebox.showinfo("Please Login on the next screen")
                        messagebox.showinfo("Account Created", "Please Login on the next screen")
                        stdSup.after(1000, stdSup.destroy())
                        #stdSup.destroy()
                        import stdLogin
                        stdLogin.studentLogin()
                    except:
                        L10.config(text="Some error error")
                else:
                    L9.config(text="Username already exists")
            else:
                L9.config(text="Please enter Valid Details")
                #print("NOT OK")
        else:
            L9.config(text="Please enter valid values")

    L4 = Label(stdSup, text="Full Name")
    L4.grid(row=6, column=2, padx="10", pady="10")
    E1 = Entry(stdSup)
    E1.grid(row=6, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L5 = Label(stdSup, text="Reg. Num")
    L5.grid(row=7, column=2, padx="10", pady="10")
    E2 = Entry(stdSup)
    E2.grid(row=7, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L6 = Label(stdSup, text="Mobile Num")
    L6.grid(row=8, column=2, padx="10", pady="10")
    E3 = Entry(stdSup)
    E3.grid(row=8, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L7 = Label(stdSup, text="Username")
    L7.grid(row=9, column=2, padx="10", pady="10")
    E4 = Entry(stdSup)
    E4.grid(row=9, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L8 = Label(stdSup, text="Password")
    L8.grid(row=10, column=2, padx="10", pady="10")
    E5 = Entry(stdSup)
    E5.grid(row=10, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    B1 = Button(stdSup, text="SignUp", command=signUpNow, fg="white", bg="green")
    B1.grid(row=11, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L9 = Label(stdSup)
    L9.grid(row=12, column=0, rowspan=2, columnspan=12, pady="20")

    L10 = Label(stdSup)
    L10.grid(row=13, column=0, rowspan=2, columnspan=12, pady="20")

    B20 = Button(stdSup,text="Go Home", command=doSomething, fg="white", bg="green")
    B20.grid(row=14, column=12,padx="10",pady="10")
    
    stdSup.mainloop()
    

#studentSignup() #call

##############################################################
