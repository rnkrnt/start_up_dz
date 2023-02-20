import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 60000))
    messege = input("Введите уведомление: ")
    sock.send(bytes(messege, encoding='UTF-8'))
    data = sock.recv(1024).decode('UTF-8')
    print(data)
    sock.close()