#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = arp_request / broadcast
    answred, unanswred = scapy.srp(arp_request_broadcast, timeout=1)
    print(unanswred.summary())


scan("172.16.8.2/24")
