import os
import sqlite3
conn = sqlite3.connect('emp.db')        
conn.row_factory = sqlite3.Row
def sql_query(query):
    conn = sqlite3.connect('emp.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    conn = sqlite3.connect('emp.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()
    return cur.rowcount
  

def sql_query2(query,var):
    conn = sqlite3.connect('emp.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
