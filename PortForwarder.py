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
    while True:
        buffer = src.recv(0x400)
        if len(buffer) == 0:
            print "[-] No data received! Breaking..."
            break
        # print "[+] %s:%d => %s:%d [%s]" % (src_address, src_port, dst_address, dst_port, repr(buffer))
        if direction:
            print "[+] %s:%d >>> %s:%d [%d]" % (src_address, src_port, dst_address, dst_port, len(buffer))
        else:
            print "[+] %s:%d <<< %s:%d [%d]" % (dst_address, dst_port, src_address, src_port, len(buffer))
        dst.send(handle(buffer))
    try:
        print "[+] Closing src connecions! [%s:%d]" % (src_address, src_port)
        src.shutdown(socket.SHUT_RDWR)
        src.close()    
        print "[+] Closing dest connecions! [%s:%d]" % (dst_address, dst_port)
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


    print '[+] Server started [%s:%d]' % (local_host, local_port)
    while True:
        print "Current loadBalanceIndex is:" + str(loadBalanceIndex)
        print "remote length " + str(len(remote_port))
        print "adding" + str((loadBalanceIndex + 1) % len(remote_port))


        local_socket, local_address = server_socket.accept()
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "trying to connect to remote port:" + str(remote_port[loadBalanceIndex])
        remote_socket.connect((remote_host, remote_port[loadBalanceIndex]))
        loadBalanceIndex = (loadBalanceIndex + 1) % len(remote_port)

        s = threading.Thread(target=transfer, args=(
            remote_socket, local_socket, False))
        r = threading.Thread(target=transfer, args=(
            local_socket, remote_socket, True))

        s.start()
        r.start()

    print "[+] Releasing resources..."
    remote_socket.shutdown(socket.SHUT_RDWR)
    remote_socket.close()
    local_socket.shutdown(socket.SHUT_RDWR)
    local_socket.close()
    print "[+] Closing server..."
    server_socket.shutdown(socket.SHUT_RDWR)
    server_socket.close()
    print "[+] Server shuted down!"


def main():
    LOCAL_HOST = "141.252.218.55"
    LOCAL_PORT = 8080
    REMOTE_HOST = "141.252.207.174" #raw_input("IP? ") 
    print REMOTE_HOST
    test = str(REMOTE_HOST)
    REMOTE_PORTS = [8888, 8889]
    MAX_CONNECTION = 0x10
    server(LOCAL_HOST, LOCAL_PORT, test, REMOTE_PORTS, MAX_CONNECTION)


if __name__ == "__main__":
    main()