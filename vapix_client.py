"""
Vapix module to interact with AXIS IP devices more easily.

Created 2021-04-09
"""
import requests
from requests.auth import HTTPDigestAuth


def get_ips_from_text(filename: str) -> list:
    """Iterate over IP addresses in a given file and return them  as a list.

    :param filename:        Path or name of file to iterate over
    :return:                A list of IP address
    """
    ip_list = []
    with open(filename, mode="r") as file_handle:
        for line in file_handle:
            ip_list.append(line.strip())

    return ip_list


def fetch_params(host: str, password: str = "pass") -> dict:
    """Fetch parameters from AXIS device via param.cgi.

    :param ip:          IPv4 address of an AXIS device
    :param password:    Password for root user, default = pass
    :return:            Dictionary containing the device's settings
    """
    # https://docs.python-requests.org/en/latest
    # https://realpython.com/python-requests/
    settings = {}
    req = requests.get(
        f"http://{host}/axis-cgi/param.cgi?action=list",
        auth=HTTPDigestAuth("root", password),
    )
    # Does request succeed?
    req.raise_for_status()
    print(req.text)

    return settings


for ip_address in get_ips_from_text("ip_list.txt"):
    fetch_params(ip_address)
