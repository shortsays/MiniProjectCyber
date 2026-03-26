from scapy.all import Raw

def analyze_http(packet):
    try:
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors="ignore")

            if "Host:" in payload:
                host = payload.split("Host: ")[1].split("\r\n")[0]
                first_line = payload.split("\r\n")[0]
                path = first_line.split(" ")[1]

                return f"http://{host}{path}"
    except:
        return None

    return None