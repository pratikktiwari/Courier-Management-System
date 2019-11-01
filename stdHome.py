from imports import *
from tkinter import ttk
def afterStudentLogin(username):
    afLogin=Tk()

    afLogin.title('Courier Tracking | CMS')
    #afLogin.tk.call('wm', 'iconphoto', afLogin._w, PhotoImage(file='ires/ns.ico'))
    afLogin.resizable(0, 0)
    def callLogin():
        try:
            afLogin.destroy()
            import stdLogin
            stdLogin.studentLogin()
        except:
            print("Cannot Logout")

    #user_info_variables
    l_user_id = get_id_from_uname(username)
    #(col_id, std_id) for calling single_row_item
    l_reg_num = select_single_row_item(2,l_user_id)
    l_name = select_single_row_item(1,l_user_id)
    l_mobile = select_single_row_item(3,l_user_id)
    #l_uname = select_single_row_item(4,l_user_id)

    #L1
    L1 = Label(afLogin,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.pack()

    #L2
    L2 = Label(afLogin,text="Track your consignment",font = ( "bold" , 15 , ), fg="green")
    L2.pack()
    #L3 empty
    #L3 = Label(afLogin,text="")
    #L3.pack()

    new_welcome_txt = "Welcome, "+l_name
    L5 = Label(afLogin, text=new_welcome_txt, font = ( "bold" , 14 , ), fg="blue", pady="25")
    L5.pack()
    
    L4=Label(afLogin, text="Registration Number")
    L4.pack()
    
    L6=Label(afLogin, text=l_reg_num)
    L6.pack()

    L11=Label(afLogin, text="Mobile")
    L11.pack()
    
    L12=Label(afLogin, text=l_mobile)
    L12.pack()
    
    #L8 empty
    L8 = Label(afLogin,text="")
    L8.pack()

    

    #tree
    #top-labels
    def view_data():
        #rows = select_all_courier()
        rows=select_all_item_info_user_id(l_reg_num)
        #print(type(rows))
        #print(type((2,3)))
        import sqlite3
        if type(rows)==sqlite3.Cursor:
            for row in rows:
                tree.insert("", END, values=row)
        else:
            L8.config(text="You have no consignments")

    tree=ttk.Treeview(afLogin, column=("item_name", "item_expected_delivery_num_days", "transit_complete","transit_location","transit_timestamp"), show='headings')
    tree.heading("#1", text="item_name")
    tree.heading("#2", text="Num days")
    tree.heading("#3", text="Complete")
    tree.heading("#4", text="Location")
    tree.heading("#5", text="Timestamp")
    
    tree.tag_configure('odd', background='red')
    tree.tag_configure('even', background='green')

    ttk.Style().configure("Treeview", background="#383838", 
    foreground="white", fieldbackground="red",margin=1,border=1)

    ttk.Style().configure("Treeview.Heading",background="blue", foreground="blue", relief="flat")
    ttk.Style().configure("Treeview.Heading",relief=[('active','groove'),('pressed','sunken')])

    tree.pack()
    view_data()    

    B15=Button(text="Logout", fg="white",bg="green",padx="3", command=callLogin)
    B15.pack()

    #L9 empty
    L9 = Label(afLogin,text="")
    L9.pack()
    afLogin.mainloop()
#afterStudentLogin("devendra")
