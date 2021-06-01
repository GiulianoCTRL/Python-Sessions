"""
Update settings of Axis Companion mini cameras, without need for Axis
Companion Software.

Axis VAPIX documentation: https://www.axis.com/vapix-library/
"""
# Read axis documentation +
# APIs to use: 
#       - /axis-cgi/rootpwdsetvalue.cgi -> check if root exists
#       - /axis-cgi/pwdgrp.cgi -> change password/create initial user
# action=add&user=root&pwd=pass&grp=root&sgrp=admin:operator:viewer:ptz
# Read json for settings +
# Check requests for success
# Test if camera has been reset/setup/available
# Exit if not available
# Update settings

import json

import requests
from requests.auth import HTTPDigestAuth


def _read_settings() -> dict:
    """Read settings from json file."""

    with open("settings.json", mode="r") as jsonfile:
        # json.load analyses the contents of a json file and converts
        # it to a regular python dictionary
        settings = json.load(jsonfile)
    return settings


def _send_request(host: str, api: str, params=None, auth=None) -> requests.Response:
    """Send request to device.
    
    :param host:        IP or host address of AXIS device
    :param api:         API to use when sending request, inc. first /
    :param params:      Eventual parameters for API as dict
    :param auth:        Authentication if required
    :return:            Successful response object
    """

    resp = requests.get(f"http://{host}{api}", params=params, auth=auth)
    resp.raise_for_status()
    return resp


if __name__ == '__main__':
    print(_read_settings())
