#!/usr/bin/env python

import os
import requests
import urllib3

urllib3.disable_warnings()


def set_grafana_users_readonly(grafana_url, token, exclude={}):
    s = requests.Session()
    s.headers.update({'Authorization': 'Bearer ' + token})
    users_request = s.get(grafana_url + '/api/org/users', verify=False)
    users = users_request.json()
    for user in users:
        # Skip non-editors
        if user['role'] == 'Viewer':
            continue
        # Skip excluded users
        if user['login'] in exclude:
            continue

        req = s.patch(
            grafana_url + '/api/org/users/%s' % user['userId'],
            data={"role": "Viewer"}
        )
        print("%s %s" % (user['login'], req.json()))


if __name__ == '__main__':
    set_grafana_users_readonly(
        os.getenv('GRAFANA_URL'),
        os.getenv('GRAFANA_TOKEN'),
        {
            'admin',
            # Add your users here
        }
    )
