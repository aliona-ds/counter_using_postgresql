import psycopg2
from threading import Thread
import time

def postgre_conn():
    con =  psycopg2.connect(host='localhost', 
                            port=5432, 
                            dbname="postgres", 
                            user="postgres", 
                            password="O1234567")
    return con

def counter_function():
    pcon = postgre_conn()
    curr = pcon.cursor()
    for i in range(10000):
        curr.execute("""update user_counter set counter = counter + 1 where user_id = %s""", (1,))
        pcon.commit()
    curr.close()
    pcon.close()

conn = postgre_conn()
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS user_counter;""")
cur.execute("""CREATE TABLE user_counter (user_id integer, counter integer, version integer);""")
cur.execute("""INSERT INTO user_counter (user_id, counter, version)
               VALUES (%s, %s, %s);""",
            (1, 1, 0))
conn.commit()

thr_list = []
t = time.time()
for i in range(10):
    thr = Thread(target=counter_function)
    thr_list.append(thr)
    thr.start()
    print('Thread ' + str(i) + ' started')

for i in thr_list:
    i.join()
    print('Thread ' + str(i) + ' finiched')

t = time.time() - t

cur.execute("""SELECT counter FROM user_counter WHERE user_id = 1""")
print('Resulting counter from PostgeSQL = ' + str(cur.fetchone()[0]))
print('Counter running time = ' + str(t) + ' seconds')