import pyshark

import matplotlib.pyplot as plt
import numpy as np
import time

from collections import deque

capture = pyshark.LiveCapture(interface='ens19')
capture.set_debug()

fig = plt.figure(figsize=(8,6))

MAX_LEN = 20

tcp_list_x = deque([],maxlen=MAX_LEN)
tcp_list_y = deque([],maxlen=MAX_LEN)

udp_list_x = deque([],maxlen=MAX_LEN)
udp_list_y = deque([],maxlen=MAX_LEN)

other_list_x = deque([],maxlen=MAX_LEN)
other_list_y = deque([],maxlen=MAX_LEN)

known_ip = {}

def create_loc(ip):
    global known_ip
    if str(ip) not in known_ip:
        known_ip[str(ip)] = np.random.random()*np.random.randint()


def get_loc(ip):
    global known_ip
    return float(known_ip[str(ip)])

for packet in capture.sniff_continuously(packet_count=999):
    plt.clf()
    print("\n==========\n")
    print('Just arrived:')
    # '_packet_string', 'captured_length', 'eth', 'frame_info',
    # 'get_multiple_layers', 'get_raw_packet', 'highest_layer',
    # 'interface_captured', 'ipv6', 'layers', 'length', 'mdns',
    # 'number', 'pretty_print', 'show', 'sniff_time', 'sniff_timestamp',
    # 'transport_layer', 'udp']
    print("Layer:", packet.transport_layer)
    #print(packet)

    if packet.transport_layer == "TCP":
        print("TCP", packet.ip.src, packet.ip.dst)
        breakdown_src = packet.ip.src.split(".")
        breakdown_dst = packet.ip.dst.split(".")
        if breakdown_dst[0]=="1":
            source = float(breakdown_src[-2]+"."+breakdown_src[-1])
            dest = float(breakdown_dst[-2]+"."+breakdown_dst[-1])

            create_loc(source)
            create_loc(dest)

            plt.scatter(get_loc(source),source, c="red", label=packet.ip.src)
            plt.scatter(get_loc(dest), dest, c="red", label=packet.ip.dst)
            tcp_list_x.append(np.array([get_loc(source),get_loc(dest)]))
            tcp_list_y.append(np.array([source,dest]))
            plt.plot(tcp_list_x, tcp_list_y, color="red", marker="^", linestyle="--", linewidth=int(int(packet.length)/1000), markersize=12)
            plt.pause(0.001)

    elif packet.transport_layer == "UDP":
        print("UDP", packet.udp.srcport, packet.udp.dstport)
        try:
            print("TCP", packet.ip.src, packet.ip.dst)
            breakdown_src = packet.ip.src.split(".")
            breakdown_dst = packet.ip.dst.split(".")
            if breakdown_dst[0]=="1":
                source = float(breakdown_src[-2]+"."+breakdown_src[-1])
                dest = float(breakdown_dst[-2]+"."+breakdown_dst[-1])

                create_loc(source)
                create_loc(dest)

                plt.scatter(get_loc(source),source, c="blue", label=packet.ip.src)
                plt.scatter(get_loc(dest), dest, c="blue", label=packet.ip.dst)
                udp_list_x.append(np.array([get_loc(source),get_loc(dest)]))
                udp_list_y.append(np.array([source,dest]))
                plt.plot(udp_list_x, udp_list_y, color="blue", marker="^", linestyle="--", linewidth=int(int(packet.length)/1000), markersize=12)
                plt.pause(0.001)
        except:
            print("TCP", packet.ipv6.src, packet.ipv6.dst)
        
    else:
        try:
            print("None", packet.ip.src, packet.ip.dst)
            breakdown_src = packet.ip.src.split(".")
            breakdown_dst = packet.ip.dst.split(".")
            if breakdown_dst[0]=="1":
                source = float(breakdown_src[-2]+"."+breakdown_src[-1])
                dest = float(breakdown_dst[-2]+"."+breakdown_dst[-1])

                create_loc(source)
                create_loc(dest)

                plt.scatter(get_loc(source),source, c="green", label=packet.ip.src)
                plt.scatter(get_loc(dest), dest, c="green", label=packet.ip.dst)
                other_list_x.append(np.array([get_loc(source),get_loc(dest)]))
                other_list_y.append(np.array([source,dest]))
                plt.plot(other_list_x, other_list_y, color="green", marker="^", linestyle="--", linewidth=int(int(packet.length)/1000), markersize=12)
                plt.pause(0.001)
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
