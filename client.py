"""
@title client.py
@author Cody Harrington (cah143), Josephine Lim (tcl44)
@description Client program for COSC364. 
0 = 0000 = close request
1 = 0001 = read request
2 = 0010 = read response
4 = 0100 = open request
8 = 1000 = open response

"""

#TODO: Timers to initiate re-transmissions. Why timeout of 1 second?
#TODO: What to do with invalid packets received. How to discard? What do we do after that, return to mainloop?
#TODO: Error msgs indicating reason the file transfer could not be completed. What are the cases in which this would happen?

from socket import *
import sys

class Client(object):
	
    def __init__(self):
        """Sets up socket, obtains 4 values at command line:
        Filename to be read from server
        Filename under which received file is to be stored locally
        IP Addr of server
        Port number of server	
	"""
        self.client_socket = socket(AF_INET, SOCK_DGRAM)
	
	
	self.file_read = str(sys.argv[1])
	self.file_store = str(sys.argv[2])
	self.ip = str(sys.argv[3])
	self.port = int(sys.argv[4])
    
	
        #TODO: Throw error msgs for port (and IP?) range and format.
    
    def recv_invalid_response(self, recv_data):
	#What to do when bit signature is invalid or wrong packet type. Discard packet and wait? Must we notify user?
	pass
    
  
    def send_open_request(self):
        """Sends an open-request packet to the server."""
        # Carries filename to be read(as ASCII str) as sole param

	#Concatenates "1101" (signature) and "0001" (open_request type) to beginning of data (all strs)
	send_data = "%dx%dx%s" % (1101, 1000, self.file_read)
	self.client_socket.sendto(send_data, self.ip)

	pass

    
    def recv_open_response(self, recv_payload):
        """Specifies what the client does when it receives an (already-validated) open-response
        packet from the server. Calls send_read_request."""
	
	#The str sent to this function is already the payload, header has been stripped
	
        # Read status field. If set to 0, ignore remaining fields and generate error msg (file not found). 
	split_payload = recv_payload.split("x")
	status = split_payload[0]
	if status == 0:
	    print "File not found."
	    sys.exit()
	
	#If set to 1, read remaining fields.
	elif status == 1:
	    # Read file-length, epoch no. and handle no. fields, store outside function
	    
	    self.file_length = split_payload[1]
	    self.epoch_number = split_payload[2]	    
	    self.handle_number = split_payload[3]

	    send_read_request()
    
    def send_read_request(self):
        """Sends a read request packet to the server"""
        # Packet contains the fields:
        # 1) File-handle (from open_response packet)
        # 2) Integer giving the start position of the block to read from the file??? (How do we know this?)
        # 3) Number of bytes to read (158 bytes - multiple of Ethernet MTU (1500)?)
	
	
        
        pass
    
    def recv_read_response(self):
        """Specifies what the client does when it receives a read-response
        packet from the server."""
        
        #Read data bytes and write them into a file to be stored locally
        pass
    
    
    def send_close_request(self):
        """Sends a close request packet to the server"""
        
        # Do we really need this? UDP is connectionless, so there was no connection to close to begin with.
        pass
    

    def mainloop(self):
	"""Main loop of client. Loops until user exits."""
	
	
	while (1):
	    #TODO: how do we exit? 
	    user_exit = raw_input("Type Q to exit: ")
	    
	    #call send_open_request() to send the open request packet 
	    self.send_open_request()
	    recv_data = self.client_socket.recv(self.buffer_)
		
	    #Check the headers of the packet received for validity
	    if recv_data:
		#str.split("x") to get the fields
		split_data = recv_data.split("x")
		
		bit_signature = split_data[0]
		response_type = split_data[1]
		recv_payload = split_data[2:]
		
		# If bit signature is not correct, the packet is invalid.
		if bit_signature != "1101":
		    recv_invalid_response(recv_data)
		else:
		    # Check what type of response the packet is
		    if response_type == "1000":
			recv_open_response(recv_payload)
		    elif response_type == "0010":
			recv_read_response(recv_payload)
		    else:
			recv_invalid_response(recv_data)
			
			
	    if (user_exit == "Q"):
		break
	self.client_socket.close()	

#main method would make a Client object with the cmd line params passed to constructor. 
#Then it would start the main loop




client = Client()
client.mainloop()

