import socket

example1 = "Hello!"
example2 = "How are you?"
example3 = "Bye!"



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
        if data == example1:
            answer = "Hi! How are you?"
        elif data == example2:
            answer = "I am fine!"
        elif data == example3:
            answer = "Goodbye!"
        else:
            answer = input("Введите ответ: ")
        conn.send(bytes(answer, encoding="utf-8"))

except KeyboardInterrupt as ex:
    print(f"Error: {ex}")
conn.close()
