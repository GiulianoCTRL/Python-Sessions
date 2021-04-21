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

    :param host:        IPv4 address of an AXIS device
    :param password:    Password for root user, default = pass
    :return:            Dictionary containing the device's settings
    """
    # https://docs.python-requests.org/en/latest
    # https://realpython.com/python-requests/
    response = requests.get(
        f"http://{host}/axis-cgi/param.cgi?action=list",
        auth=HTTPDigestAuth("root", password),
    )
    # Does request succeed?
    response.raise_for_status()

    settings = {}
    # Get response content as text
    param_text = response.text
    # split string after each newline symbol (\n) into a list of strings
    param_list = param_text.split("\n")
    for line in param_list:
        # Check that param is not empty, continue to next item in loop
        if line == "":
            continue
        # Initialize two variables at the same time, as we split each line
        # into a list of two strings, the left side of the = and the right side
        # of it
        param, value = line.split("=", maxsplit=1)
        # Add a key (name of the parameter) with the value of the parameter
        settings[param] = value

    # Return the freshly populated settings dict!
    return settings


def fetch_server_report(host: str, password: str = "pass") -> str:
    """Describe how this function works."""


for ip_address in get_ips_from_text("ip_list.txt"):
    print(fetch_params(ip_address))
