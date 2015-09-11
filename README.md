# python-server-client

A partnered university assignment to write a file transfer program from scratch with Python (using high-level networking libraries like FTP was not allowed). I wrote the code for the client and my assignment partner wrote the code for the server.

## client.py

A command line program that takes 5 arguments:
* Filename to be read from server
* Filename under which received file is to be stored locally
* IP address or hostname of server (localhost if client is run on same machine)
* Port number of server
* Probability of packet loss (for testing purposes)

It sets up a UDP socket and sends read-request packets to the server in binary.  When it receives a read-response packet from the server, it unpacks payload, makes the necessary checks, and appends the file data received to the local file at the given start position. When the file has been received, it sends a close request packet to the server to close the file object.

## server.py

A command line program that listens on the specified port. It awaits the read-request packet from the client and sends read-respond packets containing portions of the file. 

