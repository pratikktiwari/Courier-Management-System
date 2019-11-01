def insert_db(student_reg_num, student_name, student_uname, student_pwd, student_mobile):
        import sqlite3
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        #c.execute('DROP TABLE students')
        c.execute('CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT, student_reg_num INTEGER(10),student_mobile INTEGER(12), student_uname TEXT UNIQUE, student_pwd TEXT)')

        param_query = """INSERT INTO `students` ('student_reg_num','student_name','student_uname','student_pwd','student_mobile') VALUES (?,?,?,?,?);"""
        data_tuple = (student_reg_num, student_name, student_uname, student_pwd, student_mobile)
        c.execute(param_query, data_tuple)
        conn.commit()

        #c.execute('SELECT * FROM students')
        #z=c.fetchall()
        #print(z)

        conn.close()


#insert_db(12343434, 'Pratik Tiwari', 'pratik','pratik', 8986729191)
        
###########################################################
        
def check_login(uname,pwd):
        import sqlite3
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        select_query = """SELECT * FROM students WHERE student_uname = ? AND student_pwd=?"""
        c.execute(select_query, (uname,pwd))
        record = c.fetchone()
        conn.close()
        #print(record)
        if type(record) is tuple:
                return True
        else:
                return False
        
###########################################################
        
def check_if_user_exists(uname):
        import sqlite3
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        select_query = """SELECT student_id FROM students WHERE student_uname = ?"""
        c.execute(select_query, (uname,))
        record = c.fetchone()
        conn.close()
        #print(record)
        if type(record) is tuple:
                return True
        else:
                return False
#print(check_if_user_exists('asa'))

###########################################################
        
def select_single_row_item(col_id,student_id):
        import sqlite3
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        select_query = """SELECT * FROM students WHERE student_id = ?"""
        c.execute(select_query, (student_id,))
        record = c.fetchone()
        conn.close()
        #col_id - 1-student_name, 2-student_reg_num, 3-student_mobile, 4-student_uname, 5-student_pwd
        return record[col_id]

#print(select_single_row_item(2,1))

###########################################################

def get_id_from_uname(username):
        import sqlite3
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        select_query = """SELECT student_id FROM students WHERE student_uname = ?"""
        c.execute(select_query, (username,))
        record = c.fetchone()
        conn.close()
        #col_id - 1-student_name, 2-student_reg_num, 3-student_mobile, 4-student_uname, 5-student_pwd
        return record[0]

#print(get_id_from_uname('pratik'))

###########################################################


def select_all_students():
        import sqlite3
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute('SELECT * FROM students')
        items_tuple = c.fetchall()
        conn.close()
        return items_tuple

#print(select_all_inventory_items())

###########################################################

def select_all_courier():
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        c.execute('SELECT * FROM c_items')
        items_tuple = c.fetchall()
        conn.close()
        return items_tuple
#print(select_all_courier())
###################################
def select_single_student(student_id):
        import sqlite3
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        select_query = """SELECT * FROM students WHERE student_id = ?"""
        c.execute(select_query, (student_id,))
        record = c.fetchone()
        conn.close()
        return record

#print(select_single_row(2))

###########################################################



def insert_db_c_items(item_name, item_weight, item_charge, item_destination, item_student_reg_num,item_expected_delivery_num_days):
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        #c.execute('DROP TABLE c_items')
        c.execute('CREATE TABLE IF NOT EXISTS c_items(item_id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT, item_weight INTEGER(5),item_charge INTEGER(5), item_destination TEXT, item_student_reg_num INTEGER(10), item_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, item_expected_delivery_num_days INTEGER(5))')

        param_query = """INSERT INTO `c_items` ('item_name','item_weight','item_charge','item_destination','item_student_reg_num','item_expected_delivery_num_days') VALUES (?,?,?,?,?,?);"""
        data_tuple = (item_name, item_weight, item_charge, item_destination, item_student_reg_num,item_expected_delivery_num_days)
        c.execute(param_query, data_tuple)
        conn.commit()

        #c.execute('SELECT * FROM c_items')
        #z=c.fetchall()
        #print(z)

        conn.close()

#insert_db_c_items('Samsung Tab',0.25,112,'Garhwa',11801876,4)
#select datetime(timestamp, 'localtime')
###################################################################

def insert_db_transit(transit_item_id, transit_location, transit_complete):
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        #c.execute('DROP TABLE c_items')
        c.execute('CREATE TABLE IF NOT EXISTS transit(transit_id INTEGER PRIMARY KEY AUTOINCREMENT, transit_item_id INTEGER, transit_location TEXT, transit_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, transit_complete INTEGER, FOREIGN KEY(transit_item_id) REFERENCES c_items(item_id))')

        param_query = """INSERT INTO `transit` ('transit_item_id','transit_location','transit_complete') VALUES (?,?,?);"""
        data_tuple = (transit_item_id, transit_location, transit_complete)
        c.execute(param_query, data_tuple)
        conn.commit()

        #c.execute('SELECT * FROM transit')
        #z=c.fetchall()
        #print(z)

        conn.close()
#insert_db_transit(2,'Jalandhar',0)
def select_all_item_info_user_id(reg_num):
        #SELECT * FROM table_a INNER JOIN table_b ON table_a.id=table_b.id
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        
        param_query = """SELECT c_items.item_name,c_items.item_expected_delivery_num_days,transit.transit_complete,transit.transit_location,transit.transit_timestamp FROM c_items INNER JOIN transit ON c_items.item_id=transit.transit_item_id WHERE c_items.item_student_reg_num=? ORDER BY transit.transit_id DESC;"""
        #data_tuple = (reg_num,)
        data_all = c.execute(param_query,(reg_num,))
        #z=c.fetchall()
        #print(z)
        return data_all
#select_all_item_info_user_id(11813081)
####################################################################
def check_if_item_exists(item_id):
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        select_query = """SELECT item_id FROM c_items WHERE item_id = ?"""
        c.execute(select_query, (item_id,))
        record = c.fetchone()
        conn.close()
        #print(record)
        if type(record) is tuple:
                return True
        else:
                return False
####################################################################

def check_last_transit_location(transit_item_id):
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        select_query = """SELECT transit_location FROM transit WHERE transit_item_id = ? ORDER BY transit_id DESC LIMIT 1"""
        #select_query = """SELECT * FROM transit"""
        #c.execute(select_query)
        c.execute(select_query, (transit_item_id,))
        record = c.fetchone()
        conn.close()
        if type(record)!=tuple:
                return "Not Started"
        else:
                return record[0]
#print(check_last_transit_location(3))
####################################################################
def select_count_rows_courier():
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        select_query = """SELECT COUNT(item_id) FROM c_items"""
        record=c.execute(select_query)
        record = c.fetchone()
        conn.close()
        return record
###################################################################
def select_single_cons(item_id):
        import sqlite3
        conn = sqlite3.connect('courier.db')
        c = conn.cursor()
        select_query = """SELECT * FROM c_items WHERE item_id = ? ORDER BY item_id DESC"""
        c.execute(select_query, (item_id,))
        record = c.fetchone()
        conn.close()
        return record

#print(select_single_row(2))
