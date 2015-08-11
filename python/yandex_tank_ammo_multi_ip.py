#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def make_ammo(headers):
    """ makes phantom ammo """
    #http request w/o entity body template
    req_template = (
          "GET / HTTP/1.1\r\n"
          "%s\r\n"
          "\r\n"
    )

    req = req_template % headers

    #phantom ammo template
    ammo_template = (
        "%d geoip\n"
        "%s"
    )

    return ammo_template % (len(req), req)

def main():
    for stdin_line in sys.stdin:
        try:
            ip = stdin_line.strip()
        except:
            ip = stdin_line

        headers = "Host: example.com\r\n" + \
            "User-Agent: tank\r\n" + \
            "Accept: */*\r\n" + \
            "X-Real-IP: %s\r\n" % ip + \
            "Connection: Close"

        sys.stdout.write(make_ammo(headers))

if __name__ == "__main__":
    main()
