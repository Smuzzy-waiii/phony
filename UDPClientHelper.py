from socket import *


class UDPHelper:
	def __init__(self, serverName, serverPort, clientPort):
		self.serverName = serverName 
		self.serverPort = serverPort
		self.socket = socket(AF_INET, SOCK_DGRAM) 
		self.socket.bind(('', clientPort))

	def sendPacket(self, message):
		self.socket.sendto(message, (self.serverName, self.serverPort)) 

	def recv(self, size):
		message, clientAddress = self.socket.recvfrom(size) 
		return message, clientAddress

	def __del__(self):
		self.socket.close()