import datetime
import sqlite3 as db
import time
# from tkinter import *
# from tkinter.ttk import *

# window = Tk()

# window.title("PI Hour Tracker")
# window.geometry('400x400')


# combo = Combobox(window)

# combo['values'] = (1, 2, 3, 4, 5, 0)

# combo.current(0)
# combo.grid(column = 5, row = 5)

# window.mainloop()

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
\t*Candles and Candles
\t*Dog Toys Ltd
\t*Guitar World
\t*Purses and More
""")
        req_client = input("\tEnter client to view data: ",)
        print("\n")
        getClientInfo(req_client)
    # elif user_choice == selection_options[3]:
    #     break
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
\t*Candles and Candles
\t*Dog Toys Ltd
\t*Guitar World
\t*Purses and More
""")
    pi_due = input("\tEnter client for PI due date: ")

    print("\tThe due date for this inventory is {}".format(clients_byWHS[pi_due]))

    today = datetime.date.today()
    delta = clients_byWHS[pi_due] - today
    print( "\tThere are %d days remaining until inventory must be completed." % (delta.days))

    time.sleep(5)
    intro()

def new_entry():
    add_date_to_list = str(input("\tEnter record date (m/d/yyyy): "))
    record_list.append(add_date_to_list)

    print("""
\tSelect:
\t*Indianapolis
\t*Louisville
\t*Nashville
\t*Orlando
""")
            
    add_warehouse_to_list = str(input("\tEnter warehouse: "))
    record_list.append(add_warehouse_to_list)

    print("""
Select:
\t*Candles and Candles
\t*Dog Toys Ltd
\t*Guitar World
\t*Purses and More
""")
            
    add_client_to_list = str(input("\tEnter client: "))
    record_list.append(add_client_to_list)

    print("""
\t*Prep Work
\t*Physical Counts
\t*Auditing
\t*Clean Up   
""")

    add_task_to_list = str(input("\tEnter task: "))
    record_list.append(add_task_to_list)

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

    time.sleep(3)
    intro()

# def view(task=None):
#     conn = db.connect("tracker.db")
#     cur = conn.cursor()
#     if task:
#         sql = '''
#         select * from tasks where task = '{}'
#         '''.format(task)
#     else:
#         sql = '''
#         select * from tasks
#         '''.format(task)
#     cur.execute(sql)
#     results = cur.fetchall()
#     return results

# print (view())

# Main Program

intro()