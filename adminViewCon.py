from imports import *

def viewCon(uname):
    viewCo=Tk()

    viewCo.title('Courier Tracking | CMS')
    #viewCo.tk.call('wm', 'iconphoto', afLogin._w, PhotoImage(file='ires/ns.ico'))
    viewCo.resizable(0, 0)
    def refreshScreen():
        try:
            viewCo.destroy()
            import adminViewCon
            adminViewCon.viewCon("adimn")
        except:
            print("Cannot destroy")
    def updateLocation():
        con_num = E16.get()
        con_loc = E17.get()
        insert_db_transit(2,'Jalandhar',0)
        item_exists = check_if_item_exists(con_num)
        #print(item_exists)
        if con_num!='' and con_loc!='' and item_exists==True:
            try:
                insert_db_transit(con_num,con_loc,0)
                L70.config(text="Location Updated")
            except:
                L70.config(text="Cannot update location")
        else:
            L70.config(text="Cannot Update/ No such consignment number")
    def doSomething():
        viewCo.destroy()
        import adminHome
        adminHome.afterAdminLogin("admin")
        #print("Admin Logged Out")
        
    #L1
    L1 = Label(viewCo,text="Courier Management System, LPU",font = ( "bold" , 32 , ), fg="blue",padx="20")
    L1.grid(row=0,column=0, rowspan=2, columnspan=12)

    #L2
    L2 = Label(viewCo,text="Home - Manage Consignment",font = ( "bold" , 15 , ), fg="green")
    L2.grid(row=3,column=0, rowspan=2, columnspan=12)
    #L3 empty
    L3 = Label(viewCo,text="")
    L3.grid(row=5,column=0, rowspan=1, columnspan=12)

    l_name = uname
    new_welcome_txt = "Welcome "+l_name+", Showing top 3 Consignments"
    L5 = Label(viewCo, text=new_welcome_txt, font = ( "bold" , 14 , ), fg="blue", pady="25")
    L5.grid(row=6,column=0, columnspan=12)
    
    



    #viewing data three latest data items from db
    count_rows_db=select_count_rows_courier()
    count_rows=count_rows_db[0]
    #print("Count rows-",count_rows)
    #top-labels
    L21=Label(viewCo,text="id", font=("bold",13,),fg="white",bg="blue")
    L21.grid(row=7,column=0)
    L22=Label(viewCo,text="Item Name", font=("bold",13,),fg="white",bg="blue")
    L22.grid(row=7,column=1)
    L23=Label(viewCo,text="Weight", font=("bold",13,),fg="white",bg="blue")
    L23.grid(row=7,column=2)
    L24=Label(viewCo,text="Charge", font=("bold",13,),fg="white",bg="blue")
    L24.grid(row=7,column=3)
    L25=Label(viewCo,text="Destination", font=("bold",13,),fg="white",bg="blue")
    L25.grid(row=7,column=4)
    L26=Label(viewCo,text="Reg. Num", font=("bold",13,),fg="white",bg="blue")
    L26.grid(row=7,column=5)
    L27=Label(viewCo,text="TimeStamp", font=("bold",13,),fg="white",bg="blue")
    L27.grid(row=7,column=6)
    L28=Label(viewCo,text="Days", font=("bold",13,),fg="white",bg="blue")
    L28.grid(row=7,column=7)
    L29=Label(viewCo,text="Curr. Loc.", font=("bold",13,),fg="white",bg="blue")
    L29.grid(row=7,column=8)
    #check_last_transit_location(2)
    #first-row-data-items
    L31=Label(viewCo,text=select_single_cons(count_rows)[0], font=("bold",10,))
    L31.grid(row=8,column=0)
    L32=Label(viewCo,text=select_single_cons(count_rows)[1], font=("bold",10,))
    L32.grid(row=8,column=1)
    L33=Label(viewCo,text=select_single_cons(count_rows)[2], font=("bold",10,))
    L33.grid(row=8,column=2)
    L34=Label(viewCo,text=select_single_cons(count_rows)[3], font=("bold",10,))
    L34.grid(row=8,column=3)
    L35=Label(viewCo,text=select_single_cons(count_rows)[4], font=("bold",10,))
    L35.grid(row=8,column=4)
    L36=Label(viewCo,text=select_single_cons(count_rows)[5], font=("bold",10,))
    L36.grid(row=8,column=5)
    L37=Label(viewCo,text=select_single_cons(count_rows)[6], font=("bold",10,))
    L37.grid(row=8,column=6)
    L38=Label(viewCo,text=select_single_cons(count_rows)[7], font=("bold",10,))
    L38.grid(row=8,column=7)
    L39=Label(viewCo,text=check_last_transit_location(count_rows), font=("bold",10,))
    L39.grid(row=8,column=8)
    #second-row-data-items
    L41=Label(viewCo,text=select_single_cons(count_rows-1)[0], font=("bold",10,))
    L41.grid(row=9,column=0)
    L42=Label(viewCo,text=select_single_cons(count_rows-1)[1], font=("bold",10,))
    L42.grid(row=9,column=1)
    L43=Label(viewCo,text=select_single_cons(count_rows-1)[2], font=("bold",10,))
    L43.grid(row=9,column=2)
    L44=Label(viewCo,text=select_single_cons(count_rows-1)[3], font=("bold",10,))
    L44.grid(row=9,column=3)
    L45=Label(viewCo,text=select_single_cons(count_rows-1)[4], font=("bold",10,))
    L45.grid(row=9,column=4)
    L46=Label(viewCo,text=select_single_cons(count_rows-1)[5], font=("bold",10,))
    L46.grid(row=9,column=5)
    L47=Label(viewCo,text=select_single_cons(count_rows-1)[6], font=("bold",10,))
    L47.grid(row=9,column=6)
    L48=Label(viewCo,text=select_single_cons(count_rows-1)[7], font=("bold",10,))
    L48.grid(row=9,column=7)
    L49=Label(viewCo,text=check_last_transit_location(count_rows-1), font=("bold",10,))
    L49.grid(row=9,column=8)
    #second-row-data-items
    L51=Label(viewCo,text=select_single_cons(count_rows-2)[0], font=("bold",10,))
    L51.grid(row=10,column=0)
    L52=Label(viewCo,text=select_single_cons(count_rows-2)[1], font=("bold",10,))
    L52.grid(row=10,column=1)
    L53=Label(viewCo,text=select_single_cons(count_rows-2)[2], font=("bold",10,))
    L53.grid(row=10,column=2)
    L54=Label(viewCo,text=select_single_cons(count_rows-2)[3], font=("bold",10,))
    L54.grid(row=10,column=3)
    L55=Label(viewCo,text=select_single_cons(count_rows-2)[4], font=("bold",10,))
    L55.grid(row=10,column=4)
    L56=Label(viewCo,text=select_single_cons(count_rows-2)[5], font=("bold",10,))
    L56.grid(row=10,column=5)
    L57=Label(viewCo,text=select_single_cons(count_rows-2)[6], font=("bold",10,))
    L57.grid(row=10,column=6)
    L58=Label(viewCo,text=select_single_cons(count_rows-2)[7], font=("bold",10,))
    L58.grid(row=10,column=7)
    L59=Label(viewCo,text=check_last_transit_location(count_rows-2), font=("bold",10,))
    L59.grid(row=10,column=8)

    L60 = Label(viewCo,text="", font=("bold",13,), pady="5")
    L60.grid(row=11,column=0, columnspan=12)
    L61 = Label(viewCo,text="Update consignment Location", font=("bold",13,),fg="green",bg="yellow", padx="10")
    L61.grid(row=12,column=0, columnspan=12)

    L62 = Label(viewCo,text="Consignment Num.")
    L62.grid(row=13,column=2, columnspan=2)
    E16=Entry(viewCo)
    E16.grid(row=14,column=2,columnspan=2)

    L63 = Label(viewCo,text="New Location")
    L63.grid(row=13,column=4, columnspan=2)
    E17=Entry(viewCo)
    E17.grid(row=14,column=4,columnspan=2)
    
    B30=Button(viewCo,text="Update", command=updateLocation, fg="white", bg="green")
    B30.grid(row=14,column=6)



    L70=Label(viewCo)
    L70.grid(row=15,column=0, columnspan=12)


    B16 = Button(text="Refresh", command=refreshScreen, fg="white", bg="green")
    B16.grid(row=15, column=10,padx="10",pady="10")

    B20 = Button(viewCo,text="Go Back", command=doSomething, fg="white", bg="green")
    B20.grid(row=15, column=12,padx="10",pady="10")
    
    viewCo.mainloop()

#viewCon("admin")
