from imports import *
import index
##############################################################
    
def studentLogin():
    addWin=Tk()
    gen_random_str=rand_str_generator()

    addWin.title('Student Login | CMS')
    #addWin.tk.call('wm', 'iconphoto', addWin._w, PhotoImage(file='ires/ns.ico'))
    addWin.resizable(0, 0)

    #L1
    L1 = Label(addWin,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.pack()

    #L2
    L2 = Label(addWin,text="Student Login",font = ( "bold" , 15 , ), fg="green")
    L2.pack()
    #L3 empty
    L3 = Label(addWin,text="")
    L3.pack()

    def doSomething():
        addWin.destroy()
        index.main_scr()
        #print("Went Home")
    
    def loginNow():
        username=E1.get()
        password=E2.get()
        entered_captcha = E3.get()
        captcha_truthy=check_captcha(gen_random_str,entered_captcha)
        
        if (username!='' and password!=''):
            text_ = check_login(username,password)
            if text_==True and captcha_truthy==True:
                #print("OK")
                addWin.destroy()
                import stdHome
                stdHome.afterStudentLogin(username)
            else:
                L9.config(text="Wrong Username/ Password/Captcha Combination")
                #print("NOT OK")
        else:
            L9.config(text="Please enter valid values")

    L4=Label(addWin, text="Username")
    L4.pack()
    E1=Entry(addWin, bd=5)
    E1.pack()
    L5=Label(addWin, text="Password")
    L5.pack()
    E2=Entry(addWin, bd=5)
    E2.pack()

    
    #text captch
    random_str_txt = "Captcha: "+gen_random_str
    L11 =Label(addWin,text=random_str_txt, bg="blue",fg="white",font = ( "bold" , 14 , ))
    L11.pack(padx="15",pady="15")
    E3=Entry(addWin, bd=5)
    E3.pack()
    #text captcha

    
    #L8 empty
    L9 = Label(addWin,text="")
    L9.pack()

    B10 = Button(addWin,text="Login", command=loginNow, fg="white", bg="green")
    B10.pack()

    #L8 empty
    L8 = Label(addWin,text="")
    L8.pack()

    #L9 empty
    L9 = Label(addWin,text="")
    L9.pack()

    B20 = Button(addWin,text="Go Home", command=doSomething, fg="white", bg="green")
    B20.pack(side="right",padx="10",pady="10")
    
    addWin.mainloop()
#studentLogin()

##############################################################
