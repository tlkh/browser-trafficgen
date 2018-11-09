import pyshark

capture = pyshark.LiveCapture(interface='ens19')
capture.set_debug()

for packet in capture.sniff_continuously(packet_count=999):
    print("\n==========\n")
    print('Just arrived:')
    # '_packet_string', 'captured_length', 'eth', 'frame_info',
    # 'get_multiple_layers', 'get_raw_packet', 'highest_layer',
    # 'interface_captured', 'ipv6', 'layers', 'length', 'mdns',
    # 'number', 'pretty_print', 'show', 'sniff_time', 'sniff_timestamp',
    # 'transport_layer', 'udp']
    print("Layer:", packet.transport_layer)
    #print(packet)

    if packet.transport_layer== "TCP":
        print("TCP", packet.ip.src, packet.ip.dst)

    elif packet.transport_layer== "UDP":
        print("UDP", packet.udp.srcport, packet.udp.dstport)
        try:
            print("TCP", packet.ip.src, packet.ip.dst)
        except:
            print("TCP", packet.ipv6.src, packet.ipv6.dst)
        
    else:
        try:
            print("None", packet.ip.src, packet.ip.dst)
        except:
            pass
        try:
            print("ICMP:", icmp.type)
        except:
            pass
        print(packet)

    print("\n==========\n")
