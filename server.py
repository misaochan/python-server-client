"""
@title server.py
@authour Cody Harrington (cah143), Josephine Lim (tcl44)
@description Server program for COSC364. 
May be optimised once completed, if there is time.
http://www.python.org/doc/essays/list2str.html
http://wiki.python.org/moin/PythonSpeed/PerformanceTips
"""

from socket import *
import os.path
import argparse

class Server(object):
    
    def __init__(self):
        self.ip = 'localhost'
        self.port = 5000
        # Comment out the line above and uncomment the line below to test the
        # server at the command line
        #port_number = self.parse_arguments()
        self.address = (self.ip, self.port)
        self.buffer_ = 1024
        
        self.udp_socket = self.init_socket(self.address)
        
        self.epoch_number = self.get_epoch_number();
        self.handle_number = 0
        
        self.listen(self.address, self.packet_buffer)
        
    def parse_arguments(self):
        """Parses the port number at the command line. Returns port number."""
        # Create an instance of the command line argument parser
        parser = argparse.ArgumentParser(description='File server.')
        # Set the parser to accept 1 integer argument
        parser.add_argument('Port', metavar='p', type=int, nargs=1)
        # Parse the command line argument into a variable
        port = parser.parse_args()
        
        return port
    
    def init_socket(self):
        """Creates socket for use. Returns an active UDP socket."""
        # Create a UDP Socket
        udp_socket = socket(AF_INET, SOCK_DGRAM)
        # Connect it to the local machine address on the specified port
        udp_socket.bind(self.address)
        udp_socket.setblocking(True)
        
        return udp_socket
    
    def get_epoch_number(self):
        """
        Checks to see if file "epoch.number" exists. If it doesn't, an
        error is returned. Otherwise, the first line is read for a single 
        integer, which is stored as the epoch number. This number is then
        incremented by 1, and is written into the file over the old number
        """
        if os.path.isfile('epoch.number'):
            f = open('epoch.number', 'r+')
            epoch_number = int(f.readline())
            epoch_number += 1
            f.write(str(epoch_number))
        else:
            f = open('epoch.number', 'r+')
            epoch_number = '1'
            f.write(epoch_number)
            
        f.close()
        
        return epoch_number
            
    def recv_open_request(self):
        """Specifies what the server should do if an open-request is received"""
        # To be completed
        pass
    
    def recv_read_request(self):
        """Specifies what the server should do if a read-request is received"""
        # To be completed
        pass
    
    def recv_close_request(self):
        """Specifies what the server should do if a close-request is received"""
        # To be completed
        pass
    
    def recv_invalid_request(self):
        """Specifies what should happen should an invalid request be made"""
        # To be completed
        pass
    
    def listen(self):
        """
        Enters into an infinite loop and listens on the specified UDP socket.
        """
        while (1):
            print ("Listening at address %s on port %d" % (self.ip, self.port))
            # Listen for data
            packet_data = self.udp_socket.recv(self.buffer_)
            # When data is received
            if packet_data:
                # Need to specify how a packet request is structured
                pass
            
            
server_process = Server()