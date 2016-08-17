#!/usr/bin/env python
def IP2Int(ip):
    o = list(map(int, ip.split('.')))
    res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
    return res


def Int2IP(ipnum):
    o = []
    for i in range(0, 4):
        o.append(ipnum % 256)
        ipnum /= 256
    return ".".join(map(str, o[::-1]))

if __name__ == "__main__":
    import sys
    if "." in sys.argv[1]:
        print(IP2Int(sys.argv[1]))
    else:
        print(Int2IP(int(sys.argv[1])))
