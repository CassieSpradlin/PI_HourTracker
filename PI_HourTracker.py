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