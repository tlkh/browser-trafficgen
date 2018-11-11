import pyshark
import matplotlib.pyplot as plt
import numpy as np
import time
from threading import Thread
from collections import deque

capture = pyshark.LiveCapture(interface='ens19')
capture.set_debug()

MAX_LEN = 20

tcp_list_x = deque([], maxlen=MAX_LEN)
tcp_list_y = deque([], maxlen=MAX_LEN)

udp_list_x = deque([], maxlen=MAX_LEN)
udp_list_y = deque([], maxlen=MAX_LEN)

other_list_x = deque([], maxlen=MAX_LEN)
other_list_y = deque([], maxlen=MAX_LEN)

known_ip = {}


class liveplot(object):
    def __init__(self):
        self.fig = plt.figure(figsize=(8, 6))

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # event loop
        global tcp_list_x, tcp_list_y
        global udp_list_x, udp_list_y
        #global other_list_x, other_list_y
        global known_ip

        while True:
            if self.stopped:
                return
            else:
                plt.cla()
                for ip_loc in known_ip:
                    plt.scatter(get_loc(ip_loc), float(ip_loc), c="black")
                plt.plot(tcp_list_x, tcp_list_y, color="red", linestyle="--", linewidth=int(int(packet.length)/1000))
                plt.plot(udp_list_x, udp_list_y, color="blue", linestyle="--", linewidth=int(int(packet.length)/1000))
                plt.pause(1)

        plt.show()

    def stop(self):
        self.stopped = True


def create_loc(ip):
    global known_ip
    if str(ip) not in known_ip:
        known_ip[str(ip)] = np.random.random()*np.random.randint(10)


def get_loc(ip):
    global known_ip
    return float(known_ip[str(ip)])

live_dashboard = liveplot().start()

for packet in capture.sniff_continuously(packet_count=9999):
    print('\nJust arrived:')

    if packet.transport_layer == "TCP":
        print("TCP", packet.ip.src, packet.ip.dst)
        breakdown_src = packet.ip.src.split(".")
        breakdown_dst = packet.ip.dst.split(".")
        if breakdown_dst[0] == "1":
            source = float(breakdown_src[-2]+"."+breakdown_src[-1])
            dest = float(breakdown_dst[-2]+"."+breakdown_dst[-1])
            create_loc(source)
            create_loc(dest)
            tcp_list_x.append(np.array([get_loc(source), get_loc(dest)]))
            tcp_list_y.append(np.array([source, dest]))

    if packet.transport_layer == "UDP":
        print("UDP", packet.udp.srcport, packet.udp.dstport)
        try:
            print("TCP", packet.ip.src, packet.ip.dst)
            breakdown_src = packet.ip.src.split(".")
            breakdown_dst = packet.ip.dst.split(".")
            if breakdown_dst[0] == "1":
                source = float(breakdown_src[-2]+"."+breakdown_src[-1])
                dest = float(breakdown_dst[-2]+"."+breakdown_dst[-1])
                create_loc(source)
                create_loc(dest)
                udp_list_x.append(np.array([get_loc(source), get_loc(dest)]))
                udp_list_y.append(np.array([source, dest]))
        except:
            print("TCP", packet.ipv6.src, packet.ipv6.dst)
