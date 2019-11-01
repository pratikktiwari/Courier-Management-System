from imports import *

def main_scr():
    def callStudentLogin():
        try:
            top.destroy()
            import stdLogin
            stdLogin.studentLogin()
        except:
            print("Cannot close main from login")
    def callStudentSignup():
        #print("Signup Called")    
        try:
            top.destroy()
            import stdSignup
            stdSignup.studentSignup()
        except:
            print("Cannot destroy main from signup")
    def callAdminLogin():
        #print("Admin Login Called")    
        try:
            top.destroy()
            import adminLogin
            adminLogin.adminLogin()
        except:
            print("Cannot destroy main from signup")
    top = Tk()
    top.title("Courier Management, LPU")

    #top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file='ires/ns.ico'))
    #top.geometry('700x700')
    photo = PhotoImage(file = 'ires/inventory.PNG')
    photo = photo.subsample(1)
    lbl = Label(top,image = photo)
    lbl.image = photo
    lbl.grid(row=0,column=0, columnspan=12,rowspan=10)
    #L1
    L1 = Label(top,text="Courier Management, LPU",font = ( "bold" , 32 , ), fg="blue")
    L1.grid(row=11,column=0, columnspan=12,rowspan=2)
    
    #L2
    L2 = Label(top,text="Choose from the options below",font = ( "bold" , 15 , ), fg="green")
    L2.grid(row=13,column=0, columnspan=12,rowspan=2)
    #L3 empty
    L3 = Label(top,text="")
    L3.grid(row=15,column=0, columnspan=12,rowspan=2)
    #B1
    B1 = Button(top, text = 'Student Login',command=callStudentLogin, fg="white", bg="green")
    B1.grid(row=17,column=3,padx=3,pady=3,columnspan=2)
    #B3
    B3 = Button(top, text = 'Student Signup',command=callStudentSignup, fg="white", bg="green")
    B3.grid(row=17,column=5,padx=3,pady=3,columnspan=2)
    #B2
    B2 = Button(top, text = 'Admin Login',command=callAdminLogin,  fg="white", bg="green")
    B2.grid(row=17,column=7,padx=3,pady=3,columnspan=2)

    #L5 empty
    L5 = Label(top,text="")
    L5.grid(row=18,column=0, columnspan=12,rowspan=2)
    #top mainloop
    top.resizable(0,0)
    top.mainloop()
