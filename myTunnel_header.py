
from scapy.all import *
import sys, os

TYPE_MYTUNNEL = 0x1212
TYPE_IPV4 = 0x0800

class MyTunnel(Packet):
    name = "MyTunnel"
    fields_desc = [
        SourceIPField("IP_Mal", 0),
        IntField("TIME", 0),
        ShortField("flag", 0),
        ShortField("pid", 0),
        ShortField("dst_id", 0)
    ]
    def mysummary(self):
        return self.sprintf("IP_Mal=%IP_Mal%, TIME=%TIME%, flag=%flag%, pid=%pid%, dst_id=%dst_id%")


bind_layers(Ether, MyTunnel, type=TYPE_MYTUNNEL)
bind_layers(MyTunnel, IP, pid=TYPE_IPV4)

