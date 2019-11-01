from imports import *
from tkinter import ttk
def viewCon(uname):
    viewCo=Tk()

    viewCo.title('Courier Tracking | CMS')
    #viewCo.tk.call('wm', 'iconphoto', afLogin._w, PhotoImage(file='ires/ns.ico'))
    viewCo.resizable(0, 0)

    def doSomething():
        viewCo.destroy()
        import adminHome
        adminHome.afterAdminLogin("admin")
        #print("Admin Logged Out")
    #L1
    L1 = Label(viewCo,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.pack()

    #L2
    L2 = Label(viewCo,text="Home - Manage Consignment",font = ( "bold" , 15 , ), fg="green")
    L2.pack()
    #L3 empty
    L3 = Label(viewCo,text="")
    L3.pack()

    l_name = uname
    new_welcome_txt = "Welcome "+l_name+", Showing all Consignments"
    L5 = Label(viewCo, text=new_welcome_txt, font = ( "bold" , 14 , ), fg="blue", pady="25")
    L5.pack()
    
    

    #top-labels
    def view_data():
        rows = select_all_courier()
        print(rows)
        for row in rows:
            #print(row)
            tree.insert("", END, values=row)
    #view_data()

    tree=ttk.Treeview(viewCo, column=("item_id", "item_name", "item_weight","item_charge","item_destination", "item_student_reg_num","item_timestamp","item_expected_delivery_num_days"), show='headings')
    tree.heading("#1", text="Cons Num.")
    tree.heading("#2", text="Item Name")
    tree.heading("#3", text="Weight")
    tree.heading("#4", text="Charge")
    tree.heading("#5", text="Destination")
    tree.heading("#6", text="Reg. Num.")
    tree.heading("#7", text="Timestamp")
    tree.heading("#8", text="exp del. days")

    tree.tag_configure('odd', background='red')
    tree.tag_configure('even', background='green')

    ttk.Style().configure("Treeview", background="#383838", 
    foreground="white", fieldbackground="red",margin=1,border=1)

    ttk.Style().configure("Treeview.Heading",background="blue", foreground="blue", relief="flat")
    ttk.Style().configure("Treeview.Heading",relief=[('active','groove'),('pressed','sunken')])

    tree.pack()
    view_data()


    B20 = Button(viewCo,text="Go Back", command=doSomething, fg="white", bg="green")
    B20.pack()
    
    viewCo.mainloop()

#viewCon("admin")
