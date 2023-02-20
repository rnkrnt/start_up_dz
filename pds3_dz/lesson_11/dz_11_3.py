import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 60000))
    sock.listen(10)
    print('Server is running, please, press ctrl+c to stop')
    while True:
        conn, addr = sock.accept()
        print('connected:', addr)
        data = conn.recv(1024).decode('utf-8')
        print(data)
        answer_list = data.split(" ")
        answer = str(len(answer_list))
        print(answer)
        conn.send(bytes(answer, encoding="utf-8"))

except KeyboardInterrupt as ex:
    print(f"Error: {ex}")
conn.close()
