#!/usr/bin/env python3
"""Create a deterministic, standards-compliant Ethernet/IPv4 PCAP for an isolated fictional case.

This is a genuine PCAP file format, but all packets are constructed synthetic data.
It contains DNS query/answer and TCP SYN/SYN-ACK/ACK metadata, no real captured traffic.
"""
from pathlib import Path
import ipaddress, struct

def checksum(data):
    if len(data)%2: data+=b"\x00"
    s=sum(struct.unpack("!%dH"%(len(data)//2),data))
    while s>>16: s=(s&65535)+(s>>16)
    return (~s)&65535

def ip4(src,dst,protocol,payload,ident):
    a=ipaddress.IPv4Address(src).packed;b=ipaddress.IPv4Address(dst).packed
    head=struct.pack("!BBHHHBBH4s4s",0x45,0,20+len(payload),ident,0,64,protocol,0,a,b)
    head=head[:10]+struct.pack("!H",checksum(head))+head[12:]
    return head+payload

def eth(payload):
    return bytes.fromhex("0200000000020200000000010800")+payload

def udp(src,dst,sp,dp,data,ident):
    segment=struct.pack("!HHHH",sp,dp,8+len(data),0)+data
    pseudo=ipaddress.IPv4Address(src).packed+ipaddress.IPv4Address(dst).packed+struct.pack("!BBH",0,17,len(segment))
    segment=segment[:6]+struct.pack("!H",checksum(pseudo+segment))+segment[8:]
    return eth(ip4(src,dst,17,segment,ident))

def tcp(src,dst,sp,dp,seq,ack,flags,ident):
    head=struct.pack("!HHIIHHHH",sp,dp,seq,ack,(5<<12)|flags,64240,0,0)
    pseudo=ipaddress.IPv4Address(src).packed+ipaddress.IPv4Address(dst).packed+struct.pack("!BBH",0,6,len(head))
    head=head[:16]+struct.pack("!H",checksum(pseudo+head))+head[18:]
    return eth(ip4(src,dst,6,head,ident))

def dns_name(domain):
    return b"".join(bytes([len(x)])+x.encode("ascii") for x in domain.split("."))+b"\x00"

def generate(path):
    client="192.0.2.47";resolver="192.0.2.53";server="198.51.100.24"
    question=dns_name("catalog-sync.example")+struct.pack("!HH",1,1)
    query=struct.pack("!HHHHHH",0x1201,0x0100,1,0,0,0)+question
    answer=struct.pack("!HHHHHH",0x1201,0x8180,1,1,0,0)+question+b"\xc0\x0c"+struct.pack("!HHIH",1,1,60,4)+ipaddress.IPv4Address(server).packed
    frames=[
        (40,udp(client,resolver,53001,53,query,1)),
        (41,udp(resolver,client,53,53001,answer,2)),
        (51,tcp(client,server,52014,443,1000,0,2,3)),
        (52,tcp(server,client,443,52014,3000,1001,18,4)),
        (53,tcp(client,server,52014,443,1001,3001,16,5))
    ]
    # 2026-09-22T02:06:00Z + offset seconds
    import datetime
    base=int(datetime.datetime(2026,9,22,2,6,tzinfo=datetime.timezone.utc).timestamp())
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("wb") as f:
        f.write(struct.pack("<IHHIIII",0xa1b2c3d4,2,4,0,0,65535,1))
        for seconds,frame in frames:
            f.write(struct.pack("<IIII",base+seconds,0,len(frame),len(frame)))
            f.write(frame)
    return len(frames)

if __name__=="__main__":
    root=Path(__file__).resolve().parents[1]
    print("PASS: wrote",generate(root/"build/artifacts/network/synthetic_dns_tcp.pcap"),"synthetic packets")
