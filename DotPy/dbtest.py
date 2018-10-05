import pymysql as sql
import socket as skt
import pickle

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
host = skt.gethostname()
port = 9999
s.bind((host, port))
s.listen(10)

conn = sql.connect("localhost", "root", "", "cell_cluster")
cursor = conn.cursor()

while True:
	cskt, addr = s.accept()
	print("Connected to %s" % str(addr))
	
	query = cskt.recv(1024)
	query = query.decode("utf-8")
	print(query)
	if query == "exit":
		break
	
	cursor.execute(str(query))
	data_arr = cursor.fetchall()
	data = pickle.dumps(data_arr)
	cskt.send(data)

cskt.close()
s.close()
conn.close()
