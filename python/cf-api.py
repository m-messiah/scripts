from requests import Session

conn = Session()
conn.headers = {
    'X-Auth-Email': "",
    'X-Auth-Key': "",
}

ENDPOINT = "https://api.cloudflare.com/client/v4/"


def get_pages(conn, url):
    result = []
    try:
        resp = conn.get(ENDPOINT + url)
        if resp.status_code != 200:
            return result
        resp = resp.json()
        result.extend(resp['result'])
        total_pages = resp['result_info']['total_pages']
        if total_pages > 1:
            for page in range(2, total_pages + 1):
                resp = conn.get(ENDPOINT + url, params={'page': page})
                if resp.status_code != 200:
                    break
                result.extend(resp.json()['result'])
    except Exception as error:
        print(error)
    finally:
        return result

zones = {zone['name']: (zone['id'], zone['created_on']) for zone in get_pages(conn, "zones")}
##########################
# Below is modified code #
##########################
from json import dumps


for zone in zones:
    dns = get_pages(conn, "zones/%s/dns_records?type=TXT" % zones[zone][0])
    dmarc = False
    spf = False
    for record in dns:
        if "dmarc" in record['name']:
            dmarc = True
        if "spf" in record['content']:
            spf = True
    print(zone)
    if not dmarc:
        r = conn.post(ENDPOINT + "zones/%s/dns_records" % zones[zone][0], headers={"Content-Type": "application/json"}, data=dumps({'type': "TXT", "name": "_dmarc.%s." % zone, "content": "v=DMARC1; p=reject"}))
        print(r.json())
    if not spf:
        r = conn.post(ENDPOINT + "zones/%s/dns_records" % zones[zone][0], headers={"Content-Type": "application/json"}, data=dumps({'type': "TXT", "name": "%s." % zone, "content": "v=spf1 -all"}))
        print(r.json())




exit(0)

## Browser integrity check disable"
for zone, zid in zones.items():
    r = conn.patch(ENDPOINT + "zones/%s/settings/browser_check" % zid,
                   data=dumps({'value': 'off'}),
                   headers={"Content-Type": "application/json"})
    print(zone)
    print(r.text)
