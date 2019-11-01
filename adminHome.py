from imports import *

def afterAdminLogin(uname):
    afLogin=Tk()

    afLogin.title('Courier Tracking | CMS')
    #afLogin.tk.call('wm', 'iconphoto', afLogin._w, PhotoImage(file='ires/ns.ico'))
    afLogin.resizable(0, 0)

    def callAddCon():
        afLogin.destroy()
        import adminAddCon
        adminAddCon.adminAddCon()
    def callViewCon_Tree():
        afLogin.destroy()
        import adminViewCon_Tree
        adminViewCon_Tree.viewCon("admin")
    def callViewCon():
        afLogin.destroy()
        import adminViewCon
        adminViewCon.viewCon("admin")
    def callUpdateCon(item_id):
        afLogin.destroy()
        import updateCon
        updateCon.updateCon(item_id)
    def doSomething():
        afLogin.destroy()
        import adminLogin
        adminLogin.adminLogin()
        #print("Admin Logged Out")
    #L1
    L1 = Label(afLogin,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.grid(row=0,column=0, rowspan=2, columnspan=12)

    #L2
    L2 = Label(afLogin,text="Home - Manage Consignment",font = ( "bold" , 15 , ), fg="green")
    L2.grid(row=3,column=0, rowspan=2, columnspan=12)
    #L3 empty
    L3 = Label(afLogin,text="")
    L3.grid(row=5,column=0, rowspan=1, columnspan=12)

    l_name = uname
    new_welcome_txt = "Welcome, "+l_name
    L5 = Label(afLogin, text=new_welcome_txt, font = ( "bold" , 14 , ), fg="blue", pady="25")
    L5.grid(row=6,column=0, columnspan=12)
    
    
    #L8 empty
    L8 = Label(afLogin,text="")
    L8.grid(row=8,column=2, padx="20")


    B1 = Button(afLogin,text="Add Consignment", command=callAddCon, fg="white", bg="green")
    B1.grid(row=9, column=1,padx=20)

    B2 = Button(afLogin,text="View/ Update", command=callViewCon, fg="white", bg="green")
    B2.grid(row=9, column=3,padx=20)

    B3 = Button(afLogin,text="View all Consignments", command=callViewCon_Tree, fg="white", bg="green")
    B3.grid(row=9, column=5,padx=20)
    
    #B3 = Button(afLogin,text="Update Location", command=callUpdateCon, fg="white", bg="green")
    #B3.grid(row=9, column=5,padx=20)
    
    #L9 empty
    L9 = Label(afLogin,text="")
    L9.grid(row=10,column=2, padx="20")

    B20 = Button(afLogin,text="Log Out", command=doSomething, fg="white", bg="green")
    B20.grid(row=11, column=12,padx="10",pady="10")
    
    afLogin.mainloop()

#afterAdminLogin("admin")
