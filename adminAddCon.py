from imports import *
import adminHome
def adminAddCon():
    stdSup=Tk()

    stdSup.title('Add Consignment | CMS')
    #stdSup.tk.call('wm', 'iconphoto', stdSup._w, PhotoImage(file='ires/ns.png'))
    stdSup.resizable(0, 0)

    L1 = Label(stdSup,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.grid(row=0,column=0, rowspan=2, columnspan=12)

    #L2
    L2 = Label(stdSup,text="Add consignment/ shipment here",font = ( "bold" , 15 , ), fg="green")
    L2.grid(row=3,column=0, rowspan=2, columnspan=12)
    #L3 empty
    L3 = Label(stdSup,text="")
    L3.grid(row=5,column=0, rowspan=1, columnspan=12)
    def doSomething():
        stdSup.destroy()
        adminHome.afterAdminLogin("admin")
        #print("Went Home")
        
    def addConsNow():
        item_name=E1.get()
        item_weight=E2.get()
        item_charge=E3.get()
        item_destination=E4.get()
        item_student_reg_num=E5.get()
        item_expected_delivery_num_days=E6.get()

        #print(type(item_name),type(item_weight),item_charge,item_destination,item_student_reg_num,item_expected_delivery_num_days)
        if (item_name!='' and item_weight!='' and item_charge!='' and item_destination!='' and item_student_reg_num!='' and item_expected_delivery_num_days!=''):
            if ((len(item_name)>4) and (len(item_destination)>4) and item_student_reg_num.isdigit() and item_charge.isdigit() and item_weight.isdigit()):
                #print("OK-valid")
                L9.config(text="Data Validated")
                try:
                    insert_db_c_items(item_name, item_weight, item_charge, item_destination, item_student_reg_num,item_expected_delivery_num_days)
                    L10.config(text="Consignment Added Successfully...")
                    #messagebox.showinfo("Account Created", "Please Login on the next screen")
                    #stdSup.after(3000, stdSup.destroy())
                    #stdSup.destroy()
                    #stdLogin.studentLogin()
                except:
                    L10.config(text="Some error occured")
            else:
                L9.config(text="Please enter Valid Details")
                #print("NOT OK-invalid datas")
        else:
            L9.config(text="Please enter all fields")

    L4 = Label(stdSup, text="Shipment Item Name")
    L4.grid(row=6, column=2, padx="10", pady="10")
    E1 = Entry(stdSup)
    E1.grid(row=6, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L5 = Label(stdSup, text="Shipment Item Weight (grams)")
    L5.grid(row=7, column=2, padx="10", pady="10")
    E2 = Entry(stdSup)
    E2.grid(row=7, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L6 = Label(stdSup, text="Shipment Item Charge (Rs.)")
    L6.grid(row=8, column=2, padx="10", pady="10")
    E3 = Entry(stdSup)
    E3.grid(row=8, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L7 = Label(stdSup, text="Destination")
    L7.grid(row=9, column=2, padx="10", pady="10")
    E4 = Entry(stdSup)
    E4.grid(row=9, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L8 = Label(stdSup, text="Student Reg. Num")
    L8.grid(row=10, column=2, padx="10", pady="10")
    E5 = Entry(stdSup)
    E5.grid(row=10, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L11 = Label(stdSup, text="Expected delivery days")
    L11.grid(row=11, column=2, padx="10", pady="10")
    E6 = Entry(stdSup)
    E6.grid(row=11, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    B1 = Button(stdSup, text="Add Consignment", command=addConsNow, fg="white", bg="green")
    B1.grid(row=12, column=3, padx="10", pady="10", ipadx="2",ipady="2")

    L9 = Label(stdSup)
    L9.grid(row=13, column=0, rowspan=2, columnspan=12, pady="20")

    L10 = Label(stdSup)
    L10.grid(row=14, column=0, rowspan=2, columnspan=12, pady="20")

    B20 = Button(stdSup,text="Go Back", command=doSomething, fg="white", bg="green")
    B20.grid(row=15, column=12,padx="10",pady="10")
    
    stdSup.mainloop()
    

#studentSignup() #call
#adminAddCon()
##############################################################
