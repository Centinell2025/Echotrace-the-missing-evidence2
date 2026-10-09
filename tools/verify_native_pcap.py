#!/usr/bin/env python3
"""Validate generated synthetic PCAP structure and case correlations."""
from pathlib import Path
import csv, ipaddress, struct
p=Path(__file__).resolve().parents[1]/"build/artifacts/network/synthetic_dns_tcp.pcap"
data=p.read_bytes()
assert len(data)>=24
magic,major,minor,zone,sig,snap,link=struct.unpack_from("<IHHIIII",data)
assert (magic,major,minor,link)==(0xa1b2c3d4,2,4,1)
pos=24;packets=[];previous=0
while pos<len(data):
    assert pos+16<=len(data)
    sec,usec,inc,orig=struct.unpack_from("<IIII",data,pos);pos+=16
    assert inc==orig and inc>=14+20 and pos+inc<=len(data)
    frame=data[pos:pos+inc];pos+=inc
    assert frame[12:14]==b"\x08\x00"
    ip=frame[14:];ihl=(ip[0]&15)*4
    assert ip[0]>>4==4 and ihl==20
    assert struct.unpack_from("!H",ip,2)[0]==len(ip)
    src=str(ipaddress.IPv4Address(ip[12:16]));dst=str(ipaddress.IPv4Address(ip[16:20]))
    proto=ip[9];segment=ip[ihl:]
    sport,dport=struct.unpack_from("!HH",segment)
    assert sec>=previous;previous=sec
    packets.append((src,dst,proto,sport,dport,segment))
assert pos==len(data) and len(packets)==5
assert packets[0][2:5]==(17,53001,53)
assert packets[1][2:5]==(17,53,53001)
assert b"catalog-sync" in packets[0][5] and ipaddress.IPv4Address("198.51.100.24").packed in packets[1][5]
assert packets[2][:5]==("192.0.2.47","198.51.100.24",6,52014,443)
assert packets[3][:5]==("198.51.100.24","192.0.2.47",6,443,52014)
assert packets[4][:5]==packets[2][:5]
with (p.parent/"flows.csv").open(newline="",encoding="utf-8") as f:
    flows=list(csv.DictReader(f))
assert any(x["flow_id"]=="FLOW-1201" and x["src_ip"]==packets[2][0] and x["dst_ip"]==packets[2][1] for x in flows)
print("PASS: native-format synthetic PCAP, 5 Ethernet/IPv4 packets, DNS and TCP handshake, flow correlation")
print("LIMITATION: synthetic packet metadata; no captured TLS payload or real incident traffic")
