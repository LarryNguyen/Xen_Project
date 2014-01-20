#!/usr/bin/env python

# echo server program

import socket

def create_server(port):
	HOST = ''
	PORT = port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST,PORT))
	s.listen(1)
	conn, addr = s.accept()
	return conn

# echo client program
def create_client(serverIP, port):
	HOST = serverIP
	PORT = port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST,PORT))
	return s

def receive_data(conn):
	return conn.recv(1024)

def send_data(conn, data):
	conn.sendall(data)

def close(conn):
	conn.close()

