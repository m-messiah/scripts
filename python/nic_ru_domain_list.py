#!/usr/bin/python

import requests
import json
from dns import query, name as dns_name
import dns.message

s = requests.Session()
login = s.post("https://www.nic.ru/login/manager/",
               verify=False,
               data={'login': '',
                     'client_type': 'NIC-D',
                     'password': '',
                     'password_type': 'adm'})
if login.status_code == 200:
    csv = s.get("https://www.nic.ru/manager/my_domains.cgi"
                "?step=srv.my_domains&view.format=csv",
                verify=False)
    if csv.status_code == 200:
        csv = csv.text.encode("utf8")

        # Check if NS is correct
        def check_dns(domain, ns):
            ns_s = filter(len, map(lambda s: s.strip(),
                                   ns.replace('"', '').split(';')))
            if len(ns_s) < 1:
                return {}
            mess = dns.message.make_query(dns_name.from_text(domain),
                                          dns.rdatatype.SOA)
            result = {}
            for ns in ns_s:
                try:
                    name_s = dns_name.from_text(ns.split()[0]).to_text()
                    answer = query.tcp(mess, name_s, timeout=2)
                    if len(answer.authority):
                        result[ns] = True
                    else:
                        rr = answer.answer[0][0]
                        if rr.rdtype == dns.rdatatype.SOA:
                            result[ns] = True
                        else:
                            result[ns] = False
                except:
                    result[ns] = False
            return result

        def get_dns_info(info):
            return {
                'domain': info[0],
                # You can assign without check
                # 'ns': info[2],
                'ns': check_dns(info[1], info[2]),
                'status': info[5],
                'sost': info[6],
                'till': info[7]
            }
        csv = map(lambda l: get_dns_info(l.split(",")),
                  filter(len, csv.split("\n")[2:]))
        with open("nic.ru.json", "w") as config:
            config.write(json.dumps(csv))
