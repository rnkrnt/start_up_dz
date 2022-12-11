import socket
import logging

# Программа звітує Warning коли повідомленя з клієнта приходить кирилицею
# Программа звітує Error коли спочатку відклучається клієнт а потім сервер

def my_server():
    logger = logging.getLogger("exampleApp.dz_15_1")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', 60000))
        sock.listen(10)
        print('Server is running, please, press ctrl+c to stop')
        logger.info("exampleApp.dz_15_1.server_started")
        while True:
            conn, addr = sock.accept()
            print('connected:', addr)
            data1 = conn.recv(1024).decode('latin1')
            print(data1)
            data_code = data1.encode('latin1')
            data2 = data_code.decode('utf-8')
            logger_warning = logging.getLogger("exampleApp.dz_15_1")
            if not data1 == data2:
                print("Кодировка клиента отличается от кодировки сервера")
                logger_warning.warning("Different encoding for server and client messages")



            answer = input("Введите ответ: ")
            conn.send(bytes(answer, encoding="latin1"))

    except KeyboardInterrupt as ex:
        logger_error = logging.getLogger("exampleApp.dz_15_1")
        print(f"Error: {ex}")
        logger_error.error("Connection error: Client disconnected")
    conn.close()