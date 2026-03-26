from scapy.all import sniff
from scapy.layers.dns import DNSQR
from scapy.layers.tls.all import TLSClientHello
from http_analyzer import analyze_http


def process_packet(packet, callback):

    if packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode()
        callback("DNS", domain)


    url = analyze_http(packet)
    if url:
        callback("HTTP", url)


    if packet.haslayer(TLSClientHello):
        try:
            for ext in packet[TLSClientHello].ext:
                if hasattr(ext, "servernames"):
                    for sni in ext.servernames:
                        domain = sni.servername.decode()
                        callback("HTTPS", domain)
        except:
            pass


def start_sniffing(callback):
    sniff(filter="tcp or udp", prn=lambda pkt: process_packet(pkt, callback), store=0)