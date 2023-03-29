from socket import *

class UDPServerHelper:
	def __init__(self, port):
		self.serverSocket = socket(AF_INET, SOCK_DGRAM) 
		self.serverSocket.bind(('', port))
		print("The server is ready to receive")

	def recv(self, size):
		message, clientAddress = self.serverSocket.recvfrom(size) 
		return message, clientAddress