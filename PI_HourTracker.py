import datetime
import sqlite3 as db
import time

def init():
    conn = db.connect("tracker.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists tasks (
        date string,
        warehouse string,
        client string,
        task string,
        hours float
        )
    '''
    cur.execute(sql)
    conn.commit()

record_list = []

#Functions

def intro():
    selection_options = ["1", "2", "3", "4", "5","0"]
    user_choice = ""
    while user_choice not in selection_options:
        print("""

\t1. Check Inventory Due Date of a Client
\t2. Add Another Record
\t3. View Data for Specific Client
\t4. Done Entering Records
\t5. Return to Help Menu

\t0. Quit

""")
        user_choice = input("\tEnter option number: ")

    if user_choice == selection_options[0]:
        check_dueDate()
    elif user_choice == selection_options[1]:
        new_entry()
    elif user_choice == selection_options[2]:
        print("""
\tSelect:
\t1. Candles and Candles
\t2. Dog Toys Ltd
\t3. Guitar World
\t4. Purses and More
""")
        req_client = input("\tEnter client number to view data: ",)
        print("\n")
        if req_client == '1':
            getClientInfo("Candles and Candles")
        elif req_client == '2':
            getClientInfo("Dog Toys Ltd")
        elif req_client == '3':
            getClientInfo("Guitar World")
        elif req_client == '4':
            getClientInfo("Purses and More")
    
    elif user_choice == selection_options[4]:
        intro()
    elif user_choice == selection_options[5]:
        exit()

def check_dueDate():
    clients_byWHS = {
        "Dog Toys Ltd" : datetime.date(2021, 7, 15),
        "Guitar World": datetime.date(2021, 7, 25),
        "Candles and Candles": datetime.date(2022, 1, 5),
        "Purses and More": datetime.date(2021, 10, 1)   
    }
    print("""
\tSelect:
\t1. Candles and Candles
\t2. Dog Toys Ltd
\t3. Guitar World
\t4. Purses and More
""")
    pi_due = input("\tEnter client number for PI due date: ")

    if pi_due == '1':
        print("\tThe due date for this inventory is {}".format(clients_byWHS["Candles and Candles"]))
    elif pi_due == '2':
        print("\tThe due date for this inventory is {}".format(clients_byWHS["Dog Toys Ltd"]))
    elif pi_due == '3':
        print("\tThe due date for this inventory is {}".format(clients_byWHS["Guitar World"]))
    elif pi_due == '4':
        print("\tThe due date for this inventory is {}".format(clients_byWHS["Purses and More"]))

    today = datetime.date.today()
    if pi_due == '1':
        delta = clients_byWHS["Candles and Candles"] - today
        print( "\tThere are %d days remaining until inventory must be completed." % (delta.days))
    elif pi_due == '2':
        delta = clients_byWHS["Dog Toys Ltd"] - today
        print( "\tThere are %d days remaining until inventory must be completed." % (delta.days))
    elif pi_due == '3':
        delta = clients_byWHS["Guitar World"] - today
        print( "\tThere are %d days remaining until inventory must be completed." % (delta.days))
    elif pi_due == '4':
        delta = clients_byWHS["Purses and More"] - today
        print( "\tThere are %d days remaining until inventory must be completed." % (delta.days))
    

    time.sleep(5)
    intro()

def new_entry():
    add_date_to_list = str(input("\tEnter record date (m/d/yyyy): "))
    record_list.append(add_date_to_list)

    print("""
\tSelect:
\t1. Indianapolis
\t2. Louisville
\t3. Nashville
\t4. Orlando
""")
            
    add_warehouse_to_list = str(input("\tEnter warehouse: "))
    if add_warehouse_to_list == '1':
        record_list.append("Indianapolis")
    elif add_warehouse_to_list == '2':
        record_list.append("Louisville")
    elif add_warehouse_to_list == '3':
        record_list.append("Nashville")
    elif add_warehouse_to_list == '4':
        record_list.append("Orlando")


    print("""
Select:
\t1. Candles and Candles
\t2. Dog Toys Ltd
\t3. Guitar World
\t4. Purses and More
""")
            
    add_client_to_list = str(input("\tEnter client: "))
    if add_client_to_list == '1':
        record_list.append("Candles and Candles")
    elif add_client_to_list == '2':
        record_list.append("Dog Toys Ltd")
    elif add_client_to_list == '3':
        record_list.append("Guitar World")
    elif add_client_to_list == '4':
        record_list.append("Purses and More")
    

    print("""
\t1. Prep Work
\t2. Physical Counts
\t3. Auditing
\t4. Clean Up   
""")

    add_task_to_list = str(input("\tEnter task: "))
    if add_task_to_list == '1':
        record_list.append("Prep Work")
    elif add_task_to_list == '2':
        record_list.append("Physical Counts")
    elif add_task_to_list == '3':
        record_list.append("Auditing")
    elif add_task_to_list == '4':
        record_list.append("Clean Up")
    

    add_hours_to_list = float(input("\tEnter hours: "))
    record_list.append(add_hours_to_list)

    def log(date, warehouse, client, task, hours):
        conn = db.connect("tracker.db")
        cur = conn.cursor()
        sql = '''
        insert into tasks values (
            '{}',
            '{}',
            '{}',
            '{}',
            {}
            )
        '''.format(date, warehouse, client, task, hours)
        cur.execute(sql)
        conn.commit()

    log(record_list[0], record_list[1], record_list[2], record_list[3], record_list[4])

    record_list.clear()

    print("\n\n\tSelect: \n\t2. Add Another Record \n\t4. Done Entering Records")



    while True:
        new_record = input("> ")
        if new_record == '2':
            new_entry()
        elif new_record == '4':
            intro()
        elif new_record == '5':
            intro
        elif new_record == '0':
            break

    time.sleep(3)
    intro()

def getClientInfo(client):

    sql_select_query = """select * from tasks where client = ?"""
    conn = db.connect("tracker.db")
    cur = conn.cursor()
    cur.execute(sql_select_query, (client,))
    records = cur.fetchall()
    print("\tTotal records for client:  ", len(records),"\n")
    for row in records:
        print("\tdate = ", row[0])
        print("\twarehouse  = ", row[1])
        print("\tclient  = ", row[2])
        print("\ttask  = ", row[3])
        print("\thours  = ", row[4],"\n")

    cur.close()

    time.sleep(4)
    intro()

intro()