# -*- coding: utf-8 -*-

import socket
import os

def get_response(request):


    request = request.decode()

    try:
        start = request.index(' ')
    except ValueError:
        return "HTTP/1.1 405 Method Not Allowed\n\n".encode()  # после GET обязательно будет пробел
        #  если нет, то это не он.
    if (request[:start] != "GET"):
        return "HTTP/1.1 405 Method Not Allowed\n\n".encode()  # продолжение защиты от прочих запросов


    try:
        end = request.index(' ', start + 1)  # ищем конец запроса
    except ValueError:
        return "HTTP/1.1 405 Method Not Allowed\n\n".encode()


    start += 1

    pathRequest = request[start:end]
    if (pathRequest == '/'):
        try:
            userAgntIndex = request.index('User-Agent')
            usr = request[userAgntIndex + 12:].split()[0]  # 12 тк после U-A идет ":" и  " "
            return ('HTTP/1.1 200 OK\n\n Hello mister! You are: {}'.format(usr)).encode()
        except ValueError:
            return ("HTTP/1.1 400 Bad Request\n\n" + 'User-Agent error').encode()

    elif (pathRequest.startswith('/test')):
        if (pathRequest == '/test' or pathRequest == '/test/'):
            return ("HTTP/1.1 200 OK\n\n {}".format(request)).encode()

    elif (pathRequest.startswith('/media')):
        if (pathRequest == '/media' or pathRequest == '/media/'):
            result = "HTTP/1.1 200 OK\n\n".encode()

            for f in os.listdir("files"):
                path = "files/" + f
                if (os.path.exists(path)):
                    with open(path, 'rb') as file:
                        result += f.encode() +  "\n".encode() + file.read() + "\n".encode()
            return  result
        else:
            try:
                filename = pathRequest[pathRequest.index('/', 1):]
                path = "files" + filename
            except ValueError: 
                return "HTTP/1.1 404 Not found\n\n Bad path request\n".encode()

            if (os.path.exists(path)):
                with open(path, 'r') as file:
                    result = "HTTP/1.1 200 OK\n\n".encode() + file.read()
                    return result
            else:
                return "HTTP/1.1 404 Not found\n\n File Not found\n".encode()

    return "HTTP/1.1 404 Not found\n\n Not found\n".encode() # в случае если пролетим все if / elif








server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # назначаем хост и порт
server_socket.listen(0)  # отслеживаем попытки подключения новых клиентов,
# параметр определяет сколько входящих соединений можно положить в очередь на соединение

print ('Server started...\n')

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print ('Got new client', client_socket.getsockname())  # выводим IP подключившегося
        # подключившегося к серверу.
        request_string = client_socket.recv(2048)  # получаем данные от клиента (GET ...), размер буфера 2048 байт
        client_socket.send(get_response(request_string))   #  вызываем get_response, передавая полученные данные
        #  отправляем ответ
    except KeyboardInterrupt:  # остановка сервера вручную
        print ('Stopped')
        server_socket.close()  # закрываем сокет
        exit()

