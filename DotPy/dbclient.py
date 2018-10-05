import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.connect((host, port))

while True:
	query = input("Enter query to execute: ")
	s.send(query.encode("utf-8"))

	if query == "exit":
		break

	data = s.recv(100000)
	data_arr = pickle.loads(data)
	print("Query Result:\n%s" % (data_arr))

s.close()