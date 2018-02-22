#!/usr/bin/env python
import socket
import threading
import sys


def handle(buffer):
    return buffer


def transfer(src, dst, direction):
    src_name = src.getsockname()
    src_address = src_name[0]
    src_port = src_name[1]
    dst_name = dst.getsockname()
    dst_address = dst_name[0]
    dst_port = dst_name[1]
    src.settimeout(1)
	
    while True:
        try:
            buffer = src.recv(0x400)
            if len(buffer) == 0:
                    break
            dst.send(handle(buffer))
        except Exception as inst:
            print "Ip released" 
            break
    try:
        src.shutdown(socket.SHUT_RDWR)
        src.close()    

        dst.shutdown(socket.SHUT_RDWR)
        dst.close()
    except Exception as inst:
        print inst


def server(local_host, local_port, remote_host, remote_port, max_connection):
    loadBalanceIndex = 0
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((local_host, local_port))
    server_socket.listen(max_connection)


    print 'Portforwarder started'
    while True:
        local_socket, local_address = server_socket.accept()
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        remote_socket.connect((remote_host, remote_port[loadBalanceIndex]))
        loadBalanceIndex = (loadBalanceIndex + 1) % len(remote_port)

        s = threading.Thread(target=transfer, args=(
            remote_socket, local_socket, False))
        r = threading.Thread(target=transfer, args=(
            local_socket, remote_socket, True))

        s.start()
        r.start()

    remote_socket.shutdown(socket.SHUT_RDWR)
    remote_socket.close()

    local_socket.shutdown(socket.SHUT_RDWR)
    local_socket.close()

    server_socket.shutdown(socket.SHUT_RDWR)
    server_socket.close()

def main():
    LOCAL_HOST = "127.0.0.1"#"141.252.218.55"
    LOCAL_PORT = 8080
    REMOTE_HOST = "127.0.0.1" #raw_input("IP? ") 
    test = str(REMOTE_HOST)
    REMOTE_PORTS = [8001, 8002, 8003, 8004, 8005, 8006, 8007]
    MAX_CONNECTION = 0x10
    server(LOCAL_HOST, LOCAL_PORT, test, REMOTE_PORTS, MAX_CONNECTION)


if __name__ == "__main__":
    main()
