from imports import *
import index
##############################################################

def adminLogin():
    admnL=Tk()

    admnL.title('Student Login | CMS')
    #addWin.tk.call('wm', 'iconphoto', admnL._w, PhotoImage(file='ires/ns.ico'))
    admnL.resizable(0, 0)

    #L1
    L1 = Label(admnL,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.pack()

    #L2
    L2 = Label(admnL,text="Admin Login",font = ( "bold" , 15 , ), fg="green")
    L2.pack()
    #L3 empty
    L3 = Label(admnL,text="")
    L3.pack()

    def doSomething():
        admnL.destroy()
        index.main_scr()
        print("Went Home")
    
    def loginNow():
        username=E1.get()
        password=E2.get()
        org_uname="admin"
        org_pwd="root"
        if (username!='' and password!=''):
            if username == org_uname and password==org_pwd:
                #print("OK")
                admnL.destroy()
                #messagebox.showinfo("Logged In","You are now logged in")
                import adminHome
                adminHome.afterAdminLogin(username)
            else:
                L9.config(text="Wrong Username/ Password Combination")
                #print("NOT OK")
        else:
            L9.config(text="Please enter valid values")

    L4=Label(admnL, text="Username")
    L4.pack()
    E1=Entry(admnL, bd=5)
    E1.pack()
    L5=Label(admnL, text="Password")
    L5.pack()
    E2=Entry(admnL, bd=5)
    E2.pack()

    #L8 empty
    L9 = Label(admnL,text="")
    L9.pack()

    B10 = Button(admnL,text="Login", command=loginNow, fg="white", bg="green")
    B10.pack()

    #L8 empty
    L8 = Label(admnL,text="")
    L8.pack()

    #L9 empty
    L9 = Label(admnL,text="")
    L9.pack()

    B20 = Button(admnL,text="Go Home", command=doSomething, fg="white", bg="green")
    B20.pack(side="right",padx="10",pady="10")
    
    admnL.mainloop()
#adminLogin()

##############################################################
