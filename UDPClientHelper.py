from socket import *


class UDPHelper:
	def __init__(self, serverName, serverPort):
		self.serverName = serverName 
		self.serverPort = serverPort
		self.clientSocket = socket(AF_INET, SOCK_DGRAM) 

	def sendPacket(self, message):
		self.clientSocket.sendto(message, (self.serverName, self.serverPort)) 

# modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
# print(modifiedMessage.decode()) 
	def __del__(self):
		self.clientSocket.close()