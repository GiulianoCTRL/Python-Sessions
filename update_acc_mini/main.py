"""
Update settings of Axis Companion mini cameras, without need for Axis
Companion Software.

Axis VAPIX documentation: https://www.axis.com/vapix-library/
"""
# Read axis documentation +
# APIs to use:
#       - /axis-cgi/rootpwdsetvalue.cgi -> check if root exists
#       - /axis-cgi/pwdgrp.cgi -> change password/create initial user
# params for above cgi
# action=add&user=root&pwd=pass&grp=root&sgrp=admin:operator:viewer:ptz
# Read json for settings +
# Check requests for success
# Test if camera has been reset/setup/available
# Exit if not available
# Update settings

import json

import requests

# from requests.auth import HTTPDigestAuth


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


def is_root_set(host: str) -> bool:
    """Check if root account has been configured for AXIS device.

    :param host:        IP or host address of AXIS device
    :return:            Whether root is configured
    """
    # https://docs.python-requests.org/en/latest/api/#requests.Response.text
    resp = _send_request(host, "/axis-cgi/rootpwdsetvalue.cgi").text
    # bool() function returns if a statement is True or False
    return bool("yes" in resp.split("=")[-1])


def create_root_account(host: str, password: str):
    """Create root account for AXIS device.
    :param host:        IP or host address of AXIS device
    :param pass:        new password from json
    :return:            ?
    """
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    # API to use /axis-cgi/pwdgrp.cgi
    # params for API: action=add&user=root&pwd=pass&grp=root&sgrp=admin:operator:viewer:ptz
    payload = {
        "action": "add",
        "user": "root",
        "pwd": password,
        "grp": "root",
        "sgrp": "admin:operator:viewer:ptz",
    }
    resp = _send_request(f"http://{host}/axis-cgi/pwdgrp.cgi", params=payload).text
    if "Created account root" not in resp:
        raise ValueError(f"Root account not created, response content {resp}")


def main():
    """Run script."""
    # Read settings into dict
    settings = _read_settings()
    host = settings["src"]
    # Check if root account is set
    if not is_root_set(host):
        # If root is not set, create root account
        password = settings["password"]
        create_root_account(host, password)


# If file is directly executed ($ python3 filename.py) the file will
# internally (in python) be known as __main__
# If a file is imported it will be known by it's filename, e.g.
# if the file is named "something.py" it is known as something
if __name__ == "__main__":
    print(main())
