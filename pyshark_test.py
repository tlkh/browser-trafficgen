import pyshark

import matplotlib.pyplot as plt
import numpy as np
import time

capture = pyshark.LiveCapture(interface='ens19')
capture.set_debug()

fig = plt.figure(figsize=(8,6))

known_ip = {}

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
        breakdown_src = packet.ip.src.split(".")
        breakdown_dst = packet.ip.dst.split(".")
        if breakdown_dst[0]=="1":
            source = (int(breakdown_src[-1]), float(breakdown_src[-2]+"."+breakdown_src[-1]))
            dest = (int(breakdown_dst[-1]), float(breakdown_dst[-2]+"."+breakdown_dst[-1]))
            plt.scatter(source[0],source[1])
            plt.scatter(dest[0],dest[1])
            plt.plot(np.array([source[0],dest[0]]),np.array([source[1],dest[1]]))
            plt.pause(0.001)

    elif packet.transport_layer== "UDP":
        print("UDP", packet.udp.srcport, packet.udp.dstport)
        try:
            print("TCP", packet.ip.src, packet.ip.dst)
            breakdown_src = packet.ip.src.split(".")
            breakdown_dst = packet.ip.dst.split(".")
            if breakdown_dst[0]=="1":
                source = (int(breakdown_src[-1]), float(breakdown_src[-2]+"."+breakdown_src[-1]))
                dest = (int(breakdown_dst[-1]), float(breakdown_dst[-2]+"."+breakdown_dst[-1]))
                plt.scatter(source[0],source[1])
                plt.scatter(dest[0],dest[1])
                plt.plot(np.array([source[0],dest[0]]),np.array([source[1],dest[1]]))
                plt.pause(0.001)
        except:
            print("TCP", packet.ipv6.src, packet.ipv6.dst)
        
    else:
        try:
            print("None", packet.ip.src, packet.ip.dst)
        except Exception as e:
            print(e)
            print(packet)
        try:
            print("ICMP:", icmp.type)
        except Exception as e:
            print(e)
            print(packet)

    print("\n==========\n")

plt.show()
