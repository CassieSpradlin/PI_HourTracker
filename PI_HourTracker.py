#import pandas as pd
#data = pd.read_csv('/Users/cassie/Documents/Project_Folder/PI_HourTracker/inventory_hours.csv')
#data.head()

import sqlite3 as db

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

def show_help():
    print("Add data record for Physical Inventory")
    print("""
Enter 'New Record' to add another record.
Enter 'DONE' to stop adding records.
Enter 'HELP' for this help.
""")

show_help()

def new_entry():


    add_date_to_list = str(input("Enter record date: "))
    record_list.append(add_date_to_list)
            
    add_warehouse_to_list = str(input("Enter warehouse: "))
    record_list.append(add_warehouse_to_list)
            
    add_client_to_list = str(input("Enter client: "))
    record_list.append(add_client_to_list)

    add_task_to_list = str(input("Enter task: "))
    record_list.append(add_task_to_list)

    add_hours_to_list = float(input("Enter hours: "))
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


while True:
    new_record = input("> ")
    if new_record == 'New Record':
        new_entry()
    elif new_record == 'DONE':
        break
    elif new_record == 'HELP':
        break





def view(task=None):
    conn = db.connect("tracker.db")
    cur = conn.cursor()
    if task:
        sql = '''
        select * from tasks where task = '{}'
        '''.format(task)
    else:
        sql = '''
        select * from tasks
        '''.format(task)
    cur.execute(sql)
    results = cur.fetchall()
    return results

print (view())