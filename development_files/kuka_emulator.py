"""
Author: Eren Sezener (erensezener@gmail.com)
Date: May 17, 2014

Description: Keeps the server alive by simulating KUKA. However, unlike KUKA sends the IPOC as a dummy text.

Status: Works correctly.

Dependencies:

Known bugs: -

"""
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 49153

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

data = "<IPOC>0000000000</IPOC>"

while True:


    sock.sendto(data, (UDP_IP, 49152))
    received_data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    # print ("received message:", received_data)
    if 'X=\"0.0000\"' not in received_data and 'A1=\"0.0000\"' not in received_data:
        print received_data
    ipoc_begin_tag_index = received_data.index("<IPOC>")
    ipoc_end_tag_index = received_data.index("</IPOC>")
    old_ipoc = received_data[ipoc_begin_tag_index + 6: ipoc_end_tag_index]
    new_ipoc = str(int(old_ipoc) + 1).zfill(10)
    data = "<IPOC>"+new_ipoc+"</IPOC>"
